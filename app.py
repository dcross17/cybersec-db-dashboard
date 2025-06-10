# Citation for the following routes:
# Date: 5/6/25
# Base code was for routes was adapted from Exploation - Web Application Technology
# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-web-application-technology-2?module_item_id=25352948


# ########################################
# ########## SETUP

from flask import Flask, render_template, request, redirect, flash
import database.db_connector as db

PORT = 49124

app = Flask(__name__)

# secret key to fascilitate flash messages - I know nothing about encryption so used a string - Dawson - citation in routes section
app.secret_key = "imagine_that_this_has_fancy_encryption"  
# ########################################
# ########## ROUTE HANDLERS

# RESET ROUTE
# Citation for the following code:
# Date: 5/20/25
# Copied from /OR/ Adapted from /OR/ Based on 
# Adapted from the CUD Operations exploration with a small amount of copilot, described below
# Source URL: www.m365.cloud.microsoft
# If AI tools were used: The online line that copilot helped with was the callproc. All other code
# was adapted from our class materials. I could not figure out how to call a procedure with a cursor in this
# context. Prompt used: "How do I call a stored procedure with a cursor in a route handler in Flask?"

# reset route
@app.route("/reset", methods=["POST"])
def reset():
    try:
        dbConnection = db.connectDB()
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return "An error occurred while connecting to the database.", 500

    try:
        cursor = dbConnection.cursor()
        cursor.callproc("sp_ResetDB")
        dbConnection.commit()

        print("Database reset successfully.")

        return redirect("/")
    except Exception as e:
        print(f"Error resetting database: {e}")
        return "An error occurred while resetting the database.", 500
    
    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# READ ROUTES
@app.route("/", methods=["GET"])
def home():
    try:
        return render_template("home.j2")

    except Exception as e:
        print(f"Error rendering page: {e}")
        return "An error occurred while rendering the page.", 500
    

