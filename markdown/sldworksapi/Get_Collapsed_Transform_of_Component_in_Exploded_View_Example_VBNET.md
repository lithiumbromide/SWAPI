---
title: "Get Collapsed Transform of Component in Exploded View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Collapsed_Transform_of_Component_in_Exploded_View_Example_VBNET.htm"
---

# Get Collapsed Transform of Component in Exploded View Example (VB.NET)

This example shows how to get the collapsed transform of a component in an exploded view.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\pdmworks\speaker.sldasm.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the name of the active configuration.
' 2. Creates five exploded views for the active configuration.
' 3. Gets the name of each exploded view for the active configuration
'    and shows each exploded view.
' 4. Gets the name of the exploded view shown in the model.
' 5. Selects a component and gets its collapsed transform.
' 6. Examine the Immediate window.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swAssembly As AssemblyDoc
        Dim swConfigMgr As ConfigurationManager
        Dim swConfig As Configuration
        Dim swComponent As Component2
        Dim swSelectionMgr As SelectionMgr
        Dim swTransform As MathTransform
        Dim activeConfigName As String
        Dim viewNames As Object
        Dim viewName As String
        Dim i As Integer

        swModel = swApp.ActiveDoc
        swAssembly = swModel

        'Get active configuration name
        swConfigMgr = swModel.ConfigurationManager
        swConfig = swConfigMgr.ActiveConfiguration
        activeConfigName = swConfig.Name

        'Create five exploded views in the active configuration
        For i = 0 To 4
            swAssembly.CreateExplodedView()
        Next i

        'Get the name of each exploded view in the active configuration
        'and show each exploded view
        viewNames = swAssembly.GetExplodedViewNames2(activeConfigName)
        For i = 0 To UBound(viewNames)
            viewName = viewNames(i)
            swAssembly.ShowExploded2(True, viewName)
        Next i

        'Get the name of exploded view shown in model
        viewName = ""
        swModelDocExt = swModel.Extension
        swModelDocExt.IsExploded(viewName)
        Debug.Print("Name of exploded view shown in model: " & viewName)

        'Select a component and get its collapsed transform
        swModelDocExt.SelectByID2("speaker_frame-1@speaker", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swComponent = swSelectionMgr.GetSelectedObjectsComponent4(1, -1)
        Debug.Print("  Name of component whose collapsed transform to get in the exploded view: " & swComponent.Name2)
        swTransform = swComponent.GetSpecificTransform(True)
        Debug.Print("    Transform:")
        Debug.Print("      Rotate     = (" & swTransform.ArrayData(0) & ", " & swTransform.ArrayData(1) & ", " & swTransform.ArrayData(2) & ")")
        Debug.Print("                 = (" & swTransform.ArrayData(3) & ", " & swTransform.ArrayData(4) & ", " & swTransform.ArrayData(5) & ")")
        Debug.Print("                 = (" & swTransform.ArrayData(6) & ", " & swTransform.ArrayData(7) & ", " & swTransform.ArrayData(8) & ")")
        Debug.Print("      Translate  = (" & swTransform.ArrayData(9) & ", " & swTransform.ArrayData(10) & ", " & swTransform.ArrayData(11)& ")")

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
