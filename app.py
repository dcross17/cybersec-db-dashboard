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
        

        # Render the incidents j2 file, and also send the renderer
        return render_template(
            "Incidents.j2", incidents=incidents
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
        

        # Render the incidents j2 file, and also send the renderer
        return render_template(
            "IncidentDevices.j2", incidentDevices=incidentDevices
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
        "FROM Devices; " \

        devices = db.query(dbConnection, query2).fetchall()

        query3 = "SELECT serviceID, serviceName " \
        "FROM Services; " \

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



# ########################################
# ########## LISTENER

if __name__ == "__main__":
    app.run(
        port=PORT, debug=True
    )  # debug is an optional parameter. Behaves like nodemon in Node.