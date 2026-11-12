---
title: "Isolate Component Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Isolate_Component_Example_VBNET.htm"
---

# Isolate Component Example (VB.NET)

This example shows how to isolate a component and save the characteristics of the new display state.

```
'----------------------------------------------------------
' Preconditions: Verify that the assembly exists.
'
' Postconditions:
' 1. Opens the assembly.
' 2. Selects a component.
' 3. Isolates the selected component and changes the
'    display of all of the other components to wireframe.
' 4. Saves the display characteristics to a new display
'    state.
' 5. Exits isolate.
' 6. Click the ConfigurationManager tab and double-click
'    Test_Display_State.
'
' NOTE: Because the assembly is used elsewhere, do not
' save changes.
'----------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swAssembly As AssemblyDoc
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim assemblyName As String
        Dim componentToIsolate As String

        assemblyName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\interferenceassem.sldasm"
        swModel = swApp.OpenDoc6(assemblyName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension
        swAssembly = swModel
        componentToIsolate = "squarepad_pink-1@interferenceassem"
        status = swModelDocExt.SelectByID2(componentToIsolate, "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)

        'Isolate selected component and set the
        'visibility of all of the other components to wireframe
        status = swAssembly.Isolate()
        swAssembly.SetIsolateVisibility(swIsolateVisibility_e.swIsolateVisibility_WIREFRAME)

        'Save the new display state as Test_Display_State
        status = swAssembly.SaveIsolate("Test_Display_State")

        'Exit isolate
        status = swAssembly.ExitIsolate()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
