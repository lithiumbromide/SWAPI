---
title: "Fire Events When PropertyManager Page Opened and Canceled Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Events_When_PropertyManager_Page_Opened_and_Canceled_Example_CSharp.htm"
---

# Fire Events When PropertyManager Page Opened and Canceled Example (C#)

## Fire Events When PropertyManager Page Opened and Canceled (C#)

This example shows how to get the SOLIDWORKS command ID, PropertyManager title, and whether the user interface is active. Events are fired before the PropertyManager page is opened and when it is canceled.

//------------------------------------------
// Preconditions:
// 1. Verify that the part to open exists.
// 2. Add a reference to **SolidWorks.Interop.swcommands.dll**.
// 3. Open the Immediate window.
// 4. Clear **Tools > Options > Stop VSTA debugger on**
// **macro exit**, if it's selected.
//
// Postconditions:
// 1. Opens the part.
// 2. Fires the CommandOpenPreNotify event; click **OK**
// to close the message box.
// 3. Opens the Fillet PropertyManager page.
// 4. Gets the title of the PropertyManager page, whether the
// user interface is active, and whether the command ID
// is a fillet.
// 5. Click **X** on the Fillet PropertyManager page
// to cancel it.
// 6. Fires the CommandCloseNotify event; click **OK** to close
// the message box.
// 7. Examine the Immediate window.
// 8. Click **Stop Debugging** in the IDE.
// 9. Select **Tools > Options > Stop VSTA debugger on**
// **macro exit**, if you cleared it in Preconditions
// step 4.
//--------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using SolidWorks.Interop.swcommands;
using System.Windows.Forms;

namespace GetRunningCommandInfoSldWorksCSharp.csproj
{
partial class SolidWorksMacro
{

public SldWorks swAppSW;

public void Main()
{

ModelDoc2 swModel;
ModelDocExtension swModelDocExt;
string modelName = null;
int errors = 0;
int warnings = 0;
int commandID = 0;
string pmpTitle = null;
bool isUIActive = false;

// Set up event
swAppSW = (SldWorks)swApp;
AttachEventHandlers();

// Open the model
modelName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\fillets\\knob.sldprt";
swModel = (ModelDoc2)swApp.**OpenDoc6**(modelName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
swModelDocExt = (ModelDocExtension)swModel.**Extension**;

// Open the Fillet PropertyManager Page,
// which causes the CommandOpenPreNotify event
// to fire
swModelDocExt.**RunCommand**((int)swCommands_e.swCommands_Fillet, "Fillet");

// Get the command ID if the command is a fillet,
// get the PropertyManager page title if one is active,
// and get whether the user interface is active
swApp.**GetRunningCommandInfo**(out commandID, out pmpTitle, out isUIActive);

if (!string.IsNullOrEmpty(pmpTitle)) Debug.Print("Title of PropertyManager page: " + pmpTitle);
Debug.Print("Is user interface active? " + isUIActive);
if ((commandID == 9))
{
Debug.Print("Command ID: " + "swCommands_Fillet");
}
else
{
Debug.Print("Command ID: " + "Not a fillet.");

}
}

public void AttachEventHandlers()
{
AttachSWEvents();
}

public void AttachSWEvents()
{
swAppSW.CommandOpenPreNotify += this.swAppSW_CommandOpenPreNotify;
swAppSW.CommandCloseNotify += this.swAppSW_CommandCloseNotify;
}

private int swAppSW_**CommandOpenPreNotify**(int command, int userCommand)
{
//Send message when the Fillet PropertyManager page is about to open
if ((command == (int)swCommands_e.swCommands_Fillet)) MessageBox.Show("Fillet PropertyManager page is about to open.");
return 0;
}
private int swAppSW_**CommandCloseNotify**(int command, int reason)
{
//Send message when the Fillet PropertyManager page is canceled
MessageBox.Show("Fillet PropertyManager page was canceled.");
return 0;
}

/// <summary>
/// The SldWorks swApp variable is pre-assigned for you.
/// </summary>
public SldWorks swApp;

}
}
