USE baseAdvertiser;
-- DROP TABLE ADVERTISER;
-- DROP TABLE AD;
CREATE TABLE ADVERTISER(
   ID   INT NOT NULL   ,
   name VARCHAR (30)   ,
   clicks INT DEFAULT 0,
   views INT DEFAULT 0,    
   PRIMARY KEY (ID) 
)
CREATE TABLE AD(
   ID   INT NOT NULL   ,
   title VARCHAR (30)   ,
   ImgURL  VARCHAR (100)   ,
   link VARCHAR (100) ,
   advertiser INT  references ADVERTISER(ID) ,
   clicks INT DEFAULT 0,
   views INT DEFAULT 0,    
   PRIMARY KEY (ID)
)