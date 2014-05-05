CREATE DATABASE IF NOT EXISTS Scrapy;
CREATE TABLE IF NOT EXISTS Scrapy.AirQuality (
    station VARCHAR(32),
    timestamp DATETIME,
    air_quality INT,
    PRIMARY KEY (station, timestamp));
GRANT ALL ON Scrapy.AirQuality TO 'scrapy'@'localhost' IDENTIFIED BY 'some_password';
FLUSH PRIVILEGES;