# get users
@app.route("/Users", methods=["GET"])
def Users():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        query1 = "SELECT Users.userID as 'User ID', Users.firstName as 'First Name', Users.lastName as 'Last Name', Users.email as Email, Users.department as Department, Users.role as 'Role' FROM Users;"
        users = db.query(dbConnection, query1).fetchall()
        
        # send the user to the update form if one is selected during an update attempt
        selected_user = None
        user_id = request.args.get("user_id")
        if user_id:
            query2 = "SELECT Users.userID as 'User ID', Users.firstName as 'First Name', Users.lastName as 'Last Name', Users.email as Email, Users.department as Department, Users.role as 'Role' FROM Users WHERE Users.userID = %s;"
            selected_user = db.query(dbConnection, query2, (user_id,)).fetchone()

        # Render the users j2 file, and also send the renderer
        return render_template(
            "Users.j2", users=users, selected_user=selected_user
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# get incidents
@app.route("/Incidents", methods=["GET"])
def Incidents():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        query1 = "SELECT Incidents.incidentID as 'Incident ID', Incidents.timeOccurred as 'Time Occurred', Incidents.description as 'Description', Incidents.priority as Priority, Incidents.status as 'Status', Incidents.threatID as 'Threat ID' FROM Incidents;"
        incidents = db.query(dbConnection, query1).fetchall()
        
        # Query to get all incidents so we can display them in the dropdown
        query2 = "SELECT KnownThreats.threatID, KnownThreats.name FROM KnownThreats;"
        threats = db.query(dbConnection, query2).fetchall()

        # send the data to the update form if one is selected during an update attempt
        selected_incident = None
        incident_id = request.args.get("incident_id")
        if incident_id:
            query3 = "SELECT Incidents.incidentID as 'Incident ID', Incidents.timeOccurred as 'Time Occurred', Incidents.description as 'Description', Incidents.priority as Priority, Incidents.status as 'Status', Incidents.threatID as 'Threat ID' FROM Incidents WHERE Incidents.incidentID = %s;"
            selected_incident = db.query(dbConnection, query3, (incident_id,)).fetchone()

        # Render the incidents j2 file, and also send the renderer
        return render_template(
            "Incidents.j2", 
            incidents=incidents,
            threats=threats,
            selected_incident=selected_incident
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# get IncidentDevices
@app.route("/IncidentDevices", methods=["GET"])
def IncidentDevices():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        query1 = "SELECT IncidentDevices.incidentDevicesID as 'Incident Devices ID', IncidentDevices.incidentID as 'Incident ID', IncidentDevices.deviceID as 'Device ID' "\
        "FROM IncidentDevices;"

        incidentDevices = db.query(dbConnection, query1).fetchall()
        
        # Query to get all incidents so we can display them in the dropdown
        query2 = "SELECT Incidents.incidentID, Incidents.description " \
        "FROM Incidents;"
        incidents = db.query(dbConnection, query2).fetchall()

        # Query to get all devices so we can display them in the dropdown
        query3 = "SELECT Devices.deviceID, Devices.deviceName " \
        "FROM Devices " \
        "ORDER BY Devices.deviceID ASC;"
        devices = db.query(dbConnection, query3).fetchall()

        #Get join query to get all incidentDevices with device names and incident descriptions and threat names
        query4 = "SELECT IncidentDevices.incidentDevicesID, Incidents.description as 'Incident Description', Devices.deviceName as 'Device Name' " \
        "FROM IncidentDevices " \
        "JOIN Incidents ON IncidentDevices.incidentID = Incidents.incidentID " \
        "JOIN Devices ON IncidentDevices.deviceID = Devices.deviceID;"
        incDevInfo = db.query(dbConnection, query4).fetchall()

        # send the data to the update form if one is selected during an update attempt
        selected_incidentDevice = None
        incidentDevices_id = request.args.get("incidentDevices_id")
        if incidentDevices_id:
            query5 = "SELECT IncidentDevices.incidentDevicesID as 'Incident Devices ID', IncidentDevices.incidentID as 'Incident ID', IncidentDevices.deviceID as 'Device ID' FROM IncidentDevices WHERE IncidentDevices.incidentDevicesID = %s;"
            selected_incidentDevice = db.query(dbConnection, query5, (incidentDevices_id,)).fetchone()

        # Render the incidents j2 file, and also send the renderer
        return render_template(
            "IncidentDevices.j2", incidentDevices=incidentDevices,
            incidents=incidents,
            devices=devices,
            incDevInfo=incDevInfo,
            selected_incidentDevice=selected_incidentDevice
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# get responses
@app.route("/Responses", methods=["GET"])
def Responses():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        query1 = "SELECT Responses.responseID as 'Response ID', Responses.incidentID as 'Incident ID', Responses.userID as 'User ID', Responses.timeStarted as 'Time Started', Responses.timeEnded as 'Time Ended', Responses.actionPerformed as 'Action Performed', Responses.status as 'Status' "\
        "FROM Responses;"

        responses = db.query(dbConnection, query1).fetchall()
        
        # Query to get all users so we can display them in the dropdown
        query2 = "SELECT Users.userID, Users.firstName, Users.lastName " \
        "FROM Users;"
        users = db.query(dbConnection, query2).fetchall()

        # Query to get all incidents so we can display them in the dropdown
        query3 = "SELECT Incidents.incidentID, Incidents.description FROM Incidents;"
        incidents = db.query(dbConnection, query3).fetchall()

        # send the data to the update form if one is selected during an update attempt
        selected_response = None
        response_id = request.args.get("response_id")
        if response_id:
            query4 = "SELECT Responses.responseID as 'Response ID', Responses.incidentID as 'Incident ID', Responses.userID as 'User ID', Responses.timeStarted as 'Time Started', Responses.timeEnded as 'Time Ended', Responses.actionPerformed as 'Action Performed', Responses.status as 'Status' FROM Responses WHERE Responses.responseID = %s;"
            selected_response = db.query(dbConnection, query4, (response_id,)).fetchone()

        # Render the responses j2 file, and also send the renderer
        return render_template(
            "Responses.j2", 
            responses=responses,
            users=users,
            incidents=incidents,
            selected_response=selected_response
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# get devices
@app.route("/Devices", methods=["GET"])
def Devices():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        query1 = "SELECT Devices.deviceID as 'Device ID', Devices.deviceName as 'Device Name', Devices.IPAddress as 'IP Address', Devices.deviceType as 'Device Type', Devices.status as 'Status', Devices.assignedTo as 'Assigned To' " \
        "FROM Devices " \
        
        devices = db.query(dbConnection, query1).fetchall()

        # Query to get all users so we can display them in the dropdown
        query2 = "SELECT Users.userID, Users.firstName, Users.lastName " \
        "FROM Users;"
        users = db.query(dbConnection, query2).fetchall()

        # send the data to the update form if one is selected during an update attempt
        selected_device = None
        device_id = request.args.get("device_id")
        if device_id:
            query3 = "SELECT Devices.deviceID as 'Device ID', Devices.deviceName as 'Device Name', Devices.IPAddress as 'IP Address', Devices.deviceType as 'Device Type', Devices.status as 'Status', Devices.assignedTo as 'Assigned To' FROM Devices WHERE Devices.deviceID = %s;"
            selected_device = db.query(dbConnection, query3, (device_id,)).fetchone()

        # Render the devices j2 file, and also send the renderer
        return render_template(
            "Devices.j2", 
            devices=devices,
            users=users,
            selected_device=selected_device
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

@app.route("/DeviceServices", methods=["GET"])
def DeviceServices():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        query1 = "SELECT DeviceServices.deviceServiceID as 'Device Service ID', DeviceServices.deviceID as 'Device ID', DeviceServices.serviceID as 'Service ID' " \
        "FROM DeviceServices; "
        deviceServices = db.query(dbConnection, query1).fetchall()

        query2 = "SELECT deviceID, deviceName " \
        "FROM Devices " \
        "ORDER BY deviceID ASC; "
        devices = db.query(dbConnection, query2).fetchall()

        query3 = "SELECT serviceID, serviceName " \
        "FROM Services " \
        "ORDER BY serviceID ASC;"
        services = db.query(dbConnection, query3).fetchall()

        # send the data to the update form if one is selected during an update attempt
        selected_deviceService = None
        deviceService_id = request.args.get("deviceService_id")
        if deviceService_id:
            query4 = "SELECT DeviceServices.deviceServiceID as 'Device Service ID', DeviceServices.deviceID as 'Device ID', DeviceServices.serviceID as 'Service ID' FROM DeviceServices WHERE DeviceServices.deviceServiceID = %s;"
            selected_deviceService = db.query(dbConnection, query4, (deviceService_id,)).fetchone()

        # Render the deviceServices j2 file, and also send the renderer
        return render_template(
            "DeviceServices.j2", 
            deviceServices=deviceServices,
            devices=devices,
            services=services,
            selected_deviceService=selected_deviceService
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# get services
@app.route("/Services", methods=["GET"])
def Services():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        query1 = "SELECT Services.serviceID as 'Service ID', Services.serviceName as 'Service Name', Services.port as Port, Services.protocol as Protocol " \
        "FROM Services "
        services = db.query(dbConnection, query1).fetchall()

        # send the data to the update form if one is selected during an update attempt
        selected_service = None
        service_id = request.args.get("service_id")
        if service_id:
            query2 = "SELECT Services.serviceID as 'Service ID', Services.serviceName as 'Service Name', Services.port as Port, Services.protocol as Protocol FROM Services WHERE Services.serviceID = %s;"
            selected_service = db.query(dbConnection, query2, (service_id,)).fetchone()

        # Render the services j2 file, and also send the renderer
        return render_template(
            "Services.j2", 
            services=services,
            selected_service=selected_service
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# get knownThreats
@app.route("/KnownThreats", methods=["GET"])
def KnownThreats():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        query1 = "SELECT KnownThreats.threatID as 'Threat ID', KnownThreats.name as 'Name', KnownThreats.type as 'Type', KnownThreats.description as 'Description', KnownThreats.dateFirstSeen as 'Date First Seen', KnownThreats.dateLastSeen as 'Date Last Seen' " \
        "FROM KnownThreats " \
        
        knownThreats = db.query(dbConnection, query1).fetchall()

        # send the data to the update form if one is selected during an update attempt
        selected_knownThreat = None
        threat_id = request.args.get("threat_id")
        if threat_id:
            query2 = "SELECT KnownThreats.threatID as 'Threat ID', KnownThreats.name as 'Name', KnownThreats.type as 'Type', KnownThreats.description as 'Description', KnownThreats.dateFirstSeen as 'Date First Seen', KnownThreats.dateLastSeen as 'Date Last Seen' FROM KnownThreats WHERE KnownThreats.threatID = %s;"
            selected_knownThreat = db.query(dbConnection, query2, (threat_id,)).fetchone()

        # Render the knownThreats j2 file, and also send the renderer
        return render_template(
            "KnownThreats.j2", 
            knownThreats=knownThreats,
            selected_knownThreat=selected_knownThreat
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# Citation for the following routes:
# Date: 5/6/25
# Base code was for routes was adapted from Exploation - Implementing CUD Operations Into Your App
# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-implementing-cud-operations-in-your-app?module_item_id=25352968
# base code was augumented with some original code

# CREATE ROUTES START
@app.route("/Users/create", methods=["POST"])
def create_user():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor()

        # Get the form data
        firstName = request.form["create_user_firstName"]
        lastName = request.form["create_user_lastName"]
        email = request.form["create_user_email"]
        department = request.form["create_user_department"]
        role = request.form["create_user_role"]

        try:
            # Create and execute our queries
            query1 = "CALL sp_CreateUser(%s, %s, %s, %s, %s);"
            cursor.execute(query1, (firstName, lastName, email, department, role))

            # Commit the changes to the database
            dbConnection.commit()

        # Citation for the following code:
        # Date: 6/8/25
        # Copied from /OR/ Adapted from /OR/ Based on 
        # Adapted from the exploration code with additional error catching using flash - tutorial linked below
        # Source URL: https://www.tutorialspoint.com/flask/flask_message_flashing.htm
        # I needed to know how to generate a popup message on an error (duplicate unique fields), I have heard of flash before
        # so I researched from there and found this tutorial. The code is original + adapted from website
        except Exception as e:
            # duplicate email error
            flash("Error: A user with that email already exists.")
            return redirect("/Users")

        print(f"CREATE Users. Name: {firstName} {lastName}")

        # Redirect to the Users page
        return redirect("/Users")

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

@app.route("/Devices/create", methods=["POST"])
def create_device():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor()

        # Get the form data
        deviceName = request.form["create_device_name"]
        ipAddress = request.form["create_device_ipAddress"]
        deviceType = request.form["create_device_type"]
        status = request.form["create_device_status"]
        assignedTo = request.form["create_device_assignedTo"]

        
        try:
            # Create and execute our queries
            query1 = "CALL sp_CreateDevice(%s, %s, %s, %s, %s);"
            cursor.execute(query1, (deviceName, ipAddress, deviceType, status, assignedTo))

            # Commit the changes to the database
            dbConnection.commit()

        # Citation for the following code:
        # Date: 6/8/25
        # Copied from /OR/ Adapted from /OR/ Based on 
        # Adapted from the exploration code with additional error catching using flash - tutorial linked below
        # Source URL: https://www.tutorialspoint.com/flask/flask_message_flashing.htm
        # I needed to know how to generate a popup message on an error (duplicate unique fields), I have heard of flash before
        # so I researched from there and found this tutorial. The code is original + adapted from website
        except Exception as e:
            # duplicate device name and/or IP address error
            flash("Error: A device with that name and/or IP address already exists.")

        print(f"CREATE Devices. Name: {deviceName}")

        # Redirect to the Devices page
        return redirect("/Devices")

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()


@app.route("/Incidents/create", methods=["POST"])
def create_incident():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor()

        # Get the form data
        timeOccurred = request.form["create_incident_timeOccurred"]
        description = request.form["create_incident_description"]
        priority = request.form["create_incident_priority"]
        status = request.form["create_incident_status"]
        threatID = request.form["create_incident_threatID"]

        # Create and execute our queries
        query1 = "CALL sp_CreateIncident(%s, %s, %s, %s, %s);"
        cursor.execute(query1, (timeOccurred, description, priority, status, threatID))

        # Commit the changes to the database
        dbConnection.commit()

        print(f"CREATE Incidents. Description: {description}")

        # Redirect to the Incidents page
        return redirect("/Incidents")

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()


@app.route("/IncidentDevices/create", methods=["POST"])
def create_incidentDevice():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor()

        # Get the form data
        incidentID = request.form["create_incident_id"]
        deviceID = request.form["create_device_id"]

        # Create and execute our queries
        query1 = "CALL sp_CreateIncidentDevice(%s, %s);"
        cursor.execute(query1, (incidentID, deviceID))

        # Commit the changes to the database
        dbConnection.commit()

        print(f"CREATE IncidentDevices. Incident ID: {incidentID}, Device ID: {deviceID}")

        # Redirect to the IncidentDevices page
        return redirect("/IncidentDevices")

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

@app.route("/Responses/create", methods=["POST"])
def create_response():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor()

        # Get the form data
        incidentID = request.form["create_response_incidentID"]
        userID = request.form["create_response_userID"]
        timeStarted = request.form["create_response_timeStarted"]
        timeEnded = request.form["create_response_timeEnded"]
        actionPerformed = request.form["create_response_actionPerformed"]
        status = request.form["create_response_status"]
        
        # Create and execute our queries
        query1 = "CALL sp_CreateResponse(%s, %s, %s, %s, %s, %s);"
        cursor.execute(query1, (incidentID, userID, timeStarted, timeEnded, actionPerformed, status))

        # Commit the changes to the database
        dbConnection.commit()

        print(f"CREATE Responses. Incident ID: {incidentID}, User ID: {userID}")

        # Redirect to the Responses page
        return redirect("/Responses")

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

@app.route("/DeviceServices/create", methods=["POST"])
def create_deviceService():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor()

        # Get the form data
        deviceID = request.form["create_deviceService_device"]
        serviceID = request.form["create_deviceService_service"]

        # Create and execute our queries
        query1 = "CALL sp_CreateDeviceService(%s, %s);"
        cursor.execute(query1, (deviceID, serviceID))

        # Commit the changes to the database
        dbConnection.commit()

        print(f"CREATE DeviceServices. Device ID: {deviceID}, Service ID: {serviceID}")

        # Redirect to the DeviceServices page
        return redirect("/DeviceServices")

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

@app.route("/Services/create", methods=["POST"])
def create_service():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor()

        # Get the form data
        serviceName = request.form["create_service_name"]
        port = request.form["create_service_port"]
        protocol = request.form["create_service_protocol"]

        try:
            # Create and execute our queries
            query1 = "CALL sp_CreateService(%s, %s, %s);"
            cursor.execute(query1, (serviceName, port, protocol))

            # Commit the changes to the database
            dbConnection.commit()
        # Citation for the following code:
        # Date: 6/8/25
        # Copied from /OR/ Adapted from /OR/ Based on 
        # Adapted from the exploration code with additional error catching using flash - tutorial linked below
        # Source URL: https://www.tutorialspoint.com/flask/flask_message_flashing.htm
        # I needed to know how to generate a popup message on an error (duplicate unique fields), I have heard of flash before
        # so I researched from there and found this tutorial. The code is original + adapted from website
        except Exception as e:
            # duplicate service name error
            flash("Error: A service with that name already exists.")
            return redirect("/Services")

        print(f"CREATE Services. Name: {serviceName}")

        # Redirect to the Services page
        return redirect("/Services")

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

@app.route("/KnownThreats/create", methods=["POST"])
def create_knownThreat():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor()

        # Get the form data
        name = request.form["create_knownThreat_name"]
        threatType = request.form["create_knownThreat_type"]
        description = request.form["create_knownThreat_description"]
        dateFirstSeen = request.form["create_knownThreat_dateFirstSeen"]
        dateLastSeen = request.form["create_knownThreat_dateLastSeen"]

        # Create and execute our queries
        query1 = "CALL sp_CreateKnownThreat(%s, %s, %s, %s, %s);"
        cursor.execute(query1, (name, threatType, description, dateFirstSeen, dateLastSeen))

        # Commit the changes to the database
        dbConnection.commit()

        print(f"CREATE KnownThreats. Name: {name}")

        # Redirect to the KnownThreats page
        return redirect("/KnownThreats")

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()


# CREATE ROUTES END





# Citation for the following routes:
# Date: 5/6/25
# Base code was for routes was adapted from Exploation - Implementing CUD Operations Into Your App
# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-implementing-cud-operations-in-your-app?module_item_id=25352968
# base code was augumented with some original code

# DELETE ROUTES START
@app.route("/Users/delete", methods=["POST"])
def delete_user():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor()

        # Get the userID from the form
        userID = request.form["delete_user_id"]
        userName = request.form["delete_user_name"]

        # Create and execute our queries
        query1 = "CALL sp_DeleteUser(%s);"
        cursor.execute(query1, (userID,))

        # Commit the changes to the database
        dbConnection.commit()

        print(f"DELETE Users. ID: {userID} Name: {userName}")

        # Redirect to the Users page
        return redirect("/Users")

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

@app.route("/Incidents/delete", methods=["POST"])
def delete_incident():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor()

        # Get the incidentID from the form
        incidentID = request.form["delete_incident_id"]

        # Create and execute our queries
        query1 = "CALL sp_DeleteIncident(%s);"
        cursor.execute(query1, (incidentID,))

        # Commit the changes to the database
        dbConnection.commit()

        print(f"DELETE Incidents. ID: {incidentID}")

        # Redirect to the Users page
        return redirect("/Incidents")

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

@app.route("/IncidentDevices/delete", methods=["POST"])
def delete_incidentDevice():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor()

        # Get the incidentID from the form
        incidentDeviceID = request.form["delete_incidentDevice_id"]

        # Create and execute our queries
        query1 = "CALL sp_DeleteIncidentDevice(%s);"
        cursor.execute(query1, (incidentDeviceID,))

        # Commit the changes to the database
        dbConnection.commit()

        print(f"DELETE IncidentDevice ID: {incidentDeviceID}")

        # Redirect to the Users page
        return redirect("/IncidentDevices")

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

@app.route("/Responses/delete", methods=["POST"])
def delete_response():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor()

        # Get the incidentID from the form
        responseID = request.form["delete_response_id"]

        # Create and execute our queries
        query1 = "CALL sp_DeleteResponse(%s);"
        cursor.execute(query1, (responseID,))

        # Commit the changes to the database
        dbConnection.commit()

        print(f"DELETE Responses. ID: {responseID}")

        # Redirect to the Users page
        return redirect("/Responses")

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

@app.route("/Devices/delete", methods=["POST"])
def delete_device():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor()

        # Get the incidentID from the form
        deviceID = request.form["delete_device_id"]

        # Create and execute our queries
        query1 = "CALL sp_DeleteDevice(%s);"
        cursor.execute(query1, (deviceID,))

        # Commit the changes to the database
        dbConnection.commit()

        print(f"DELETE Devices. ID: {deviceID}")

        # Redirect to the Users page
        return redirect("/Devices")

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

@app.route("/DeviceServices/delete", methods=["POST"])
def delete_deviceService():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor()

        # Get the incidentID from the form
        deviceServiceID = request.form["delete_deviceService_id"]

        # Create and execute our queries
        query1 = "CALL sp_DeleteDeviceService(%s);"
        cursor.execute(query1, (deviceServiceID,))

        # Commit the changes to the database
        dbConnection.commit()

        print(f"DELETE DeviceServices. DeviceService ID: {deviceServiceID}")
        # Redirect to the Users page
        return redirect("/DeviceServices")

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

@app.route("/Services/delete", methods=["POST"])
def delete_service():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor()

        # Get the incidentID from the form
        serviceID = request.form["delete_service_id"]

        # Create and execute our queries
        query1 = "CALL sp_DeleteService(%s);"
        cursor.execute(query1, (serviceID,))

        # Commit the changes to the database
        dbConnection.commit()

        print(f"DELETE Services. ID: {serviceID}")

        # Redirect to the Users page
        return redirect("/Services")

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

@app.route("/KnownThreats/delete", methods=["POST"])
def delete_knownThreat():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor()

        # Get the incidentID from the form
        threatID = request.form["delete_knownThreat_id"]
        threatName = request.form["delete_knownThreat_name"]

        # Create and execute our queries
        query1 = "CALL sp_DeleteKnownThreat(%s);"
        cursor.execute(query1, (threatID,))

        # Commit the changes to the database
        dbConnection.commit()

        print(f"DELETE KnownThreats. ID: {threatID}")

        # Redirect to the Users page
        return redirect("/KnownThreats")

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# DELETE ROUTES END


# Citation for the following routes:
# Date: 5/6/25
# Base code was for routes was adapted from Exploation - Implementing CUD Operations Into Your App
# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-implementing-cud-operations-in-your-app?module_item_id=25352968
# base code was augumented with some original code
# UPDATE ROUTES START

# update users
@app.route("/Users/update", methods=["POST"])
def update_users():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor() 

        # get the form data
        userID = request.form["update_user_id"]

        # queries
        try:
            query1 = "CALL sp_UpdateUser(%s, %s, %s, %s, %s, %s);"
            cursor.execute(
                query1,
                (
                    userID,
                    request.form["update_user_firstName"],
                    request.form["update_user_lastName"],
                    request.form["update_user_email"],
                    request.form["update_user_department"],
                    request.form["update_user_role"]
                )
            )

            dbConnection.commit()  # commit the changes

        # Citation for the following code:
        # Date: 6/8/25
        # Copied from /OR/ Adapted from /OR/ Based on 
        # Adapted from the exploration code with additional error catching using flash - tutorial linked below
        # Source URL: https://www.tutorialspoint.com/flask/flask_message_flashing.htm
        # I needed to know how to generate a popup message on an error (duplicate unique fields), I have heard of flash before
        # so I researched from there and found this tutorial. The code is original + adapted from website
        except Exception as e:
            # duplicate email error
            flash("Error: A user with that email already exists.")
            return redirect("/Users")

        #redirect to the Users page
        return redirect("/Users")
    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500
    finally:
        # Close the DB connection
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# update incidents
@app.route("/Incidents/update", methods=["POST"])
def update_incidents():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor() 

        # get the form data
        incidentID = request.form["update_incident_id"]

        # queries
        query1 = "CALL sp_UpdateIncident(%s, %s, %s, %s, %s, %s);"
        cursor.execute(
            query1,
            (
                incidentID,
                request.form["update_incident_timeOccurred"],
                request.form["update_incident_description"],
                request.form["update_incident_priority"],
                request.form["update_incident_status"],
                request.form["update_incident_threatID"]
            )
        )

        dbConnection.commit()  # commit the changes

        #redirect to the Incidents page
        return redirect("/Incidents")
    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500
    finally:
        # Close the DB connection
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# update incidentDevices
@app.route("/IncidentDevices/update", methods=["POST"])
def update_incidentDevices():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor() 

        # get the form data
        incidentDeviceID = request.form["update_incidentDevices_id"]
        incidentID = request.form["update_incident_id"]
        deviceID = request.form["update_device_id"]

        # queries
        query1 = "CALL sp_UpdateIncidentDevice(%s, %s, %s);"
        cursor.execute(
            query1,
            (
                incidentDeviceID,
                incidentID,
                deviceID
            )
        )

        dbConnection.commit()  # commit the changes

        #redirect to the IncidentDevices page
        return redirect("/IncidentDevices")
    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500
    finally:
        # Close the DB connection
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# update responses
@app.route("/Responses/update", methods=["POST"])
def update_responses():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor() 

        # get the form data
        responseID = request.form["update_responseID"]

        # queries
        query1 = "CALL sp_UpdateResponse(%s, %s, %s, %s, %s);"
        cursor.execute(
            query1,
            (
                responseID,
                request.form["update_timeStarted"],
                request.form["update_timeEnded"],
                request.form["update_actionPerformed"],
                request.form["update_status"]
            )
        )

        dbConnection.commit()  # commit the changes

        #redirect to the Responses page
        return redirect("/Responses")
    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500
    finally:
        # Close the DB connection
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# update devices
@app.route("/Devices/update", methods=["POST"])
def update_devices():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor() 

        # get the form data
        deviceID = request.form["update_device_id"]

        try:
            # queries
            query1 = "CALL sp_UpdateDevice(%s, %s, %s, %s, %s, %s);"
            cursor.execute(
                query1,
                (
                    deviceID,
                    request.form["update_device_name"],
                    request.form["update_device_ipAddress"],
                    request.form["update_device_type"],
                    request.form["update_device_status"],
                    request.form["update_device_assignedTo"]
                )
            )

            dbConnection.commit()  # commit the changes
            
        # Citation for the following code:
        # Date: 6/8/25
        # Copied from /OR/ Adapted from /OR/ Based on 
        # Adapted from the exploration code with additional error catching using flash - tutorial linked below
        # Source URL: https://www.tutorialspoint.com/flask/flask_message_flashing.htm
        # I needed to know how to generate a popup message on an error (duplicate unique fields), I have heard of flash before
        # so I researched from there and found this tutorial. The code is original + adapted from website
        except Exception as e:
            # duplicate device name and/or IP address error
            flash("Error: A device with that name and/or IP address already exists.")
            return redirect("/Devices")

        #redirect to the Devices page
        return redirect("/Devices")
    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500
    finally:
        # Close the DB connection
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# update deviceServices
@app.route("/DeviceServices/update", methods=["POST"])
def update_deviceServices():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor() 

        # get the form data
        deviceServiceID = request.form["update_deviceService_id"]
        

        # queries
        query1 = "CALL sp_UpdateDeviceService(%s, %s, %s);"
        cursor.execute(
            query1,
            (
                deviceServiceID,
                request.form["update_deviceService_device"],
                request.form["update_deviceService_service"]
            )
        )

        dbConnection.commit()  # commit the changes

        #redirect to the DeviceServices page
        return redirect("/DeviceServices")
    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500
    finally:
        # Close the DB connection
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# update services
@app.route("/Services/update", methods=["POST"])
def update_services():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor() 

        # get the form data
        serviceID = request.form["update_service_id"]

        # queries
        try:
            query1 = "CALL sp_UpdateService(%s, %s, %s, %s);"
            cursor.execute(
                query1,
                (
                    serviceID,
                    request.form["update_service_name"],
                    request.form["update_service_port"],
                    request.form["update_service_protocol"]
                )
            )

            dbConnection.commit()  # commit the changes
        # Citation for the following code:
        # Date: 6/8/25
        # Copied from /OR/ Adapted from /OR/ Based on 
        # Adapted from the exploration code with additional error catching using flash - tutorial linked below
        # Source URL: https://www.tutorialspoint.com/flask/flask_message_flashing.htm
        # I needed to know how to generate a popup message on an error (duplicate unique fields), I have heard of flash before
        # so I researched from there and found this tutorial. The code is original + adapted from website
        except Exception as e:
            # duplicate service name error
            flash("Error: A service with that name already exists.")
            return redirect("/Services")

        #redirect to the Services page
        return redirect("/Services")
    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500
    finally:
        # Close the DB connection
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# update knownThreats
@app.route("/KnownThreats/update", methods=["POST"])
def update_knownThreats():
    try:
        dbConnection = db.connectDB()  # Open our database connection
        cursor = dbConnection.cursor() 

        # get the form data
        threatID = request.form["update_knownThreat_id"]

        # queries
        query1 = "CALL sp_UpdateKnownThreat(%s, %s, %s, %s, %s, %s);"
        cursor.execute(
            query1,
            (
                threatID,
                request.form["update_knownThreat_name"],
                request.form["update_knownThreat_type"],
                request.form["update_knownThreat_description"],
                request.form["update_knownThreat_dateFirstSeen"],
                request.form["update_knownThreat_dateLastSeen"]
            )
        )

        dbConnection.commit()  # commit the changes

        #redirect to the KnownThreats page
        return redirect("/KnownThreats")
    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500
    finally:
        # Close the DB connection
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# ########################################
# ########## LISTENER

if __name__ == "__main__":
    app.run(
        port=PORT, debug=True
    )  # debug is an optional parameter. Behaves like nodemon in Node.
