# Citation for the following function:
# Date: 5/6/25
# Adapted from Exploation - Web Application Technology
# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-web-application-technology-2?module_item_id=25352948


# ########################################
# ########## SETUP

from flask import Flask, render_template, request, redirect
import database.db_connector as db

PORT = 50124

app = Flask(__name__)

# ########################################
# ########## ROUTE HANDLERS

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
        query1 = "SELECT Users.userID, Users.firstName, Users.lastName, Users.email, Users.department, Users.role " \
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
        query1 = "SELECT Incidents.incidentID, Incidents.timeOccurred, Incidents.description, Incidents.priority, Incidents.status, Incidents.threatID " \
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
        query1 = "SELECT IncidentDevices.incidentDevicesID, IncidentDevices.incidentID, IncidentDevices.deviceID "\
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
        query1 = "SELECT Responses.responseID, Responses.incidentID, Responses.userID, Responses.timeStarted, Responses.timeEnded, Responses.actionPerformed, Responses.status "\
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
        query1 = "SELECT * " \
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
        query1 = "SELECT * " \
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
        query1 = "SELECT * " \
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
        query1 = "SELECT * " \
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