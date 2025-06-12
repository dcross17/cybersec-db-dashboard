This project originated as a collaboration with [Dawson Herrington](https://github.com/dawson-herrington) for Oregon State University's CS340 (Spring 2025). This version includes my personal UI layout, CRUD logic, and post-submission improvements.

# CS340-Project
All code is based originally (then modified) on the CS340 starter code except:
- The specifics of our procedures in PL.SQL
- style.CSS (original + based on documentation - cited in code and below)
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

---------- File Specific Citations ----------
*also present in files*
*explanation follows each citation*

---------- db_connector.py ----------

# Citation for the following code:
# Date: 5/6/25
# Copied from Exploation - Web Application Technology
# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-web-application-technology-2?module_item_id=25352948
(top-level, concerning the entire file)

---------- PL.SQL ----------
-- Citation for the following sql code:
-- Date: 6/9/25
-- Modified from the base code provided in the PL/SQL Exploration
-- Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-pl-slash-sql-part-1-sp-view-and-function?module_item_id=25352958
(top-level, concerning entire file)

---------- style.css ----------
/*citations*/
/*Citation for the basis of the CSS:*/
/*Date: 5/9/25*/
/*Adapted and modified from Tailwinds css tool*/
/*Source URL: https://tailwindcss.com/*/
(top-level, concerning basis for CSS)

/*Citation for Icons*/
/*Date: 5/9/25*/
/*Icons from below website*/
/*Source URL: https://heroicons.com/*/
(top-level, concern origins of graphic art serving as icons on the page)

---------- Devices.j2 ----------
{# Citation for the following code: #}
{# Date: 5/6/25 #}
{# Adapted from Exploation _ Web Application Technology #}
{# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration_web_application_technology_2?module_item_id=25352948#}
(top-level, concerning entire file)

{# Citation for the following code: #}
{# Date: 6/8/25 #}
{# Copied from /OR/ Adapted from /OR/ Based on #}
{# Adapted from the exploration code with additional error catching using flash - tutorial linked below #}
{# Source URL: https://www.tutorialspoint.com/flask/flask_message_flashing.htm }
{# I needed to know how to generate a popup message on an error (duplicate unique fields), I have heard of flash before #}
{# so I researched from there and found this tutorial. The code is original + adapted from website #}
{# duplicate popup #}
(in-line, concerning flashing implementation)

{# Citation for the following code: #}
{# Date: 6/2/25 #}
{# Copied from /OR/ Adapted from /OR/ Based on #}
{# Copilot helped me solve a hunch, details below. #}
{# Source URL: www.m365.cloud.microsoft #}
{# If AI tools were used: #}
{# I realized that an empty list would result in an index error but was unsure on how to fix it/embed the proper logic. #}
{# Prompt: When keying into a list as seen in code: ***Removed for brevity, see below*, how can I use a conditional #}
{# To handle a potentially empty data set. After some refinements we arrived at the solution you see below, which is only #}
{# slighty modified from the original code #}
(in-line, concerning AI assistance in debugging an index error in our READ table)

{# Citation for the following code: #}
{# Date: 6/8/25 #}
{# Copied from /OR/ Adapted from /OR/ Based on #}
{# Starter Code + Copilot assisted in some of the embedded preopulation logic, details below. #}
{# Source URL: www.m365.cloud.microsoft #}
{# If AI tools were used: #}
{# The original Update forms were based on the Flask starter code provided in the explorations. #}
{# To enable pre-population functionality, I added code to the get routes in the app.py file but was struggling#}
{# to have the changes populate in the form after severl attempts. I gave copilot the following initial prompt: #}
{# "How can one populate the update fields upon selection of an object from the dropdown with the following route: *inserted app.py get route*.#}
{# "I beleive I am close but cannot locate my errors" After some refinement prompts and slight tweaking I arrived at the solution you see below.#}
(in-line, concerning AI assistance for getting prepopulation of update up and running)

---------- DeviceServices.j2 ----------
{# Citation for the following code: #}
{# Date: 5/6/25 #}
{# Adapted from Exploation _ Web Application Technology #}
{# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration_web_application_technology_2?module_item_id=25352948#}
(top-level, concerning entire file)

{# Citation for the following code: #}
{# Date: 6/2/25 #}
{# Copied from /OR/ Adapted from /OR/ Based on #}
{# Copilot helped me solve a hunch, details below. #}
{# Source URL: www.m365.cloud.microsoft #}
{# If AI tools were used: #}
{# I realized that an empty list would result in an index error but was unsure on how to fix it/embed the proper logic. #}
{# Prompt: When keying into a list as seen in code: ***Removed for brevity, see below*, how can I use a conditional #}
{# To handle a potentially empty data set. After some refinements we arrived at the solution you see below, which is only #}
{# slighty modified from the original code #}
(in-line, concerning AI assistance in debugging an index error in our READ table)

{# Citation for the following code: #}
{# Date: 6/8/25 #}
{# Copied from /OR/ Adapted from /OR/ Based on #}
{# Starter Code + Copilot assisted in some of the embedded preopulation logic, details below. #}
{# Source URL: www.m365.cloud.microsoft #}
{# If AI tools were used: #}
{# The original Update forms were based on the Flask starter code provided in the explorations. #}
{# To enable pre-population functionality, I added code to the get routes in the app.py file but was struggling#}
{# to have the changes populate in the form after severl attempts. I gave copilot the following initial prompt: #}
{# "How can one populate the update fields upon selection of an object from the dropdown with the following route: *inserted app.py get route*.#}
{# "I beleive I am close but cannot locate my errors" After some refinement prompts and slight tweaking I arrived at the solution you see below.#}
(in-line, concerning AI assistance for getting prepopulation of update up and running)

---------- home.j2 ----------
{# Citation for the following code: #}
{# Date: 5/6/25 #}
{# Adapted from Exploation _ Web Application Technology #}
{# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration_web_application_technology_2?module_item_id=25352948#}
(top-level, concerning entire file)

---------- IncidentDevices.j2 ----------
{# Citation for the following code: #}
{# Date: 5/6/25 #}
{# Adapted from Exploation _ Web Application Technology #}
{# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration_web_application_technology_2?module_item_id=25352948#}
(top-level, concerning entire file)

{# Citation for the following code: #}
{# Date: 6/2/25 #}
{# Copied from /OR/ Adapted from /OR/ Based on #}
{# Copilot helped me solve a hunch, details below. #}
{# Source URL: www.m365.cloud.microsoft #}
{# If AI tools were used: #}
{# I realized that an empty list would result in an index error but was unsure on how to fix it/embed the proper logic. #}
{# Prompt: When keying into a list as seen in code: ***Removed for brevity, see below*, how can I use a conditional #}
{# To handle a potentially empty data set. After some refinements we arrived at the solution you see below, which is only #}
{# slighty modified from the original code #}
(in-line, concerning AI assistance in debugging an index error in our READ table)

{# Citation for the following code: #}
{# Date: 6/8/25 #}
{# Copied from /OR/ Adapted from /OR/ Based on #}
{# Starter Code + Copilot assisted in some of the embedded preopulation logic, details below. #}
{# Source URL: www.m365.cloud.microsoft #}
{# If AI tools were used: #}
{# The original Update forms were based on the Flask starter code provided in the explorations. #}
{# To enable pre-population functionality, I added code to the get routes in the app.py file but was struggling#}
{# to have the changes populate in the form after severl attempts. I gave copilot the following initial prompt: #}
{# "How can one populate the update fields upon selection of an object from the dropdown with the following route: *inserted app.py get route*.#}
{# "I beleive I am close but cannot locate my errors" After some refinement prompts and slight tweaking I arrived at the solution you see below.#}
(in-line, concerning AI assistance for getting prepopulation of update up and running)

---------- Incidents.j2 ----------
{# Citation for the following code: #}
{# Date: 5/6/25 #}
{# Adapted from Exploation _ Web Application Technology #}
{# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration_web_application_technology_2?module_item_id=25352948#}
(top-level, concerning entire file)

{# Citation for the following code: #}
{# Date: 6/2/25 #}
{# Copied from /OR/ Adapted from /OR/ Based on #}
{# Copilot helped me solve a hunch, details below. #}
{# Source URL: www.m365.cloud.microsoft #}
{# If AI tools were used: #}
{# I realized that an empty list would result in an index error but was unsure on how to fix it/embed the proper logic. #}
{# Prompt: When keying into a list as seen in code: ***Removed for brevity, see below*, how can I use a conditional #}
{# To handle a potentially empty data set. After some refinements we arrived at the solution you see below, which is only #}
{# slighty modified from the original code #}
(in-line, concerning AI assistance in debugging an index error in our READ table)

{# Citation for the following code: #}
{# Date: 6/8/25 #}
{# Copied from /OR/ Adapted from /OR/ Based on #}
{# Starter Code + Copilot assisted in some of the embedded preopulation logic, details below. #}
{# Source URL: www.m365.cloud.microsoft #}
{# If AI tools were used: #}
{# The original Update forms were based on the Flask starter code provided in the explorations. #}
{# To enable pre-population functionality, I added code to the get routes in the app.py file but was struggling#}
{# to have the changes populate in the form after severl attempts. I gave copilot the following initial prompt: #}
{# "How can one populate the update fields upon selection of an object from the dropdown with the following route: *inserted app.py get route*.#}
{# "I beleive I am close but cannot locate my errors" After some refinement prompts and slight tweaking I arrived at the solution you see below.#}
(in-line, concerning AI assistance for getting prepopulation of update up and running)

---------- KnownThreats.j2 ----------
{# Citation for the following code: #}
{# Date: 5/6/25 #}
{# Adapted from Exploation _ Web Application Technology #}
{# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration_web_application_technology_2?module_item_id=25352948#}
(top-level, concerning entire file)

{# Citation for the following code: #}
{# Date: 6/2/25 #}
{# Copied from /OR/ Adapted from /OR/ Based on #}
{# Copilot helped me solve a hunch, details below. #}
{# Source URL: www.m365.cloud.microsoft #}
{# If AI tools were used: #}
{# I realized that an empty list would result in an index error but was unsure on how to fix it/embed the proper logic. #}
{# Prompt: When keying into a list as seen in code: ***Removed for brevity, see below*, how can I use a conditional #}
{# To handle a potentially empty data set. After some refinements we arrived at the solution you see below, which is only #}
{# slighty modified from the original code #}
(in-line, concerning AI assistance in debugging an index error in our READ table)

{# Citation for the following code: #}
{# Date: 6/8/25 #}
{# Copied from /OR/ Adapted from /OR/ Based on #}
{# Starter Code + Copilot assisted in some of the embedded preopulation logic, details below. #}
{# Source URL: www.m365.cloud.microsoft #}
{# If AI tools were used: #}
{# The original Update forms were based on the Flask starter code provided in the explorations. #}
{# To enable pre-population functionality, I added code to the get routes in the app.py file but was struggling#}
{# to have the changes populate in the form after severl attempts. I gave copilot the following initial prompt: #}
{# "How can one populate the update fields upon selection of an object from the dropdown with the following route: *inserted app.py get route*.#}
{# "I beleive I am close but cannot locate my errors" After some refinement prompts and slight tweaking I arrived at the solution you see below.#}
(in-line, concerning AI assistance for getting prepopulation of update up and running)

---------- main.j2 ----------
{# Citation for the following code: #}
{# Date: 5/6/25 #}
{# Adapted from Exploation _ Web Application Technology #}
{# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration_web_application_technology_2?module_item_id=25352948#}
(top-level, concerning entire file)

---------- Responses.j2 ----------
{# Citation for the following code: #}
{# Date: 5/6/25 #}
{# Adapted from Exploation _ Web Application Technology #}
{# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration_web_application_technology_2?module_item_id=25352948#}
(top-level, concerning entire file)

{# Citation for the following code: #}
{# Date: 6/2/25 #}
{# Copied from /OR/ Adapted from /OR/ Based on #}
{# Copilot helped me solve a hunch, details below. #}
{# Source URL: www.m365.cloud.microsoft #}
{# If AI tools were used: #}
{# I realized that an empty list would result in an index error but was unsure on how to fix it/embed the proper logic. #}
{# Prompt: When keying into a list as seen in code: ***Removed for brevity, see below*, how can I use a conditional #}
{# To handle a potentially empty data set. After some refinements we arrived at the solution you see below, which is only #}
{# slighty modified from the original code #}
(in-line, concerning AI assistance in debugging an index error in our READ table)

{# Citation for the following code: #}
{# Date: 6/8/25 #}
{# Copied from /OR/ Adapted from /OR/ Based on #}
{# Starter Code + Copilot assisted in some of the embedded preopulation logic, details below. #}
{# Source URL: www.m365.cloud.microsoft #}
{# If AI tools were used: #}
{# The original Update forms were based on the Flask starter code provided in the explorations. #}
{# To enable pre-population functionality, I added code to the get routes in the app.py file but was struggling#}
{# to have the changes populate in the form after severl attempts. I gave copilot the following initial prompt: #}
{# "How can one populate the update fields upon selection of an object from the dropdown with the following route: *inserted app.py get route*.#}
{# "I beleive I am close but cannot locate my errors" After some refinement prompts and slight tweaking I arrived at the solution you see below.#}
(in-line, concerning AI assistance for getting prepopulation of update up and running)

---------- Services.j2 ----------
{# Citation for the following code: #}
{# Date: 5/6/25 #}
{# Adapted from Exploation _ Web Application Technology #}
{# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration_web_application_technology_2?module_item_id=25352948#}
(top-level, concerning entire file)

{# Citation for the following code: #}
{# Date: 6/8/25 #}
{# Copied from /OR/ Adapted from /OR/ Based on #}
{# Adapted from the exploration code with additional error catching using flash - tutorial linked below #}
{# Source URL: https://www.tutorialspoint.com/flask/flask_message_flashing.htm }
{# I needed to know how to generate a popup message on an error (duplicate unique fields), I have heard of flash before #}
{# so I researched from there and found this tutorial. The code is original + adapted from website #}
{# duplicate popup #}
(in-line, concerning flashing implementation)

{# Citation for the following code: #}
{# Date: 6/2/25 #}
{# Copied from /OR/ Adapted from /OR/ Based on #}
{# Copilot helped me solve a hunch, details below. #}
{# Source URL: www.m365.cloud.microsoft #}
{# If AI tools were used: #}
{# I realized that an empty list would result in an index error but was unsure on how to fix it/embed the proper logic. #}
{# Prompt: When keying into a list as seen in code: ***Removed for brevity, see below*, how can I use a conditional #}
{# To handle a potentially empty data set. After some refinements we arrived at the solution you see below, which is only #}
{# slighty modified from the original code #}
(in-line, concerning AI assistance in debugging an index error in our READ table)

{# Citation for the following code: #}
{# Date: 6/8/25 #}
{# Copied from /OR/ Adapted from /OR/ Based on #}
{# Starter Code + Copilot assisted in some of the embedded preopulation logic, details below. #}
{# Source URL: www.m365.cloud.microsoft #}
{# If AI tools were used: #}
{# The original Update forms were based on the Flask starter code provided in the explorations. #}
{# To enable pre-population functionality, I added code to the get routes in the app.py file but was struggling#}
{# to have the changes populate in the form after severl attempts. I gave copilot the following initial prompt: #}
{# "How can one populate the update fields upon selection of an object from the dropdown with the following route: *inserted app.py get route*.#}
{# "I beleive I am close but cannot locate my errors" After some refinement prompts and slight tweaking I arrived at the solution you see below.#}
(in-line, concerning AI assistance for getting prepopulation of update up and running)

---------- Users.j2 ----------
{# Citation for the following code: #}
{# Date: 5/6/25 #}
{# Adapted from Exploation _ Web Application Technology #}
{# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration_web_application_technology_2?module_item_id=25352948#}
(top-level, concerning entire file)

{# Citation for the following code: #}
{# Date: 6/8/25 #}
{# Copied from /OR/ Adapted from /OR/ Based on #}
{# Adapted from the exploration code with additional error catching using flash - tutorial linked below #}
{# Source URL: https://www.tutorialspoint.com/flask/flask_message_flashing.htm }
{# I needed to know how to generate a popup message on an error (duplicate unique fields), I have heard of flash before #}
{# so I researched from there and found this tutorial. The code is original + adapted from website #}
{# duplicate popup #}
(in-line, concerning flashing implementation)

{# Citation for the following code: #}
{# Date: 6/2/25 #}
{# Copied from /OR/ Adapted from /OR/ Based on #}
{# Copilot helped me solve a hunch, details below. #}
{# Source URL: www.m365.cloud.microsoft #}
{# If AI tools were used: #}
{# I realized that an empty list would result in an index error but was unsure on how to fix it/embed the proper logic. #}
{# Prompt: When keying into a list as seen in code: ***Removed for brevity, see below*, how can I use a conditional #}
{# To handle a potentially empty data set. After some refinements we arrived at the solution you see below, which is only #}
{# slighty modified from the original code #}
(in-line, concerning AI assistance in debugging an index error in our READ table)

{# Citation for the following code: #}
{# Date: 6/8/25 #}
{# Copied from /OR/ Adapted from /OR/ Based on #}
{# Starter Code + Copilot assisted in some of the embedded preopulation logic, details below. #}
{# Source URL: www.m365.cloud.microsoft #}
{# If AI tools were used: #}
{# The original Update forms were based on the Flask starter code provided in the explorations. #}
{# To enable pre-population functionality, I added code to the get routes in the app.py file but was struggling#}
{# to have the changes populate in the form after severl attempts. I gave copilot the following initial prompt: #}
{# "How can one populate the update fields upon selection of an object from the dropdown with the following route: *inserted app.py get route*.#}
{# "I beleive I am close but cannot locate my errors" After some refinement prompts and slight tweaking I arrived at the solution you see below.#}
(in-line, concerning AI assistance for getting prepopulation of update up and running)

---------- app.py ----------
# Citation for the following routes:
# Date: 5/6/25
# Base code was for routes was adapted from Exploation - Web Application Technology
# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-web-application-technology-2?module_item_id=25352948
(top-level, concerning basis for app.py page)

# RESET ROUTE
# Citation for the following code:
# Date: 5/20/25
# Copied from /OR/ Adapted from /OR/ Based on 
# Adapted from the CUD Operations exploration with a small amount of copilot, described below
# Source URL: www.m365.cloud.microsoft
# If AI tools were used: The online line that copilot helped with was the callproc. All other code
# was adapted from our class materials. I could not figure out how to call a procedure with a cursor in this
# context. Prompt used: "How do I call a stored procedure with a cursor in a route handler in Flask?"
(in-line, concerning reset route)

# Citation for the following code:
# Date: 5/19/25
# Source URL: www.m365.cloud.microsoft (copilot)
# If AI tools were used: copilot autocomplete was implemented in order to assist with alias creation on the query1 line. Everything else was already present
(in-line concerning all create routes and copilot autocomplete) - repeated for every read route

# Citation for the following routes:
# Date: 5/6/25
# Base code was for routes was adapted from Exploation - Implementing CUD Operations Into Your App
# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-implementing-cud-operations-in-your-app?module_item_id=25352968
# base code was augumented with some original code
(function level, concerning basis for create routes)

# Citation for the following code:
# Date: 6/8/25
# Copied from /OR/ Adapted from /OR/ Based on 
# Adapted from the exploration code with additional error catching using flash - tutorial linked below
# Source URL: https://www.tutorialspoint.com/flask/flask_message_flashing.htm
# I needed to know how to generate a popup message on an error (duplicate unique fields), I have heard of flash before
# so I researched from there and found this tutorial. The code is original + adapted from website
(in line, concerning tutorial for popup message functionality) - repeats within every create route

# Citation for the following routes:
# Date: 5/6/25
# Base code was for routes was adapted from Exploation - Implementing CUD Operations Into Your App
# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-implementing-cud-operations-in-your-app?module_item_id=25352968
# base code was augumented with some original code
(function level, concerning basis for delete routes)

# Citation for the following routes:
# Date: 5/6/25
# Base code was for routes was adapted from Exploation - Implementing CUD Operations Into Your App
# Source URL: https://canvas.oregonstate.edu/courses/1999601/pages/exploration-implementing-cud-operations-in-your-app?module_item_id=25352968
# base code was augumented with some original code
(function level, concerning basis for update routes)

# Citation for the following code:
# Date: 6/8/25
# Copied from /OR/ Adapted from /OR/ Based on 
# Adapted from the exploration code with additional error catching using flash - tutorial linked below
# Source URL: https://www.tutorialspoint.com/flask/flask_message_flashing.htm
# I needed to know how to generate a popup message on an error (duplicate unique fields), I have heard of flash before
# so I researched from there and found this tutorial. The code is original + adapted from website
(in line, concerning tutorial for popup message functionality) - repeats within every update route
