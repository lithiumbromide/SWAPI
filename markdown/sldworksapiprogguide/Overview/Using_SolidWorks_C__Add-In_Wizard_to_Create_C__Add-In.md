---
title: "Inspecting the SOLIDWORKS C# Add-in Template"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Using_SolidWorks_C__Add-In_Wizard_to_Create_C__Add-In.htm"
---

# Inspecting the SOLIDWORKS C# Add-in Template

This topic identifies and describes the classes provided by the [SOLIDWORKS C# add-in template](SolidWorks_CSharp_and_VB.NET__Project_Templates.htm).

### Examining Visual C# .NET Add-In Classes

Inspect the add-in in Visual Studio's Solution Explorer. These classes are copied to the add-in from the SOLIDWORKS C# Add-in Template:

| Class | Description |
| --- | --- |
| AssemblyInfo.cs | This file provides a means to organize and publish assembly-specific information. |
| EventHandling.cs | This file contains the event handling objects for documents and model views. The DocumentEventHandler object is a base class that exposes the interface and contains code for dealing with ModelView events. PartEventHandler, AssemblyEventHandler, and DrawingEventHandler are the three object types that can listen for document events. There must be one instance of each class for each open document of that type. The ModelViewEventHandler object listens for ModelView events. There should be one instance of ModelViewEventHandler for each ModelView in each open document. |
| PMPHandler.cs | This file contains the class that implements the PropertyManager page handler interface. An instance of this object is passed to SOLIDWORKS when creating a PropertyManager page. When a control on the page is manipulated, the corresponding method in this object is called. |
| SwAddin n .cs | This file contains the main add-in class. Visual Studio adds the letter n to the default name SwAddin, if more than one project by that name exists in the same location. Examine the code in each region of this file: Region Description Local Variables Contains the definitions of this class's variables SOLIDWORKS Registration Contains methods to register and unregister the add-in ISwAddin Implementation Contains ISwAddin::ConnectToSW() and ISwAddin::DisconnectFromSW() which are the entry and exit points for the add-in UI Methods Contains methods that define how the add-in behaves within the SOLIDWORKS application Event Methods Contains SOLIDWORKS event handling methods Event Handlers Contains the event callbacks for the SOLIDWORKS object UI Callbacks Contains methods that are called from the add-in user interface |
| Region | Description |
| Local Variables | Contains the definitions of this class's variables |
| SOLIDWORKS Registration | Contains methods to register and unregister the add-in |
| ISwAddin Implementation | Contains ISwAddin::ConnectToSW() and ISwAddin::DisconnectFromSW() which are the entry and exit points for the add-in |
| UI Methods | Contains methods that define how the add-in behaves within the SOLIDWORKS application |
| Event Methods | Contains SOLIDWORKS event handling methods |
| Event Handlers | Contains the event callbacks for the SOLIDWORKS object |
| UI Callbacks | Contains methods that are called from the add-in user interface |
| UserPMPage.cs | This file contains the wrapper class and layout methods for the add-in's PropertyManager page. To modify the controls on the PropertyManager page, change the code in the AddControls() method. Add all controls to group boxes. Group boxes are displayed top to bottom in the order in which they are added to the page. Controls are displayed top to bottom in the order in which they are added to the group box. |

[Back to top](Using_SolidWorks_C__Add-In_Wizard_to_Create_C__Add-In.htm)

To learn more about add-ins and their menu items and toolbars:

- [Add-in Callbacks](Add-in_Callbacks.htm)
- [Add-in Icons](Add-in_Icons.htm)
- [Add-in Shortcut Menus](Add-in_Shortcut_Menus.htm)
- [Add-in Toolbars](Add-in_Toolbars.htm)
