_Disclaimer: This project originated as a collaboration with [Dawson Herrington](https://github.com/dawson-herrington) for Oregon State University's CS340 (Spring 2025) Class Project. This version includes my personal UI layout, CRUD logic, and post-submission improvements._

# Cybersecurity Incident Tracker Dashboard
All code is based originally (then modified) on the CS340 starter code except:
- The specifics of our procedures in PL.SQL
- style.css (original + based on documentation - cited in code and below)
- Inline styling in the templates
- Specific pre-population functionality on updates in templates
- Duplicate error handling in app.py
- flash message implementation in templates
- warnings on a delete operation
 - additional get routes to fascilitate update pre population

I would like to specifically highlight a tutorial I found useful for flashing messages in flask,
the implementation is cited in-line.
https://www.tutorialspoint.com/flask/flask_message_flashing.htm
I would reccomend this to future students.

I would also like to draw attention to the extensive work on the update code in each template. Extensive code both original and assisted (cited where appropriate) went into 
getting a second route set up to prepopulate data and in styling it, then merging those changes together.

## Project Overview

This is a full-stack web dashboard designed to track cybersecurity incidents, associated devices, services, and response actions across an organization. Users can log incidents, assign devices and responders, and maintain service records — all through a clean and accessible interface.

The goal of this project was to:

- Practice relational database design (MySQL)
- Build a backend using Flask (Python)
- Design a user-friendly frontend with HTML, CSS, and Jinja
- Implement robust CRUD (Create, Read, Update, Delete) operations.
- Collaborate using Git and GitHub workflows

## Technologies Used
- Frontend: HTML5, CSS(Tailwind), Jinja
- Backend: Flask
- Database: MySQL
- Version Control: Git + GitHub

## Database Schema
The system includes the following core tables:
- **Users**: Admins or responders who can be assigned to incidents
- **Devices**: Machines involved in or affected by cybersecurity threats
- **Services**: Networked services running on those devices
- **Incidents**: Security events recorded by the team
- **Responses**: Many-to-Many relationship between Users and Incidents, used for tracking response actions
- **KnownThreats**: Catalog of threat signatures or profiles

## Key Features
- Add, update, and delete Users, Devices, Services, and Incidents
- Assign Devices to Incidents, and Users to Responses
- Use stored procedures for all backend insert/update operations
- Flash messages for user feedback
- UI layout optimized for clarity and CRUD functionality
- Error handling for duplicate fields and relational constraints

## UI Design Highlights
- Clean, professional layout that mimics production admin dashboards
- Logical grouping of create/update forms side-by-side
- Responsive dropdowns for selecting entities to update
- Consistent typography and form design
- Ready for further responsiveness and modal integration (in-progress)

## My Post-Submission Improvements
- Clean separation of create vs. update logic using dual form submission
- Improved table layout for readability
- Enhanced delete button accessibility
- Planned work: responsive layout, reusable modal forms, button redesign

## Running Locally
_Note: This project was originally deployed to a MariaDB database provided by OSU. You will need to configure your own database to run this app._

    # Clone the repo  
    git clone https://github.com/dcross17/cybersec-db-dashboard.git  
    cd cybersec-db-dashboard  

    # (Optional) create a virtual environment
    python3 -m venv venv  
    source venv/bin/activate`

    # Install dependencies
    pip install -r requirements.txt

    # Set up environment variables and DB connection
    # (See db_connector.py for reference)

    # Run the app
    python app.py

## Credits
- UI/UX, final CRUD logic, and post-submission polish by @dcross17
- Original database design and backend structure in collaboration with [Dawson Herrington](https://github.com/dawson-herrington)