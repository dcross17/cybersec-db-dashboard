# Citation for the following function:
# Date: 5/6/25
# Adapted from Exploation - Web Application Technology
# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-web-application-technology-2?module_item_id=25352948


# ########################################
# ########## SETUP

from flask import Flask, render_template, request, redirect
import database.db_connector as db

PORT = 50122

app = Flask(__name__)

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
        query1 = "SELECT Users.userID as 'User ID', Users.firstName as 'First Name', Users.lastName as 'Last Name', Users.email as Email, Users.department as Department, Users.role as 'Role' " \
        "FROM Users;"
        users = db.query(dbConnection, query1).fetchall()
        

        # Render the users j2 file, and also send the renderer
        return render_template(
            "Users.j2", users=users
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
        query1 = "SELECT Incidents.incidentID as 'Incident ID', Incidents.timeOccurred as 'Time Occurred', Incidents.description as 'Description', Incidents.priority as Priority, Incidents.status as 'Status', Incidents.threatID as 'Threat ID' " \
        "FROM Incidents;"

        incidents = db.query(dbConnection, query1).fetchall()
        
        # Query to get all incidents so we can display them in the dropdown
        query2 = "SELECT KnownThreats.threatID, KnownThreats.name " \
        "FROM KnownThreats;"
        threats = db.query(dbConnection, query2).fetchall()

        # Render the incidents j2 file, and also send the renderer
        return render_template(
            "Incidents.j2", incidents=incidents,
            threats=threats
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
        query2 = "SELECT Incidents.incidentID " \
        "FROM Incidents;"
        incidents = db.query(dbConnection, query2).fetchall()

        # Query to get all devices so we can display them in the dropdown
        query3 = "SELECT Devices.deviceID, Devices.deviceName " \
        "FROM Devices " \
        "ORDER BY Devices.deviceID ASC;"
        devices = db.query(dbConnection, query3).fetchall()

        # Render the incidents j2 file, and also send the renderer
        return render_template(
            "IncidentDevices.j2", incidentDevices=incidentDevices,
            incidents=incidents,
            devices=devices
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
        

        # Render the incidents j2 file, and also send the renderer
        return render_template(
            "Responses.j2", responses=responses
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


        # Render the users j2 file, and also send the renderer
        return render_template(
            "Devices.j2", 
            devices=devices,
            users=users
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

# get deviceServices
@app.route("/DeviceServices", methods=["GET"])
def DeviceServices():
    try:
        dbConnection = db.connectDB()  # Open our database connection

        # Create and execute our queries
        query1 = "SELECT DeviceServices.deviceServiceID as 'Device Service ID', DeviceServices.deviceID as 'Device ID', DeviceServices.serviceID as 'Service ID' " \
        "FROM DeviceServices; " \
        
        deviceServices = db.query(dbConnection, query1).fetchall()

        query2 = "SELECT deviceID, deviceName " \
        "FROM Devices " \
        "ORDER BY deviceID ASC; " \

        devices = db.query(dbConnection, query2).fetchall()

        query3 = "SELECT serviceID, serviceName " \
        "FROM Services " \
        "ORDER BY serviceID ASC;" \

        services = db.query(dbConnection, query3).fetchall()

        # Render the users j2 file, and also send the renderer
        return render_template(
            "DeviceServices.j2", 
            deviceServices=deviceServices,
            devices=devices,
            services=services
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
        "FROM Services " \
        
        services = db.query(dbConnection, query1).fetchall()

        # Render the users j2 file, and also send the renderer
        return render_template(
            "Services.j2", 
            services=services,
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

        # Render the users j2 file, and also send the renderer
        return render_template(
            "KnownThreats.j2", 
            knownThreats=knownThreats,
        )

    except Exception as e:
        print(f"Error executing queries: {e}")
        return "An error occurred while executing the database queries.", 500

    finally:
        # Close the DB connection, if it exists
        if "dbConnection" in locals() and dbConnection:
            dbConnection.close()

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

        print(f"DELETE DeviceServices. ID: {deviceServiceID}")

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

# ########################################
# ########## LISTENER

if __name__ == "__main__":
    app.run(
        port=PORT, debug=True
    )  # debug is an optional parameter. Behaves like nodemon in Node.