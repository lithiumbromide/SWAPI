---
title: "Get Appearance File Name Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Appearance_Filename_Example_VB.htm"
---

# Get Appearance File Name Example (VBA)

This example shows how to get the file name of the first appearance applied to a model.

```
'----------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified model document exists.
' 2. Verify that the specified materials file exists.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified model document.
' 2. Applies the specified appearance to the selected face.
' 3. Gets the material IDs.
' 4. Gets the file name of the first appearance applied to the model.
' 5. Examine the graphics area and the Immediate window.
'
' NOTE: Because the model is used elsewhere, do not save changes.
'----------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swFace As SldWorks.Face2
Dim swConfiguration As SldWorks.Configuration
Dim swRenderMaterial As SldWorks.RenderMaterial
Dim nbrRenderMaterials As Long
Dim fileName As String
Dim warnings As Long
Dim errors As Long
Dim status As Boolean
Dim materialName As String
Dim displayStateNames() As String
Dim materialID1 As Long
Dim materialID2 As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open model document
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cover_plate.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Create material for the appearance
    materialName = "C:\Program Files\SolidWorks Corp\SolidWorks\data\graphics\Materials\plastic\low gloss\blue low gloss plastic.p2m"
    Set swModelDocExt = swModel.Extension
    Set swRenderMaterial = swModelDocExt.CreateRenderMaterial(materialName)
```

```
    'Verify that RealView Graphics is set
    Debug.Print "RealView Graphics set? " & swModelDocExt.ViewDisplayRealView
```

```
    'Select a face and add an appearance
    status = swModelDocExt.SelectByID2("", "FACE", 4.17924256550464E-02, 7.96803314056547E-02, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swFace = swSelectionMgr.GetSelectedObject6(1, -1)
    status = swRenderMaterial.AddEntity(swFace)
    Debug.Print "Appearance added to selected face? " & status
```

```
    swModel.ClearSelection2 True
```

```
    'Get the names of display states
    'Add the appearance to all display states
    Set swConfiguration = swModel.GetActiveConfiguration
    displayStateNames = swConfiguration.GetDisplayStates
    status = swModelDocExt.AddDisplayStateSpecificRenderMaterial(swRenderMaterial, swDisplayStateOpts_e.swAllDisplayState, displayStateNames, materialID1, materialID2)
    Debug.Print "Material IDs returned by IModelDocExtension::AddDisplayStateSpecificRenderMaterial: "
    Debug.Print "  ID1: " & materialID1
    Debug.Print "  ID2: " & materialID2
```

```
    'Get the number of appearances
    nbrRenderMaterials = swModelDocExt.GetRenderMaterialsCount2(swDisplayStateOpts_e.swAllDisplayState, displayStateNames)
```

```
    'If one or more appearances are applied to the model,
    'then get the file name of the first appearance applied
    If nbrRenderMaterials > 0 Then
        swRenderMaterial.GetMaterialIds materialID1, materialID2
        Debug.Print "Material IDs returned by IModelDocExtension::GetMaterialIds: "
        Debug.Print "  ID1: " & materialID1
        Debug.Print "  ID2: " & materialID2
        Debug.Print "First appearance's file name: " & swRenderMaterial.fileName
    Else
        Debug.Print "No appearances applied to this model."
    End If
```

```
End Sub
```
