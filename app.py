import random
import time
from datetime import datetime

from flask import Flask
from flask_restful import Resource, Api, reqparse

import config
from db_helper import DbHelper

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('type', location='args')
parser.add_argument('id', type=int, location='args')
parser.add_argument('rating', type=int, location='args')
parser.add_argument('price', type=int, location='args')
parser.add_argument('num', type=int, location='args')
parser.add_argument('authorization', location='headers')
db_helper = DbHelper()
critical_error_time = None


def send_503():
    return critical_error_time and (
            datetime.now() - critical_error_time).total_seconds() < config.SERVICE_UNAVAILABLE_TIMEOUT


class Products(Resource):
    def get(self):
        if send_503():
            return {"message": "service unavailable"}, 503
        args = parser.parse_args()
        # 15% chance of getting an error
        if random.randrange(100) < 15:
            return {"message": "internal server error"}, 500
        if args["type"]:
            if args["type"] not in config.ALLOWED_PRODUCT_TYPES:
                return {"message": "product type '{}' is not applicable".format(args["type"])}, 400
        return db_helper.get_products_as_json(args["type"])


class Product(Resource):
    def get(self, product_id=None):
        if send_503():
            return {"message": "service unavailable"}, 503
        args = parser.parse_args()
        args["id"] = args["id"] if args["id"] else product_id
        if not args["id"]:
            return {"message": "missing required parameter in the query string ('id')"}, 400
        product = db_helper.get_product_by_id(args["id"])
        if args["type"]:
            if args["type"] not in config.ALLOWED_PRODUCT_TYPES:
                return {"message": "product type '{}' is not applicable".format(args["type"])}, 400
        if product:
            if args["type"] and product["type"] != args["type"]:
                return {"message": "product id '{}' with type '{}' does not exist".format(args["id"],
                                                                                          args["type"])}, 400
            return product
        return {"message": "product not found"}, 404

    def post(self):
        if send_503():
            return {"message": "service unavailable"}, 503
        args = parser.parse_args()
        token = args["authorization"][7:] if args["authorization"] else args["authorization"]
        if token not in config.TOKENS:
            return {"message": "unauthorized"}, 401
        if not (args["name"] or args["type"] or args["price"]):
            return {"message": "missing required parameter in the query string ('name', 'type', 'price')"}, 400
        args["rating"] = args["rating"] if args["rating"] else 0
        args["num"] = args["num"] if args["num"] else 0
        if args["type"] not in config.ALLOWED_PRODUCT_TYPES:
            return {"message": "product type '{}' is not applicable".format(args["type"])}, 400
        if args["price"] and 0.99 > args["price"] > 5000:
            return {"message": "product price is out range (0,99 to 5000)"}, 400
        if args["rating"] and 0 > args["rating"] > 5:
            return {"message": "product rating is out range (0 to 5)"}, 400
        if args["num"] and 0 > args["num"] > 1000:
            return {"message": "product number is out range (0 to 1000)"}, 400
        db_helper.add_product(args["name"], args["type"], args["price"], args["rating"], args["num"])
        # random 5-15 sec sleep before response
        time.sleep(random.randint(5, 15))
        return {"message": "product '{}' added".format(args["name"])}, 201

    def delete(self, product_id=None):
        if send_503():
            return {"message": "service unavailable"}, 503
        args = parser.parse_args()
        token = args["authorization"][7:] if args["authorization"] else args["authorization"]
        if token not in config.TOKENS:
            return {"message": "unauthorized"}, 401
        args["id"] = args["id"] if args["id"] else product_id
        if not (args["id"] or args["type"] or (args["num"] is not None)):
            return {"message": "missing required parameter in the query string ('id', 'type', 'num')"}, 400
        if args["id"] and (args["id"] or (args["num"] is not None)):
            if args["num"] is not None:
                db_helper.update_product_number(args["id"], args["num"])
                return {"message": "product number updated"}
            db_helper.delete_product(args["id"])
            return {"message": "product number updated"}
        if args["type"] and (args["id"] or (args["num"] is not None)):
            return {"message": "not applicable combination of parameters in the query string"}, 400
        if args["type"]:
            if args["type"] not in config.ALLOWED_PRODUCT_TYPES:
                return {"message": "product type '{}' is not applicable".format(args["type"])}, 400
            return {"message": "products with type '{}' deleted".format(args["type"])}


class ProductNumber(Resource):
    def get(self, product_id=None):
        if send_503():
            return {"message": "service unavailable"}, 503

        args = parser.parse_args()
        args["id"] = args["id"] if args["id"] else product_id
        if not (args["id"] or args["type"] or (args["rating"] is not None)):
            return {"message": "missing required parameter in the query string ('id', 'type', 'rating')"}, 400
        if sum(bool(i) for i in (args["id"], args["type"], args["rating"])) > 1:
            return {
                       "message": "the query string should contain only one required parameter ('id', 'type', 'rating')"}, 400
        number = 0
        if args["id"]:
            for p in db_helper.get_products():
                if p.id == args["id"]:
                    number += p.number
            return {"message": "total number products with id '{}'".format(args["id"]),
                    "number": number}
        if args["type"]:
            for p in db_helper.get_products():
                if p.type == args["type"]:
                    number += p.number
            return {"message": "total number products with type '{}'".format(args["type"]),
                    "number": number}
        if args["rating"] is not None:
            if args["rating"] == 0:
                global critical_error_time
                critical_error_time = datetime.now()
                return {"message": "internal server error"}, 500
            for p in db_helper.get_products():
                if p.rating == args["rating"]:
                    number += p.number
            return {"message": "total number products with rating '{}'".format(args["rating"]),
                    "number": number}


api.add_resource(Products, '/products')
api.add_resource(Product, '/product', '/product/<int:product_id>')
api.add_resource(ProductNumber, '/product_number', '/product_number/<int:product_id>')

if __name__ == '__main__':
    app.run()
