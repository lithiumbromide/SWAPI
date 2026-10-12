---
title: "Get Component State Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Component_State_Example_VBNET.htm"
---

# Get Component State Example (VB.NET)

This example shows how to find out if the selected component is resolved or suppressed, hidden or visible, and whether or not it's a rigid or flexible subassembly. This example also gets the persistent ID of the selected component.

```
'---------------------------------------------------
' Preconditions:
' 1. Ensure that the specified assembly document
'    to open exists.
' 2. Open the Immediate window.
' 3. Run the macro.
'
' Postconditions:
' 1. Opens the assembly document.
' 2. Selects the subassembly.
' 3. Prints to the Immediate window:
'    * Paths to the assembly and subassembly documents
'    * Whether the component is hidden, fixed,
'      or suppressed
'    * Component's persistent ID
'    * Component's solving state
' 4. Examine the Immediate window.
'----------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swAssy As AssemblyDoc
        Dim swSelMgr As SelectionMgr
        Dim swComp As Component2
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer

        ' Open assembly document
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\98food processor.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension

        ' Select subassembly
        status = swModelDocExt.SelectByID2("blade shaft-1@98food processor", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        swSelMgr = swModel.SelectionManager
        swAssy = swModel
        swComp = swSelMgr.GetSelectedObjectsComponent3(1, 0)

        ' Print to the Immediate window the path and state of the
        ' selected component
        Debug.Print("File = " & swModel.GetPathName)
        Debug.Print("  Component   = " & swComp.Name2)
        Debug.Print("    Path           = " & swComp.GetPathName)
        Debug.Print("    IsHidden       = " & swComp.IsHidden(True))
        Debug.Print("    IsFixed        = " & swComp.IsFixed)
        Debug.Print("    GetSuppression = " & swComp.GetSuppression)
        Debug.Print("    ID             = " & swComp.GetID)

        ' 0 =  if subassembly is rigid
        ' 1 =  if subassembly is flexible
        ' -1 = selected component is a part component
        Debug.Print("    Solving        = " & swComp.Solving)
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
