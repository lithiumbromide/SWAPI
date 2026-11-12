---
title: "Add and Modify Equations Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Equations_Example_VB.htm"
---

# Add and Modify Equations Example (VBA)

This example shows how to add equations to multiple configurations of a part created in SOLIDWORKS 2014 or later.

```
'----------------------------------------------------------------------------
' Preconditions: Open a part created in SOLIDWORKS 2014 or later that has a
' Boss-Extrude1 feature and multiple configurations.
'
' Postconditions:
' 1. Adds two equations to all configurations.
' 2. Modifies the equation at index 1.
' 3. Click Tools > Equations and examine each configuration in the dialog.
' ---------------------------------------------------------------------------
Option Explicit
```

```vb
Sub main()
    Dim SwApp           As SldWorks.SldWorks
     Dim Part            As SldWorks.ModelDoc2
     Dim swEquationMgr   As SldWorks.EquationMgr
     Dim longEquation    As Long

    Set SwApp = Application.SldWorks
     Set Part = SwApp.ActiveDoc
    Set swEquationMgr = Part.GetEquationMgr
     If swEquationMgr Is Nothing Then ErrorMsg SwApp, "Failed to get the equation manager"

    'Add a global variable assignment at index, 0, to all configurations
     longEquation = swEquationMgr.Add3(0, """A"" = 2in", True, swAllConfiguration, Empty)
     If longEquation <> 0 Then ErrorMsg SwApp, "Failed to add a global variable assignment"

    'Add a dimension equation at index, 1, to all configurations
     longEquation = swEquationMgr.Add3(1, """D1@Boss-Extrude1"" = 0.05in", True, swAllConfiguration, Empty)
     If longEquation <> 1 Then ErrorMsg SwApp, "Failed to add a dimension equation"

    'Modify dimension equation at index, 1, in all configurations
     longEquation = swEquationMgr.SetEquationAndConfigurationOption(1, """D1@Boss-Extrude1"" = 0.07in", swAllConfiguration, Empty)
     If longEquation <> 1 Then ErrorMsg SwApp, "Failed to modify a dimension equation"

End Sub

Function ErrorMsg(SwApp As Object, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Function
```
