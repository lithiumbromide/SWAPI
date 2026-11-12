---
title: "Inspecting the SOLIDWORKS VB.NET Add-In Template"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Using_SolidWorks_VB.NET_Add-In_Wizard_to_Create_VB.NET_Add-In.htm"
---

# Inspecting the SOLIDWORKS VB.NET Add-In Template

## Inspecting the SOLIDWORKS VB.NET Add-in Template

This topic identifies and describes the classes provided by the [SOLIDWORKS VB.NET add-in template](SolidWorks_CSharp_and_VB.NET__Project_Templates.htm).

### Examining Visual Basic .NET Add-In Classes

Inspect the add-in in Visual Studio's Solution Explorer. These classes are copied to the add-in from the SOLIDWORKS VB.NET Add-in Template:

| Class | Description |
| --- | --- |
| AssemblyInfo.vb | This file provides a means to organize and publish assembly-specific information. |
| EventHandling.vb | This file contains the event handling objects for documents and model views. The DocumentEventHandler object is a base class that exposes the interface and contains code for dealing with ModelView events. PartEventHandler, AssemblyEventHandler, and DrawingEventHandler are the three object types that can listen for document events. There must be one instance of each class for each open document of that type. The ModelViewEventHandler object listens for ModelView events. There should be one instance of ModelViewEventHandler for each ModelView in each open document. |
| PMPHandler.vb | This file contains the class that implements the PropertyManager page handler interface. An instance of this object is passed to SOLIDWORKS when creating a PropertyManager page. When a control on the page is manipulated, the corresponding function or subroutine in this object is called. |
| SwAddin n .vb | This file contains the main add-in class. Visual Studio adds the letter n to the default name SwAddin, if more than one project by that name exists in the same location. Examine the code in each region of this file: Region Description Local Variables Contains the definitions of this class's variables SOLIDWORKS Registration Contains functions to register and unregister the add-in ISwAddin Implementation Contains ConnectToSW() and DisconnectFromSW() which are the entry and exit points for the add-in UI Methods Contains functions and subroutines that define how the add-in behaves within the SOLIDWORKS application Event Methods Contains SOLIDWORKS event handling functions and subroutines Event Handlers Contains the event callbacks for the SOLIDWORKS object UI Callbacks Contains functions and subroutines that are called from the add-in user interface |
| Region | Description |
| Local Variables | Contains the definitions of this class's variables |
| SOLIDWORKS Registration | Contains functions to register and unregister the add-in |
| ISwAddin Implementation | Contains ConnectToSW() and DisconnectFromSW() which are the entry and exit points for the add-in |
| UI Methods | Contains functions and subroutines that define how the add-in behaves within the SOLIDWORKS application |
| Event Methods | Contains SOLIDWORKS event handling functions and subroutines |
| Event Handlers | Contains the event callbacks for the SOLIDWORKS object |
| UI Callbacks | Contains functions and subroutines that are called from the add-in user interface |
| UserPMPage.vb | This file contains the wrapper class and layout methods for the add-in's PropertyManager page. To modify the controls on the PropertyManager page, change the code in the AddControls() subroutine. Add all controls to group boxes. Group boxes are displayed top to bottom in the order in which they are added to the page. Controls are displayed top to bottom in the order in which they are added to the group box. |

[Back to top](#Top)

To learn more about add-ins and their menu items and toolbars:

- [Add-in Callbacks](Add-in_Callbacks.htm)
- [Add-in Icons](Add-in_Icons.htm)
- [Add-in Shortcut Menus](Add-in_Shortcut_Menus.htm)
- [Add-in Toolbars](Add-in_Toolbars.htm)
