# mapui

### About:
The GMT Map User Interface (MapUI) is a front-end module for creating maps using the [Generic Mapping Tools (GMT)](https://gmt.soest.hawaii.edu/) in a Linux environment. 

This project is currently still in production. Version 1.0 accepts plain text files consisting of X/Y points and plots those points on a GMT map. Ingesting and mapping binary raster data will be incorporated in the next version. 

### Production:
The main interface was designed using QT Designer (QT5) and all code written in Python 3.76
The application does require GMT version 5.4 be installed on the system

### Project Structure:
The main application executable python file is located in the project root. All other supporting files are located in the support directory, categorized by sub-folder:
* data: Contains the back-end supporting code for each view as well as other supporting classes.
* icons: Icons used to decorate the interface buttons and widgets.
* images: Screenshots used to develop the help files.
* Interfaces: The QT Designer .ui files for each interface.
* views: The front-end code for each interface (options window, projections window, etc.) in order to set up widget states and actions.
* widgtes: Any custom subclassed widgets created for this project.

![User Interface](/mapui/support/images/example.png)
