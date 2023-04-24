Create Database vehicle;
use vehicle;

create table vehicle1
( sname varchar(50),
  address varchar(250), 
  phnum bigint, 
  vehiclenum varchar(15)
);

create table vehicle2
( sname varchar(50),
  address varchar(250), 
  phnum bigint, 
  vehiclenum varchar(15)
);

INSERT INTO vehicle1 (sname, address, phnum, vehiclenum)
VALUES ("Aadithyan", "Gandhipuram", 6369980025, "TN42A4567");
INSERT INTO vehicle1 (sname, address, phnum, vehiclenum)
VALUES ("Arvind", "Peelamedu", 9940522570, "TN42A4567");

INSERT INTO vehicle2 (sname, address, phnum, vehiclenum)
VALUES ("Ashika", "SaibabaColony", 6369980025, "TN42A4568");
INSERT INTO vehicle2 (sname, address, phnum, vehiclenum)
VALUES ("Bharath", "Vadavalli", 9940522570, "TN42A4568");

select * from vehicle1;
select * from vehicle2;