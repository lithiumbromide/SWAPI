---
title: "Add ActiveX Tabs to Model View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_ActiveX_Tabs_to_Model_View_Example_VBNET.htm"
---

# Add ActiveX Tabs to Model View Example (VB.NET)

This example shows how to add two ActiveX tabs to a model view.

'----------------------------------------------------------
' Preconditions:
' 1. In the IDE, reference your ActiveX control file
' (click **Project > Add Reference > Browse** and browse
' to the folder where the ActiveX control resides and click
' the ActiveX control file **> OK**).
' 2. Verify that the specified part document exists.
' 3. Replace `activex_control_component_declaration` and
' `activex_control_CLSID_or_ProgID` with your ActiveX control's
' information.
'
' Postconditions:
' 1. Opens the part document and adds two new tabs to the model view.
' 2. Activates the model view.
' 3. To verify the ActiveX controls on the new tabs,
' interactively click tab.
'
' NOTE: Because the part document is used elsewhere,
' do not save changes.
'------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System

Partial Class SolidWorksMacro

Public Sub Main()

Const calTabName1 As String = "Tab 1"
Const calTabName2 As String = "Tab 2"

Dim swModel As ModelDoc2
Dim swModViewMgr As ModelViewManager
Dim calCtrl1 As `activex_control_component_declaration`
Dim calCtrl2 As `activex_control_component_declaration`
Dim fileName As String
Dim errors As Integer
Dim warnings As Integer
Dim status As Boolean

swApp = CreateObject("SldWorks.Application")
fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\fillets\knob.sldprt"
swModel = swApp.**OpenDoc6**(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
swModViewMgr = swModel.**ModelViewManager**

' Add the ActiveX control tabs
calCtrl1 = swModViewMgr.**AddControl**(calTabName1, "`activex_control_CLSID_or_ProgID`", "")
calCtrl2 = swModViewMgr.**AddControl**(calTabName2, "`activex_control_CLSID_or_ProgID`", "")

status = swModViewMgr.**ActivateControlTab**(calTabName1)
status = swModViewMgr.**IsControlTabActive**(calTabName1)
status = swModViewMgr.**IsModelTabActive**

' Switch back to model view
status = swModViewMgr.**ActivateModelTab**

End Sub

''' <summary>
''' The SldWorks swApp variable is pre-assigned for you.
''' </summary>
Public swApp As SldWorks

End Class
