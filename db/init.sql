CREATE DATABASE IF NOT EXISTS Model_Logger;

USE Model_Logger;

CREATE TABLE IF NOT EXISTS Log (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Current_Date_Time DATETIME,
    Input_Params VARCHAR(255),
    Output VARCHAR(255),
    Response_Time FLOAT
);

ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root';
FLUSH PRIVILEGES;