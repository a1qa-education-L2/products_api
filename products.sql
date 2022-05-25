BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "products" (
	"id"	INTEGER,
	"name"	TEXT,
	"type"	TEXT,
	"rating"	INTEGER,
	"price"	NUMERIC,
	"number"	INTEGER,
	PRIMARY KEY("id")
);
INSERT INTO "products" VALUES (1,'Apple iPhone 13','mobile',4,'1565,74',913);
INSERT INTO "products" VALUES (2,'Apple iPhone 11','mobile',4,'1652,86',838);
INSERT INTO "products" VALUES (3,'Apple iPhone 13 Pro','mobile',3,'1905,75',832);
INSERT INTO "products" VALUES (4,'Apple iPhone 12 Pro','mobile',5,'2060,63',414);
INSERT INTO "products" VALUES (5,'Apple iPhone 12 mini','mobile',3,'1837,99',702);
INSERT INTO "products" VALUES (6,'Apple iPhone 13 mini','mobile',4,'1769,02',97);
INSERT INTO "products" VALUES (7,'Apple iPhone 13 mini','mobile',3,'1771,44',250);
INSERT INTO "products" VALUES (8,'Apple iPhone 11 Pro Max','mobile',5,'2302,63',856);
INSERT INTO "products" VALUES (9,'Samsung Galaxy S21 Ultra 5G','mobile',4,'1871,87',779);
INSERT INTO "products" VALUES (10,'Apple iPhone 12 Pro Max','mobile',3,'2043,69',880);
INSERT INTO "products" VALUES (11,'Xiaomi Mi 11 Ultra','mobile',5,'2309,89',953);
INSERT INTO "products" VALUES (12,'Samsung Galaxy Z Flip3 5G','mobile',4,'1598,41',196);
INSERT INTO "products" VALUES (13,'Samsung Galaxy Z Fold3 5G','mobile',5,'2328,04',360);
INSERT INTO "products" VALUES (14,'Google Pixel 6 Pro','mobile',4,'2375,23',966);
INSERT INTO "products" VALUES (15,'Sony Xperia Pro-I XQ-BE72','mobile',4,'2053,37',50);
INSERT INTO "products" VALUES (16,'Apple iPad 10.2','tablet',4,'908,71',237);
INSERT INTO "products" VALUES (17,'Xiaomi Pad 5','tablet',4,'1239,04',839);
INSERT INTO "products" VALUES (18,'Apple iPad Pro M1','tablet',4,'1137,4',115);
INSERT INTO "products" VALUES (19,'Apple iPad Air','tablet',3,'830,06',732);
INSERT INTO "products" VALUES (20,'Apple iPad mini','tablet',3,'911,13',649);
INSERT INTO "products" VALUES (21,'Huawei MatePad 11','tablet',4,'1087,79',172);
INSERT INTO "products" VALUES (22,'Samsung Galaxy Tab S7','tablet',4,'1200,32',519);
INSERT INTO "products" VALUES (23,'Apple iPad Pro 11','tablet',5,'984,94',219);
INSERT INTO "products" VALUES (24,'Samsung Galaxy Tab S6 Lite LTE','tablet',3,'1070,85',504);
INSERT INTO "products" VALUES (25,'Samsung Galaxy Tab S8 Wi-Fi SM-X700','tablet',4,'1166,44',889);
INSERT INTO "products" VALUES (26,'Samsung Galaxy Tab S7 FE LTE','tablet',5,'1133,77',298);
INSERT INTO "products" VALUES (27,'Microsoft Surface Pro 7','tablet',4,'1218,47',573);
INSERT INTO "products" VALUES (28,'Lenovo Tab P11 Pro TB-J706L','tablet',3,'819,17',870);
INSERT INTO "products" VALUES (29,'Lenovo Yoga Tab 13 YT-K606F','tablet',4,'1185,8',490);
INSERT INTO "products" VALUES (30,'Lenovo IdeaPad Duet 3 10IGL5','tablet',3,'778,03',148);
INSERT INTO "products" VALUES (31,'Apple Macbook Pro 14','computer',3,'2981,44',793);
INSERT INTO "products" VALUES (32,'Apple Macbook Air 13','computer',3,'2958,45',547);
INSERT INTO "products" VALUES (33,'Lenovo Legion 5 Pro','computer',3,'3191,98',91);
INSERT INTO "products" VALUES (34,'Lenovo Legion 5','computer',3,'2929,41',837);
INSERT INTO "products" VALUES (35,'Apple Macbook Pro 13','computer',3,'2848,34',554);
INSERT INTO "products" VALUES (36,'ASUS TUF Gaming Dash F15','computer',3,'3120,59',49);
INSERT INTO "products" VALUES (37,'ASUS ROG Strix G15','computer',4,'2925,78',393);
INSERT INTO "products" VALUES (38,'MSI Sword 15','computer',3,'2910,05',67);
INSERT INTO "products" VALUES (39,'Acer Nitro 5','computer',3,'2585,77',581);
INSERT INTO "products" VALUES (40,'Lenovo Legion 7','computer',5,'2565,2',801);
INSERT INTO "products" VALUES (41,'Apple MacBook Pro 16','computer',3,'2504,7',205);
INSERT INTO "products" VALUES (42,'Xiaomi Mi Notebook Pro 15','computer',4,'3055,25',293);
INSERT INTO "products" VALUES (43,'ASUS ZenBook Pro 15','computer',4,'2452,67',673);
INSERT INTO "products" VALUES (44,'Dell G15','computer',4,'3286,36',162);
INSERT INTO "products" VALUES (45,'MSI Stealth 15M','computer',5,'2492,6',991);
INSERT INTO "products" VALUES (46,'Apple Watch Series 7',NULL,5,'575,96',540);
INSERT INTO "products" VALUES (47,'Xiaomi Mi Watch',NULL,3,'492,47',60);
INSERT INTO "products" VALUES (48,'Samsung Galaxy Watch4 Classic',NULL,5,'451,33',245);
INSERT INTO "products" VALUES (49,'Huawei Watch GT2 Pro',NULL,4,'415,03',189);
INSERT INTO "products" VALUES (50,'Samsung Galaxy Watch3',NULL,4,'511,83',891);
COMMIT;
