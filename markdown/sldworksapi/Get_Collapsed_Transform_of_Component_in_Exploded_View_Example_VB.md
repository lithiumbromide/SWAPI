---
title: "Get Collapsed Transform of Component in Exploded View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Collapsed_Transform_of_Component_in_Exploded_View_Example_VB.htm"
---

# Get Collapsed Transform of Component in Exploded View Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swAssembly As SldWorks.AssemblyDoc
Dim swConfigMgr As SldWorks.ConfigurationManager
Dim swConfig As SldWorks.Configuration
Dim swComponent As SldWorks.Component2
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swTransform As SldWorks.MathTransform
Dim activeConfigName As String
Dim viewNames As Variant
Dim viewName As String
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swAssembly = swModel
```

```
    'Get active configuration name
    Set swConfigMgr = swModel.ConfigurationManager
    Set swConfig = swConfigMgr.ActiveConfiguration
    activeConfigName = swConfig.Name
```

```
    'Create five exploded views in the active configuration
    For i = 0 To 4
        swAssembly.CreateExplodedView
    Next i
```

```
    'Get the name of each exploded view in the active configuration
    'and show each exploded view
    viewNames = swAssembly.GetExplodedViewNames2(activeConfigName)
    For i = 0 To UBound(viewNames)
        viewName = viewNames(i)
        swAssembly.ShowExploded2 True, viewName
    Next i
```

```
    'Get the name of exploded view shown in model
    viewName = ""
    Set swModelDocExt = swModel.Extension
    swModelDocExt.IsExploded viewName
    Debug.Print "Name of exploded view shown in model: " & viewName
```

```
    'Select a component and get its collapsed transform
    swModelDocExt.SelectByID2 "speaker_frame-1@speaker", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0
    Set swSelectionMgr = swModel.SelectionManager
    Set swComponent = swSelectionMgr.GetSelectedObjectsComponent4(1, -1)
    Debug.Print "  Name of component whose collapsed transform to get in the exploded view: " & swComponent.Name2
```

```
    Set swTransform = swComponent.GetSpecificTransform(True)
    Debug.Print "    Transform:"
    Debug.Print "      Rotate     = (" & swTransform.ArrayData(0) & ", " & swTransform.ArrayData(1) & ", " & swTransform.ArrayData(2) & ")"
    Debug.Print "                 = (" & swTransform.ArrayData(3) & ", " & swTransform.ArrayData(4) & ", " & swTransform.ArrayData(5) & ")"
    Debug.Print "                 = (" & swTransform.ArrayData(6) & ", " & swTransform.ArrayData(7) & ", " & swTransform.ArrayData(8) & ")"
    Debug.Print "      Translate  = (" & swTransform.ArrayData(9) & ", " & swTransform.ArrayData(10) & ", " & swTransform.ArrayData(11) & ")"
```

```
End Sub
```
