# iotassignment3

### Home Automation IoT: Django

- Muhammad Hamza Zahid (100711463)
- Janajan Jeyabalan (100698148)
- Faraaz Mohsin (100659110)


### Code Structure

views.py
---
The views code structure provides APIView class, which subclasses Django's View class.
Requests such as 'on', 'off', 'auto', and 'manual' have been defined to request POST methods and
then output the values with jSON. The requests results are displayed on localhost. 

urls.py
---
The urls code structure maps the urls to the services. The lines 13 - 16 map the urls of the application. ViewSets are used in place of views, therefore by just registering the viewsets with a router class, the URL configuration may be generated automatically. Routers automatically deciding how the logic involved in handling incoming requests should be translated to an application's URLs

models.py
---
The model code structure defines the stored data, including field types, sizes, etc. In this structure we have defined the name with character field length of 50.

templates/index.html
---
The index.html file in the template directory handles the frontend of the application the user/client interacts with.

### Architectural Design

[Architectural Diagram](https://github.com/faraazmohsin/iotassignment3/blob/main/architectural%20design/architectural_design1.PNG)

The components of Diagram 1 consist of the Django App, Models.py, Views.py and URLs.py, SQLite DB, #Controller Service, Raspbian Wheezy OS, Raspberry PI. Django App is a python package that is specifically intended for use in a Django project.  Models.py consists of the classes mode and state. Views.py consists of the classes ModeViewSet and StateViewSet. URLS.py are used to map the urls. The SQLite DB facilitates communication between the REST servies and the controllor service. The SQLite database also saves the state of the application. The Controller service consists of the services readldr(PIN), switchOnLight(PIN), switchOffLight(PIN), runAutoMode, runManualMode, getCurrentMode, getCurrentState, and the setCurrentState. The Raspbian Wheezy OS is an unofficial port of Debian wheezy with compilation settings adjusted to produce code. The Raspberry PI is the official supported operating system.     

[Functional Diagram](https://github.com/faraazmohsin/iotassignment3/blob/main/architectural%20design/architectural_design2.PNG)

This diagram shows the connections between the architectural diagram and the functional diagram. The functional diagram consists of the application, management, services, communication, security, and device. The application consists of the web app, app server, and DB server. Management consists of the App, DB, Device. Services consist of Native and Web. Communication consists of APIs and Protocols. Security consists of authentication and authorization. The Device consists sensors, actuators and computing. 
