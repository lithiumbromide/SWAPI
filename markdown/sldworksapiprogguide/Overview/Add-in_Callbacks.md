---
title: "Add-in Callback and Enable Methods"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Add-in_Callbacks.htm"
---

# Add-in Callback and Enable Methods

There are two possible signatures for the callback and enable methods of menu items and toolbar commands of SOLIDWORKS add-ins:

- No parameters
- One string parameter (supported in SOLIDWORKS 2012 SP0 and later)

### No Parameters in the Callback or Enable Method

Implement one callback method and one enable method for each menu item and toolbar command in the add-in. These callback and enable methods take no arguments.

#### Example:

```vb
cmdIndex0 = cmdGroup.AddCommandItem2("CreateCube", -1, "Create a cube", "Create cube", 0, "CreateCube", "EnableCube", mainItemID1, menuToolbarOption);
cmdIndex1 = cmdGroup.AddCommandItem2("Show PMP", -1, "Display sample property manager", "Show PMP", 2, "ShowPMP", "EnablePMP", mainItemID2, menuToolbarOption);

 #Region UI Callbacks
```

```vb
 public void CreateCube
 {
     // Create Cube command code
 }
 public int EnableCube
 {
     // Return status of the Create Cube enablement
     return 0;
 }
 public void ShowPMP
 {
     // Show PMP command code
 }
 public int EnablePMP
 {
     // Return status of Show PMP enablement
     return 0;
 }
```

In the example above, one callback method and one enable method are implemented for each command item. These methods are implemented somewhere else in the add-in, usually in the UI Callback region.

### One String Parameter in the Callback or Enable Method

Implement one callback method and one enable method, each having one string parameter. Do this when you want to use the same callback/enable method for all of your menu items and toolbar commands. The argument in the method call indicates which menu item or toolbar command behavior to invoke.

#### Example:

```vb
 // Create command items, passing to the callback and enable methods a number indicating which menu item or toolbar command
     cmdIndex0 = cmdGroup.AddCommandItem2("CreateCube", -1, "Create a cube", "Create cube", 0,  "CallBackFunction(1)", "EnableFunction(1)", mainItemID1, menuToolbarOption);
     cmdIndex1 = cmdGroup.AddCommandItem2("Show PMP", -1, "Display PMP", "Show PMP", 2,  "CallBackFunction(2)", "EnableFunction(2)", mainItemID2, menuToolbarOption);

 #Region UI Callbacks
         // Single-parameter callback method
         public void CallBackFunction(string data)
         {
             int commandType = int.Parse(data);
              switch (commandType)
             {
                  case 1:
                     // Create cube command code
                     break;
                  case 2:
                     // Show PMP command code
                     break;
                  default:
                     break;
             }
         }

         // Single-parameter enable method
         public int EnableFunction(string data)
         {
             int commandType = int.Parse(data);
             int arg;
              switch (commandType)
             {
                  case 1:
                     // Return status of Create Cube enablement
                      arg = 0;
                     break;
                  case 2:
                     // Return status of Show PMP enablement
                     arg = 1
                     break;
                  default:
                     arg = 0
                     break;
             }
              return arg;
         }
```

In the example above, the same callback and enable methods are used for multiple menu items. The parameter in the callback and enable methods differentiates which behavior to invoke. The callback and enable method parameters must be of data type string.

Download **Using Single-Argument Callbacks in SolidWorks Add-ins,** which is a complete add-in example, from the SOLIDWORKS API forum. You must be a SOLIDWORKS subscription customer to access the SOLIDWORKS API forum documents.

To learn more about add-ins and their menu items and toolbars:

- [Add-in Icons](Add-in_Icons.htm)
- [Add-in Shortcut Menus](Add-in_Shortcut_Menus.htm)
- [Add-in Toolbars](Add-in_Toolbars.htm)
- [Using SwAddin to Create a SOLIDWORKS Add-in](Using_SwAddin_to_Create_a_SolidWorks_Addin.htm)
- [SOLIDWORKS API Add-in Templates and Wizards](SolidWorks_API_Add-Ins,_Project_Templates,_and_Wizards.htm)
