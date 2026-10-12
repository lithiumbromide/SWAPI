---
title: "Add and Delete Appearances from Specific Display States Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_and_Delete_Materials_from_Specific_Display_States_Example_VBNET.htm"
---

# Add and Delete Appearances from Specific Display States Example (VB.NET)

This example shows how to add an appearance to and delete an appearance from specific display states.

```vb
 '---------------------------------------------------------------------------
' Preconditions:
' 1. Specified model exists.
' 2. Specified appearance exists.
' 3. Open an Immediate window.
'
' Postconditions:
' 1. Creates Display State 2 and Display State 3 for the active
'    configuration.
' 2. Applies specified appearance to all display states of the active
'    configuration.
' 3. Press F5.
' 4. Deletes specified appearance from all display states of the active
'    configuration.
' 5. Press F5.
' 6. Closes document.
 '---------------------------------------------------------------------------
```

```vb
Imports
```

SolidWorks.Interop.sldworks

```vb
Imports
```

SolidWorks.Interop.swconst

```vb
Imports
```

System.Runtime.InteropServices

```vb
Imports
```

System

```vb
Imports
```

System.Diagnostics

```vb
Partial
```

Class

SolidWorksMacro

Dim swModel As

ModelDoc2

Dim swConfig As

Configuration

Dim swModelDocExt As

ModelDocExtension

Dim swEntity As

Entity

Dim swSelMgr As

SelectionMgr

Dim swRenderMaterial As

RenderMaterial

Dim displayStateNames As Object

Dim status As Boolean

Dim modelName As String

Dim materialName As String

Dim errors As Integer

Dim warnings As Integer

Dim nbrDisplayStates As Integer

Dim i As Integer

Dim k As Integer

Dim nbrMaterials As Integer

Dim materialID1 As Integer

Dim materialID2 As Integer

Dim materialID1_ToDelete(0) As Integer

Dim materialID2_ToDelete(0) As Integer

Sub

main()

```vb
modelName =
```

"C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\dimxpert\bracket_auto_manual.sldprt"

```vb
swModel = swApp.OpenDoc6(modelName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent,
```

""

, errors, warnings)

```vb
swModelDocExt = swModel.Extension
```

' Get active configuration and create a new display

' state for this configuration

```vb
swConfig = swModel.GetActiveConfiguration
status = swConfig.CreateDisplayState(
```

"Display State 2"

)

```vb
swModel.ForceRebuild3(
```

True

)

' Get active configuration and create another new

' display state for this configuration

```vb
swConfig = swModel.GetActiveConfiguration
status = swConfig.CreateDisplayState(
```

"Display State 3"

)

```vb
swModel.ForceRebuild3(
```

True

)

' Create appearance

```vb
materialName =
```

"C:\Program Files\SolidWorks Corp\SolidWorks\data\graphics\materials\metal\steel\stainless steel treadplate.p2m"

```vb
swRenderMaterial = swModelDocExt.CreateRenderMaterial(materialName)
```

' Select a face and add the appearance to that face

```vb
status = swModelDocExt.SelectByID2(
```

"", "FACE", 0.07151920610502, 0.0952597996959, 0.009524999999996, False, 0, Nothing

, 0)

```vb
swSelMgr = swModel.SelectionManager
swEntity = swSelMgr.GetSelectedObject6(1, -1)
status = swRenderMaterial.AddEntity(swEntity)
```

' Get the names of display states

```vb
displayStateNames = swConfig.GetDisplayStates
nbrDisplayStates = swConfig.GetDisplayStatesCount
Debug.Print(
```

"This configuration's display states ="

)

For i = 0 To

(nbrDisplayStates - 1)

```vb
Debug.Print(
```

" Display state name = "

& displayStateNames(i))

Next

i

' Add appearance to all of the display states

```vb
status = swModelDocExt.AddDisplayStateSpecificRenderMaterial(swRenderMaterial, swDisplayStateOpts_e.swAllDisplayState, displayStateNames, materialID1, materialID2)
```

' Get the appearance IDs and names

```vb
swRenderMaterial.GetMaterialIds(materialID1, materialID2)
Debug.Print(
```

" Appearance IDs:"

)

```vb
Debug.Print(
```

" ID1 = "

& materialID1)

```vb
Debug.Print(
```

" ID2 = "

& materialID2)

```vb
nbrMaterials = swModelDocExt.GetRenderMaterialsCount2(swDisplayStateOpts_e.swAllDisplayState,
```

Nothing

)

```vb
Debug.Print(
```

" Number of appearances: "

& nbrMaterials)

For k = 0 To

(nbrMaterials - 1)

```vb
Debug.Print(
```

" Name of appearance " & (k + 1) & ": "

& swModel.**MaterialIdName**)

Next

k

Dim xcoord As Double

Dim ycoord As Double

Dim zcoord As Double

```vb
swRenderMaterial.GetCenterPoint2(xcoord, ycoord, zcoord)
Debug.Print(
```

""

)

```vb
Debug.Print(
```

"Texture-based appearance data:"

)

```vb
Debug.Print(
```

"X coordinate of center point: "

& xcoord)

```vb
Debug.Print(
```

"Y coordinate of center point: "

& ycoord)

```vb
Debug.Print(
```

"Z coordinate of center point: "

& zcoord)

```vb
swRenderMaterial.GetUDirection2(xcoord, ycoord, zcoord)
Debug.Print(
```

"X coordinate of U direction: "

& xcoord)

```vb
Debug.Print(
```

"Y coordinate of U direction: "

& ycoord)

```vb
Debug.Print(
```

"Z coordinate of U direction: "

& zcoord)

```vb
swRenderMaterial.GetVDirection2(xcoord, ycoord, zcoord)
Debug.Print(
```

"X coordinate of V direction: "

& xcoord)

```vb
Debug.Print(
```

"Y coordinate of V direction: "

& ycoord)

```vb
Debug.Print(
```

"Z coordinate of V direction: "

& zcoord)

```vb
Debug.Print(
```

""

)

```vb
swModel.ClearSelection2(
```

True

)

```vb
swModel.ForceRebuild3(
```

True

)

```vb
Debug.Print(
```

"Model has an appearance: "

& swModelDocExt.**HasMaterialPropertyValues**)

Dim dispStates As Object

```vb
status = swRenderMaterial.SetLinkedDisplayStates(swDisplayStateOpts_e.swAllDisplayState, displayStateNames)
dispStates = swRenderMaterial.GetLinkedDisplayStates
```

Dim renderMaterials As Object

```vb
renderMaterials = swModelDocExt.GetRenderMaterials2(swDisplayStateOpts_e.swAllDisplayState,
```

Nothing

)

' Examine the display states of the active configuration

' to ensure that the specified appearance was applied to all

' display states

' Continue running the macro after your examination

Stop

' Delete the appearance from the part

```vb
materialID1_ToDelete(0) = materialID1
materialID2_ToDelete(0) = materialID2
swModelDocExt.DeleteDisplayStateSpecificRenderMaterial((materialID1_ToDelete), (materialID2_ToDelete))
swModel.ForceRebuild3(
```

True

)

' Examine the display states of the active configuration

' to ensure that the specified appearance was deleted from all

' display states

' Continue running the macro after your examination

Stop

' Close the part without saving changes

```vb
modelName = swModel.GetTitle
swApp.QuitDoc(modelName)
```

End

Sub

Public swApp As

SldWorks

```vb
End
```

Class
