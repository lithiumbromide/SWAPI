---
title: "Add ActiveX Tabs to Model View Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_ActiveX_Tabs_to_Model_View_Example_CSharp.htm"
---

# Add ActiveX Tabs to Model View Example (C#)

This example shows how to add two ActiveX tabs to a model view.

//----------------------------------------------------------
// Preconditions:
// 1. In the IDE, reference your ActiveX control file
// (click **Project > Add Reference > Browse** and browse
// to the folder where the ActiveX control resides and click
// the ActiveX control file **> OK**).
// 2. Verify that the specified part document exists.
// 3. Replace `activex_control_component_declaration` and
// `activex_control_CLSID_or_ProgID` with your ActiveX control's
// information.
//
// Postconditions:
// 1. Opens the part document and adds two new tabs to the model view.
// 2. Activates the model view.
// 3. To verify the ActiveX controls on the new tabs, click each tab.
//
// NOTE: Because the part document is used elsewhere,
// do not save changes.
//------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using Microsoft.VisualBasic;

namespace AddControlModelViewManagerCSharp.csproj
{
partial class SolidWorksMacro
{
public void Main()
{
const string calTabName1 = "Tab 1";
const string calTabName2 = "Tab 2";

ModelDoc2 swModel = default(ModelDoc2);
ModelViewManager swModViewMgr = default(ModelViewManager);
`activex_control_component_declaration` calCtrl1 = default(`activex_control_component_declaration`);
`activex_control_component_declaration` calCtrl2 = default(`activex_control_component_declaration`);
string fileName = null;
int errors = 0;
int warnings = 0;
bool status = false;

fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\SOLIDWORKS 2018\\samples\\tutorial\\fillets\\knob.sldprt";
swModel = swApp.**OpenDoc6**(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
swModViewMgr = swModel.**ModelViewManager**;

// Add the tabs
calCtrl1 = (`activex_control_component_declaration`)swModViewMgr.**AddControl**(calTabName1, "`activex_control_CLSID_or_ProgID`", "");
calCtrl2 = (`activex_control_component_declaration`)swModViewMgr.**AddControl**(calTabName2, "`activex_control_CLSID_or_ProgID`", "");

status = swModViewMgr.**ActivateControlTab**(calTabName1);
status = swModViewMgr.**IsControlTabActive**(calTabName1);
status = swModViewMgr.**IsModelTabActive**();

// Switch back to model view
status = swModViewMgr.**ActivateModelTab**();

}

/// <summary>
/// The SldWorks swApp variable is pre-assigned for you.
/// </summary>

public SldWorks swApp;

}
}
