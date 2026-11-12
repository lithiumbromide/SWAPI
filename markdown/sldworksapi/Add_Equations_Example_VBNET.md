---
title: "Add and Modify Equations Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Equations_Example_VBNET.htm"
---

# Add and Modify Equations Example (VB.NET)

This example shows how to add equations to multiple configurations of a part created in SOLIDWORKS 2014 or later.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open a part created in SOLIDWORKS 2014 or later that has a
 ' Boss-Extrude1 feature and multiple configurations.
 '
 ' Postconditions:
 ' 1. Adds two equations to all configurations.
 ' 2. Modifies the equation at index 1.
 ' 3. Click Tools > Equations and examine each configuration in the dialog.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Sub main()

         Dim Part As ModelDoc2
         Dim swEquationMgr As EquationMgr
         Dim longEquation As Long

         Part = SwApp.ActiveDoc

         swEquationMgr = Part.GetEquationMgr
         If swEquationMgr Is Nothing Then ErrorMsg(SwApp, "Failed to get the equation manager")

         'Add a global variable assignment at index, 0, to all configurations
         longEquation = swEquationMgr.Add3(0, """A"" = 2in", True, swInConfigurationOpts_e.swAllConfiguration,  Nothing)
         If longEquation <> 0 Then ErrorMsg(SwApp, "Failed to add a global variable assignment")

         'Add a dimension equation at index, 1, to all configurations
         longEquation = swEquationMgr.Add3(1, """D1@Boss-Extrude1"" = 0.05in", True, swInConfigurationOpts_e.swAllConfiguration,  Nothing)
         If longEquation <> 1 Then ErrorMsg(SwApp, "Failed to add a dimension equation")

         'Modify dimension equation at index, 1, in all configurations
         longEquation = swEquationMgr.SetEquationAndConfigurationOption(1, """D1@Boss-Extrude1"" = 0.07in", swInConfigurationOpts_e.swAllConfiguration,  Nothing)
         If longEquation <> 1 Then ErrorMsg(SwApp, "Failed to modify a dimension equation")

     End Sub

     Sub ErrorMsg(ByVal SwApp As Object, ByVal Message As String)
         SwApp.SendMsgToUser2(Message, 0, 0)
         SwApp.RecordLine("'*** WARNING - General")
         SwApp.RecordLine("'*** " & Message)
         SwApp.RecordLine("")
     End Sub

     Public swApp As SldWorks

 End  Class
```
