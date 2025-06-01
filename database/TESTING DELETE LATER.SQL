-- ###############
-- RESET Database to sample data
-- ###############
DROP PROCEDURE IF EXISTS sp_ResetDB;

DELIMITER //
CREATE PROCEDURE sp_ResetDB()
BEGIN

    -- Table drops for testing purposes
    DROP TABLE IF EXISTS DeviceServices;
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
        FOREIGN KEY (userID) REFERENCES Users(userID) ON DELETE CASCADE ON UPDATE CASCADE,

        PRIMARY KEY (responseID)

    );

    -- IncidentDevices table
    CREATE TABLE IncidentDevices (
        incidentDevicesID INT AUTO_INCREMENT,
        incidentID INT,
        deviceID INT,

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
END //


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

END //

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

END //

CREATE PROCEDURE sp_DeleteIncidentDevice(IN inc_id INT, IN dev_id INT)
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

    DELETE FROM IncidentDevices WHERE incidentID = inc_id AND deviceID = dev_id;

    -- Check if the user was deleted
    IF ROW_COUNT() = 0 THEN
        set error_message = CONCAT('No matching record found in IncidentDevices table for incidentID: ', inc_id, ' and deviceID: ', dev_id);
        -- User not found, raise an error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
    END IF;
    
    COMMIT;

END //

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

END //

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

    DELETE FROM Device WHERE deviceID = dev_id;

    -- Check if the user was deleted
    IF ROW_COUNT() = 0 THEN
        set error_message = CONCAT('No matching record found in Devices table for deviceID: ', dev_id);
        -- User not found, raise an error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
    END IF;
    
    COMMIT;

END //

CREATE PROCEDURE sp_DeleteDeviceService(IN dev_id INT, IN serv_id INT)
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

    DELETE FROM DeviceServices WHERE deviceID = dev_id AND serviceID = serv_id;

    -- Check if the user was deleted
    IF ROW_COUNT() = 0 THEN
        set error_message = CONCAT('No matching record found in DeviceServices table for deviceID: ', dev_id, ' and serviceID: ', serv_id);
        -- User not found, raise an error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = error_message;
    END IF;
    
    COMMIT;

END //

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

END //

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
    
END //




DELIMITER ;

-- update Procedures
DROP PROCEDURE IF EXISTS sp_UpdateUser;
DELIMITER //
CREATE PROCEDURE sp_UpdateUser()