-- Active: 1749955578181@@127.0.0.1@3306@mydb
-- ###############
-- RESET Database to sample data
-- Citation for the following sql code:
-- Date: 6/9/25
-- Modified from the base code provided in the PL/SQL Exploration
-- Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-pl-slash-sql-part-1-sp-view-and-function?module_item_id=25352958
-- ###############
DROP PROCEDURE IF EXISTS sp_ResetDB;


CREATE PROCEDURE sp_ResetDB()
BEGIN

    -- Table drops for testing purposes
    DROP TABLE IF EXISTS DeviceServices;-- KnownThreats table
    DROP TABLE IF EXISTS IncidentDevices;
    DROP TABLE IF EXISTS Responses;
    DROP TABLE IF EXISTS Incidents;
    DROP TABLE IF EXISTS Devices;
    DROP TABLE IF EXISTS KnownThreats;
    DROP TABLE IF EXISTS Services;
    DROP TABLE IF EXISTS Users;

    -- Table Creation

    -- Users table
    CREATE TABLE Users (
        userID INT AUTO_INCREMENT not NULL UNIQUE,
        firstName VARCHAR(100) not NULL,
        lastName VARCHAR(100) not NULL,
        email VARCHAR(200) not NULL UNIQUE,
        department VARCHAR(100),
        role ENUM('admin', 'user') not NULL,

        PRIMARY KEY (userID)
    );

    -- Services table
    CREATE TABLE Services (
        serviceID INT AUTO_INCREMENT not NULL UNIQUE,
        serviceName VARCHAR(100) not NULL UNIQUE,
        port INT,
        protocol ENUM('TCP', 'UDP', 'Other'),

        PRIMARY KEY (serviceID)
    );

    -- KnownThreats table
    CREATE TABLE KnownThreats (
        threatID INT AUTO_INCREMENT not NULL UNIQUE,
        name VARCHAR(100) not NULL,
        type ENUM('Malware', 'Exploit', 'Tool', 'Other'),
        description TEXT,
        dateFirstSeen DATETIME,
        dateLastSeen DATETIME,

        PRIMARY KEY (threatID)
    );

    -- Devices table
    CREATE TABLE Devices (
        deviceID INT AUTO_INCREMENT not NULL UNIQUE,
        deviceName VARCHAR(100) not NULL UNIQUE,
        IPAddress VARCHAR(100) not NULL UNIQUE,
        deviceType ENUM('Server', 'PC', 'VM', 'Other'),
        status ENUM('Active', 'Offline', 'Disabled'),
        assignedTo INT,

        FOREIGN KEY (assignedTo) REFERENCES Users(userID) ON DELETE CASCADE ON UPDATE CASCADE,

        PRIMARY KEY (deviceID)
    );

    -- Incidents table
    CREATE TABLE Incidents (
        incidentID INT AUTO_INCREMENT not NULL UNIQUE,
        timeOccurred DATETIME not NULL,
        description TEXT,
        priority INT,
        status ENUM('Not Started', 'In Progress', 'Completed'),
        threatID INT,

        FOREIGN KEY (threatID) REFERENCES KnownThreats(threatID) ON DELETE CASCADE ON UPDATE CASCADE,

        PRIMARY KEY (incidentID)
    );

    -- Responses table
    CREATE TABLE Responses (
        responseID INT AUTO_INCREMENT not NULL UNIQUE,
        incidentID INT,
        userID INT,
        timeStarted DATETIME,
        timeEnded DATETIME,
        actionPerformed TEXT,
        status ENUM('Not Started', 'In Progress', 'Completed'),

        FOREIGN KEY (incidentID) REFERENCES Incidents(incidentID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (userID) REFERENCES Users(userID) ON DELETE SET NULL ON UPDATE CASCADE,

        PRIMARY KEY (responseID)

    );

    -- IncidentDevices table
    CREATE TABLE IncidentDevices (
        incidentDevicesID INT AUTO_INCREMENT,
        incidentID INT NOT NULL,
        deviceID INT NOT NULL,

        FOREIGN KEY (incidentID) REFERENCES Incidents(incidentID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (deviceID) REFERENCES Devices(deviceID) ON DELETE CASCADE ON UPDATE CASCADE,

        PRIMARY KEY (incidentDevicesID)
    );

    -- DeviceServices
    CREATE TABLE DeviceServices (
        deviceServiceID INT AUTO_INCREMENT,
        deviceID INT,
        serviceID INT,

        FOREIGN KEY (deviceID) REFERENCES Devices(deviceID) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (serviceID) REFERENCES Services(serviceID) ON DELETE CASCADE ON UPDATE CASCADE,

        PRIMARY KEY (deviceServiceID)
    );

    INSERT INTO Users (firstName, lastName, email, department, role)
    VALUES
    ('John', 'Doe', 'johndoe@gmail.com', 'IT', 'admin'),
    ('Demetrius', 'Cross', 'user1@gmail.com', 'IT', 'user'),
    ('Dawson', 'Herrington', 'user2@gmail.com', 'IT', 'user'),
    ('Jane', 'Smith', 'admin2@gmail.com', 'HR', 'admin');

    INSERT INTO Services (serviceName, port, protocol)
    VALUES
    ('HTTP', 80, 'TCP'),
    ('HTTPS', 443, 'TCP'),
    ('FTP', 21, 'TCP'),
    ('SSH', 22, 'TCP'),
    ('DNS', 53, 'UDP');

    INSERT INTO KnownThreats (name, type, description, dateFirstSeen, dateLastSeen)
    VALUES
    ('WannaCry', 'Malware', 'Ransomware that encrypts files and demands payment.', '2025-03-01 00:00:00', '2025-04-15 00:00:00'),
    ('SQL Injection', 'Exploit', 'Code injection technique that exploits a security vulnerability.', '2024-12-25 00:00:00', '2025-01-01 00:00:00'),
    ('Phishing', 'Tool', 'Fraudulent attempt to obtain sensitive information.', '2024-10-09 00:00:00', '2025-03-02 00:00:00'),
    ('DDoS Attack', 'Other', 'Distributed denial-of-service attack.', '2024-07-01 00:00:00', '2024-11-26 12:34:56');

    INSERT INTO Devices (deviceName, IPAddress, deviceType, status, assignedTo)
    VALUES
    ('Server1', 'deviceserver1.local', 'Server', 'Active', 1),
    ('PC1', 'devicepc1.local', 'PC', 'Active', 2),
    ('VM1', 'devicevm1.local', 'VM', 'Offline', 3),
    ('Router1', 'devicerouter1.local', 'Other', 'Disabled', 4);

    INSERT INTO Incidents (timeOccurred, description, priority, status, threatID)
    VALUES
    ('2025-03-01 12:00:00', 'WannaCry ransomware detected on server.', 1, 'In Progress', 1),
    ('2024-12-25 15:30:00', 'SQL Injection attempt on web application.', 2, 'Not Started', 2),
    ('2024-10-09 09:00:00', 'Phishing email reported by user.', 3, 'Completed', 3),
    ('2024-07-01 18:00:00', 'DDoS attack detected on network.', 1, 'In Progress', 4);

    INSERT INTO Responses (incidentID, userID, timeStarted, timeEnded, actionPerformed, status)
    VALUES
    (1, 1, '2025-03-01 12:30:00', '2025-03-01 14:00:00', 'Isolated server and initiated malware scan.', 'Completed'),
    (2, 2, '2024-12-25 16:00:00', '2024-12-25 17:00:00', 'Reviewed logs and implemented security patch.', 'Completed'),
    (3, 3, '2024-10-09 10:00:00', '2024-10-09 11:00:00', 'Informed users and blocked sender.', 'Completed'),
    (4, 4, '2024-07-01 19:00:00', NULL, 'Mitigated attack and monitored traffic.', 'In Progress');

    INSERT INTO IncidentDevices (incidentID, deviceID)
    VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4);

    INSERT INTO DeviceServices (deviceID, serviceID)
    VALUES
    (1, 1),
    (1, 2),
    (2, 3),
    (3, 4);
END;








-- Delete Procedures
CREATE PROCEDURE sp_DeleteUser(IN u_id INT)
BEGIN
    DECLARE error_message VARCHAR(255);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Rollback the transaction in case of an error
        ROLLBACK;
        -- Optionally, you can log the error or raise a custom error message
        RESIGNAL;
    END;

    START TRANSACTION;

    DELETE FROM Users WHERE userID = u_id;

    -- Check if the user was deleted
    IF ROW_COUNT() = 0 THEN
        set error_message = CONCAT('No matching recond found in Users table for userID: ', u_id);
        -- User not found, raise an error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
    END IF;
    
    COMMIT;

END;

-- Create/Insert Procedures
CREATE PROCEDURE sp_CreateUser(
    IN p_firstName VARCHAR(100), IN p_lastName VARCHAR(100),
    IN p_email VARCHAR(200), IN p_department VARCHAR(100), IN p_role ENUM('admin', 'user')
)
BEGIN
    DECLARE p_id INT;
    DECLARE error_message VARCHAR(255);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Rollback the transaction in case of an error
        ROLLBACK;
        -- Optionally, you can log the error or raise a custom error message
        RESIGNAL;
    END;

    START TRANSACTION;

    INSERT INTO Users (firstName, lastName, email, department, role)
    VALUES (p_firstName, p_lastName, p_email, p_department, p_role);
    

    -- Check if the user was created
    IF ROW_COUNT() = 0 THEN
        set error_message = CONCAT('Failed to create user with email: ', p_email);
        -- User not created, raise an error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
    END IF;

    -- Get the last inserted userID
    SET p_id = LAST_INSERT_ID();

    COMMIT;

END;

CREATE PROCEDURE sp_CreateIncident(
    IN p_timeOccurred DATETIME, IN p_description TEXT,
    IN p_priority INT, IN p_status ENUM('Not Started', 'In Progress', 'Completed'),
    IN p_threatID INT
)
BEGIN
    DECLARE p_id INT;
    DECLARE error_message VARCHAR(255);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Rollback the transaction in case of an error
        ROLLBACK;
        -- Optionally, you can log the error or raise a custom error message
        RESIGNAL;
    END;

    START TRANSACTION;

    INSERT INTO Incidents (timeOccurred, description, priority, status, threatID)
    VALUES (p_timeOccurred, p_description, p_priority, p_status, p_threatID);
    
    -- Check if the incident was created
    IF ROW_COUNT() = 0 THEN
        set error_message = CONCAT('Failed to create incident with description: ', p_description);
        -- Incident not created, raise an error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
    END IF;

    -- Get the last inserted incidentID
    SET p_id = LAST_INSERT_ID();

    COMMIT;

END;

CREATE PROCEDURE sp_CreateIncidentDevice(
    IN p_incidentID INT, IN p_deviceID INT
)
BEGIN
    DECLARE p_id INT;
    DECLARE error_message VARCHAR(255);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Rollback the transaction in case of an error
        ROLLBACK;
        -- Optionally, you can log the error or raise a custom error message
        RESIGNAL;
    END;

    START TRANSACTION;

    INSERT INTO IncidentDevices (incidentID, deviceID)
    VALUES (p_incidentID, p_deviceID);
    
    -- Check if the incident device was created
    IF ROW_COUNT() = 0 THEN
        set error_message = CONCAT('Failed to create IncidentDevice for incidentID: ', p_incidentID, ' and deviceID: ', p_deviceID);
        -- IncidentDevice not created, raise an error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
    END IF;

    -- Get the last inserted incidentDevicesID
    SET p_id = LAST_INSERT_ID();

    COMMIT;

END;

CREATE PROCEDURE sp_CreateResponse(
    IN p_incidentID INT, IN p_userID INT, IN p_timeStarted DATETIME,
    IN p_timeEnded DATETIME, IN p_actionPerformed TEXT,
    IN p_status ENUM('Not Started', 'In Progress', 'Completed')
)

BEGIN
    DECLARE p_id INT;
    DECLARE error_message VARCHAR(255);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Rollback the transaction in case of an error
        ROLLBACK;
        -- Optionally, you can log the error or raise a custom error message
        RESIGNAL;
    END;

    START TRANSACTION;

    INSERT INTO Responses (incidentID, userID, timeStarted, timeEnded, actionPerformed, status)
    VALUES (p_incidentID, p_userID, p_timeStarted, p_timeEnded, p_actionPerformed, p_status);
    
    -- Check if the response was created
    IF ROW_COUNT() = 0 THEN
        set error_message = CONCAT('Failed to create response for incidentID: ', p_incidentID);
        -- Response not created, raise an error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
    END IF;

    -- Get the last inserted responseID
    SET p_id = LAST_INSERT_ID();

    COMMIT;

END;

CREATE PROCEDURE sp_CreateDevice(
    IN p_deviceName VARCHAR(100), IN p_IPAddress VARCHAR(100),
    IN p_deviceType ENUM('Server', 'PC', 'VM', 'Other'),
    IN p_status ENUM('Active', 'Offline', 'Disabled'), IN p_assignedTo INT
)

BEGIN
    DECLARE p_id INT;
    DECLARE error_message VARCHAR(255);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Rollback the transaction in case of an error
        ROLLBACK;
        -- Optionally, you can log the error or raise a custom error message
        RESIGNAL;
    END;

    START TRANSACTION;

    INSERT INTO Devices (deviceName, IPAddress, deviceType, status, assignedTo)
    VALUES (p_deviceName, p_IPAddress, p_deviceType, p_status, p_assignedTo);
    
    -- Check if the device was created
    IF ROW_COUNT() = 0 THEN
        set error_message = CONCAT('Failed to create device with name: ', p_deviceName);
        -- Device not created, raise an error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
    END IF;

    -- Get the last inserted deviceID
    SET p_id = LAST_INSERT_ID();

    COMMIT;

END;

CREATE PROCEDURE sp_CreateDeviceService(
    IN p_deviceID INT, IN p_serviceID INT
)

BEGIN
    DECLARE p_id INT;
    DECLARE error_message VARCHAR(255);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Rollback the transaction in case of an error
        ROLLBACK;
        -- Optionally, you can log the error or raise a custom error message
        RESIGNAL;
    END;

    START TRANSACTION;

    INSERT INTO DeviceServices (deviceID, serviceID)
    VALUES (p_deviceID, p_serviceID);
    
    -- Check if the device service was created
    IF ROW_COUNT() = 0 THEN
        set error_message = CONCAT('Failed to create DeviceService for deviceID: ', p_deviceID, ' and serviceID: ', p_serviceID);
        -- DeviceService not created, raise an error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
    END IF;

    -- Get the last inserted deviceServiceID
    SET p_id = LAST_INSERT_ID();

    COMMIT;

END;

CREATE PROCEDURE sp_CreateService(
    IN p_serviceName VARCHAR(100), IN p_port INT,
    IN p_protocol ENUM('TCP', 'UDP', 'Other')
)

BEGIN
    DECLARE p_id INT;
    DECLARE error_message VARCHAR(255);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Rollback the transaction in case of an error
        ROLLBACK;
        -- Optionally, you can log the error or raise a custom error message
        RESIGNAL;
    END;

    START TRANSACTION;

    INSERT INTO Services (serviceName, port, protocol)
    VALUES (p_serviceName, p_port, p_protocol);
    
    -- Check if the service was created
    IF ROW_COUNT() = 0 THEN
        set error_message = CONCAT('Failed to create service with name: ', p_serviceName);
        -- Service not created, raise an error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
    END IF;

    -- Get the last inserted serviceID
    SET p_id = LAST_INSERT_ID();

    COMMIT;

END;

CREATE PROCEDURE sp_CreateKnownThreat(
    IN p_name VARCHAR(100), IN p_type ENUM('Malware', 'Exploit', 'Tool', 'Other'),
    IN p_description TEXT, IN p_dateFirstSeen DATETIME, IN p_dateLastSeen DATETIME
)

BEGIN
    DECLARE p_id INT;
    DECLARE error_message VARCHAR(255);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Rollback the transaction in case of an error
        ROLLBACK;
        -- Optionally, you can log the error or raise a custom error message
        RESIGNAL;
    END;

    START TRANSACTION;

    INSERT INTO KnownThreats (name, type, description, dateFirstSeen, dateLastSeen)
    VALUES (p_name, p_type, p_description, p_dateFirstSeen, p_dateLastSeen);
    
    -- Check if the known threat was created
    IF ROW_COUNT() = 0 THEN
        set error_message = CONCAT('Failed to create known threat with name: ', p_name);
        -- Known threat not created, raise an error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
    END IF;

    -- Get the last inserted threatID
    SET p_id = LAST_INSERT_ID();

    COMMIT;

END;



CREATE PROCEDURE sp_DeleteIncident(IN inc_id INT)
BEGIN
    DECLARE error_message VARCHAR(255);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Rollback the transaction in case of an error
        ROLLBACK;
        -- Optionally, you can log the error or raise a custom error message
        RESIGNAL;
    END;

    START TRANSACTION;

    DELETE FROM Incidents WHERE incidentID = inc_id;

    -- Check if the user was deleted
    IF ROW_COUNT() = 0 THEN
        set error_message = CONCAT('No matching record found in Incidents table for incidentID: ', inc_id);
        -- User not found, raise an error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
    END IF;
    
    COMMIT;

END;

CREATE PROCEDURE sp_DeleteIncidentDevice(IN incDev_id INT)
BEGIN
    DECLARE error_message VARCHAR(255);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Rollback the transaction in case of an error
        ROLLBACK;
        -- Optionally, you can log the error or raise a custom error message
        RESIGNAL;
    END;

    START TRANSACTION;

    DELETE FROM IncidentDevices WHERE incidentDevicesID = incDev_id;

    -- Check if the user was deleted
    IF ROW_COUNT() = 0 THEN
        set error_message = CONCAT('No matching record found in IncidentDevices table for deviceID: ', incDev_id);
        -- User not found, raise an error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
    END IF;
    
    COMMIT;

END;

CREATE PROCEDURE sp_DeleteResponse(IN r_id INT)
BEGIN
    DECLARE error_message VARCHAR(255);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Rollback the transaction in case of an error
        ROLLBACK;
        -- Optionally, you can log the error or raise a custom error message
        RESIGNAL;
    END;

    START TRANSACTION;

    DELETE FROM Responses WHERE responseID = r_id;

    -- Check if the user was deleted
    IF ROW_COUNT() = 0 THEN
        set error_message = CONCAT('No matching record found in Responses table for responseID: ', r_id);
        -- User not found, raise an error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
    END IF;
    
    COMMIT;

END;

CREATE PROCEDURE sp_DeleteDevice(IN dev_id INT)
BEGIN
    DECLARE error_message VARCHAR(255);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Rollback the transaction in case of an error
        ROLLBACK;
        -- Optionally, you can log the error or raise a custom error message
        RESIGNAL;
    END;

    START TRANSACTION;

    DELETE FROM Devices WHERE deviceID = dev_id;

    -- Check if the user was deleted
    IF ROW_COUNT() = 0 THEN
        set error_message = CONCAT('No matching record found in Devices table for deviceID: ', dev_id);
        -- User not found, raise an error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
    END IF;
    
    COMMIT;

END;

CREATE PROCEDURE sp_DeleteDeviceService(IN devServ_id INT)
BEGIN
    DECLARE error_message VARCHAR(255);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Rollback the transaction in case of an error
        ROLLBACK;
        -- Optionally, you can log the error or raise a custom error message
        RESIGNAL;
    END;

    START TRANSACTION;

    DELETE FROM DeviceServices WHERE deviceServiceID = devServ_id;

    -- Check if the user was deleted
    IF ROW_COUNT() = 0 THEN
        set error_message = CONCAT('No matching record found in DeviceServices table for ServiceID: ', devServ_id);
        -- User not found, raise an error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
    END IF;
    
    COMMIT;

END;

CREATE PROCEDURE sp_DeleteService(IN serv_id INT)
BEGIN
    DECLARE error_message VARCHAR(255);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Rollback the transaction in case of an error
        ROLLBACK;
        -- Optionally, you can log the error or raise a custom error message
        RESIGNAL;
    END;

    START TRANSACTION;

    DELETE FROM Services WHERE serviceID = serv_id;

    -- Check if the user was deleted
    IF ROW_COUNT() = 0 THEN
        set error_message = CONCAT('No matching record found in Services table for serviceID: ', serv_id);
        -- User not found, raise an error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
    END IF;
    
    COMMIT;

END;

CREATE PROCEDURE sp_DeleteKnownThreat(IN threat_id INT)
BEGIN
    DECLARE error_message VARCHAR(255);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Rollback the transaction in case of an error
        ROLLBACK;
        -- Optionally, you can log the error or raise a custom error message
        RESIGNAL;
    END;

    START TRANSACTION;

    DELETE FROM KnownThreats WHERE threatID = threat_id;

    -- Check if the user was deleted
    IF ROW_COUNT() = 0 THEN
        set error_message = CONCAT('No matching record found in KnownThreats table for threatID: ', threat_id);
        -- User not found, raise an error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
    END IF;
    
    COMMIT;
    
END;


-- update Procedures

-- update Users
DROP PROCEDURE IF EXISTS sp_UpdateUser;

CREATE PROCEDURE sp_UpdateUser(
    IN p_userID INT, IN p_firstName VARCHAR(100), IN p_lastName VARCHAR(100),
    IN p_email VARCHAR(200), IN p_department VARCHAR(100), IN p_role ENUM('admin', 'user')
)

BEGIN
    UPDATE Users SET firstName = p_firstName, lastName = p_lastName,
    email = p_email, department = p_department, role = p_role
    WHERE userID = p_userID;

END;


-- update Incidents
DROP PROCEDURE IF EXISTS sp_UpdateIncident;

CREATE PROCEDURE sp_UpdateIncident(
    IN p_incidentID INT, IN p_timeOccurred DATETIME, IN p_description TEXT,
    IN p_priority INT, IN p_status ENUM('Not Started', 'In Progress', 'Completed'),
    IN p_threatID INT
)
BEGIN
    UPDATE Incidents SET timeOccurred = p_timeOccurred, description = p_description,
    priority = p_priority, status = p_status, threatID = p_threatID
    WHERE incidentID = p_incidentID;

END;


-- update IncidentDevices
DROP PROCEDURE IF EXISTS sp_UpdateIncidentDevice;

CREATE PROCEDURE sp_UpdateIncidentDevice(
    IN p_incidentDevicesID INT, IN p_incidentID INT, IN p_deviceID INT
)
BEGIN
    UPDATE IncidentDevices SET incidentID = p_incidentID, deviceID = p_deviceID
    WHERE incidentDevicesID = p_incidentDevicesID;

END;


-- update Responses
DROP PROCEDURE IF EXISTS sp_UpdateResponse;

CREATE PROCEDURE sp_UpdateResponse(
    IN p_responseID INT, IN p_timeStarted DATETIME, IN p_timeEnded DATETIME,
    IN p_actionPerformed TEXT, IN p_status ENUM('Not Started', 'In Progress', 'Completed')
)
BEGIN
    UPDATE Responses SET timeStarted = p_timeStarted, timeEnded = p_timeEnded,
    actionPerformed = p_actionPerformed, status = p_status
    WHERE responseID = p_responseID;

END;


-- update Devices
DROP PROCEDURE IF EXISTS sp_UpdateDevice;

CREATE PROCEDURE sp_UpdateDevice(
    IN p_deviceID INT, IN p_deviceName VARCHAR(100), IN p_IPAddress VARCHAR(100),
    IN p_deviceType ENUM('Server', 'PC', 'VM', 'Other'), IN p_status ENUM('Active', 'Offline', 'Disabled'),
    IN p_assignedTo INT
)
BEGIN
    UPDATE Devices SET deviceName = p_deviceName, IPAddress = p_IPAddress,
    deviceType = p_deviceType, status = p_status, assignedTo = p_assignedTo
    WHERE deviceID = p_deviceID;

END;


-- update DeviceServices
DROP PROCEDURE IF EXISTS sp_UpdateDeviceService;

CREATE PROCEDURE sp_UpdateDeviceService(
    IN p_deviceServiceID INT, IN p_deviceID INT, IN p_serviceID INT
)
BEGIN
    UPDATE DeviceServices SET deviceID = p_deviceID, serviceID = p_serviceID
    WHERE deviceServiceID = p_deviceServiceID;

END;


-- update Services
DROP PROCEDURE IF EXISTS sp_UpdateService;

CREATE PROCEDURE sp_UpdateService(
    IN p_serviceID INT, IN p_serviceName VARCHAR(100), IN p_port INT,
    IN p_protocol ENUM('TCP', 'UDP', 'Other')
)
BEGIN
    UPDATE Services SET serviceName = p_serviceName, port = p_port, protocol = p_protocol
    WHERE serviceID = p_serviceID;

END;


-- update KnownThreats
DROP PROCEDURE IF EXISTS sp_UpdateKnownThreat;

CREATE PROCEDURE sp_UpdateKnownThreat(
    IN p_threatID INT, IN p_name VARCHAR(100), IN p_type ENUM('Malware', 'Exploit', 'Tool', 'Other'),
    IN p_description TEXT, IN p_dateFirstSeen DATETIME, IN p_dateLastSeen DATETIME
)
BEGIN
    UPDATE KnownThreats SET name = p_name, type = p_type, description = p_description,
    dateFirstSeen = p_dateFirstSeen, dateLastSeen = p_dateLastSeen
    WHERE threatID = p_threatID;

END;
