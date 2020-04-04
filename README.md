# CMS_with_GUI

You need to have mySQL installed with 'cms_customer' as Database Name and 'cmscustomer' as the Table Name; in which the details of the customers are stored.

The schema of the table is here:

CREATE TABLE cmscustomer(
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50) NOT NULL,
address VARCHAR(250),
mobile VARCHAR(15) UNIQUE NOT NULL);
