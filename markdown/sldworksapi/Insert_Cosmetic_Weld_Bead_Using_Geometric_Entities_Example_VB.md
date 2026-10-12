---
title: "Insert Cosmetic Weld Bead Using Geometric Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Cosmetic_Weld_Bead_Using_Geometric_Entities_Example_VB.htm"
---

# Insert Cosmetic Weld Bead Using Geometric Entities Example (VBA)

This example shows how to insert a cosmetic weld bead using geometric entities.

```
'----------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a cosmetic weld bead using the
'    selected geometric entities (i.e., faces).
' 2. To verify, examine the graphics area and
'    expand the Weld Folder and its subfolder
'    in the FeatureManager design tree.
' 3. Examine the Immediate window.
'
' NOTE: Because this part document is used elsewhere,
' do not save any changes to it.
'-----------------------------------------------
Option Explicit
```

```
Dim SwApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatureMgr as SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim swSelMgr As SldWorks.SelectionMgr
Dim swCosmeticWeldBeadFeatureData As SldWorks.CosmeticWeldBeadFeatureData
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
Dim entityType As Long
```

```
Sub main()
```

```
    Set SwApp = Application.SldWorks
    'Open model document
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\driveworksxpress\leg.sldprt"
    Set swModel = SwApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Select the faces
    Set swModelDocExt = swModel.Extension
    'From face
    status = swModelDocExt.SelectByID2("", "FACE", 0.447611268878973, 0.185506718400291, 6.76112086262037E-03, True, 4, Nothing, 0)
    'To face
    status = swModelDocExt.SelectByID2("", "FACE", 0.567647499089958, 8.88999999998532E-02, 2.08831790428121E-03, True, 8, Nothing, 0)
```

```
    Set swSelMgr = swModel.SelectionManager
    Dim weldFromFace(0) As SldWorks.Face2
    Dim weldFromArray As Variant
    Set weldFromFace(0) = swSelMgr.GetSelectedObject6(1, 4)
    weldFromArray = weldFromFace
```

```
    Dim weldToFace(0) As SldWorks.Face2
    Dim weldToArray As Variant
    Set weldToFace(0) = swSelMgr.GetSelectedObject6(1, 8)
    weldToArray = weldToFace
```

```
    'Create cosmetic weld bead using the selected faces
    Dim weldObjs  As Variant
    Set swFeatureMgr = swModel.FeatureManager
    weldObjs = swFeatureMgr.InsertCosmeticWeldBead2(0, weldFromArray, weldToArray, 15 / 1000)
```

```
    'Get the weld-from and weld-to entities and their types
    status = swModelDocExt.SelectByID2("Weld Bead1", "COSMETIC_WELD", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeature = swSelMgr.GetSelectedObject6(1, -1)
    Set swCosmeticWeldBeadFeatureData = swFeature.GetDefinition
    swCosmeticWeldBeadFeatureData.AccessSelections swModel, Nothing
    Debug.Print swFeature.Name
    weldObjs = swCosmeticWeldBeadFeatureData.GetEntitiesWeldFrom(entityType)
    Debug.Print "  Weld-from type: " & entityType
    weldObjs = swCosmeticWeldBeadFeatureData.GetEntitiesWeldTo(entityType)
    Debug.Print "  Weld-to type:   " & entityType
    swCosmeticWeldBeadFeatureData.ReleaseSelectionAccess
```

```
    swModel.ClearSelection2 True
```

```
End Sub
```
