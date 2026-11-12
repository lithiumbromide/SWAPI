---
title: "Insert Cosmetic Weld Bead Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Cosmetic_Weld_Bead_Example_VB.htm"
---

# Insert Cosmetic Weld Bead Example (VBA)

This example shows how to insert a cosmetic weld bead feature and access an existing weld bead feature's properties.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\Insert_weld.sldprt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Inserts a fillet weld, Weld Bead2, and adds it to the Weld Folder in
'    the FeatureManager design tree.
' 2. Inspect the Immediate window for Weld Bead1 settings and properties.
' 3. Expand the Weld Folder and 20.08in Fillet Weld(1) folders in the
'    FeatureManager design tree to verify step 1.
'
' NOTE: Because the model is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatureManager As SldWorks.FeatureManager
Dim swCosmeticWeldBeadFeatureData As SldWorks.CosmeticWeldBeadFeatureData
Dim swWeldFolder As SldWorks.CosmeticWeldBeadFolder
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swFeature As SldWorks.Feature
Dim edges As Variant
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
```

```
    'Insert Weld Bead2
    status = swModelDocExt.SelectByID2("", "FACE", -3.44320907599354E-02, 1.70180000000641E-02, -2.27566098720899E-03, False, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", -1.61637176506133E-02, 5.03122973344716E-02, -1.3752238241409E-03, True, 0, Nothing, 0)
    Set swFeatureManager = swModel.FeatureManager
    Set swFeature = swFeatureManager.InsertCosmeticWeldBead(0.51)
```

```
    swModel.ClearSelection2 True
```

```
    'Get Weld Bead1 and get and set some properties
    status = swModelDocExt.SelectByID2("Weld Bead1", "COSMETIC_WELD", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, 0)
    Set swCosmeticWeldBeadFeatureData = swFeature.GetDefinition
    swCosmeticWeldBeadFeatureData.AccessSelections swModel, Nothing
```

```
    Debug.Print "Weld Bead1 settings: "
    Debug.Print "   Weld bead size: " & swCosmeticWeldBeadFeatureData.BeadSize * 39.37 & " in"
    Debug.Print "   Tangent propagation? " & swCosmeticWeldBeadFeatureData.TangentPropagation
    Debug.Print "   Weld sides as defined in swCosmeticWeldBeadSide_e (1 = swCosmeticWeldBeadSide_selection): " & swCosmeticWeldBeadFeatureData.Side
    Debug.Print "   From/to length properties enabled? " & swCosmeticWeldBeadFeatureData.FromToLength
    If swCosmeticWeldBeadFeatureData.FromToLength = False Then
        swCosmeticWeldBeadFeatureData.FromToLength = True
    End If
    If swCosmeticWeldBeadFeatureData.FromToLength = True Then
        Debug.Print "   Start weld at: " & swCosmeticWeldBeadFeatureData.FromToStartPoint
        Debug.Print "   Weld length: " & swCosmeticWeldBeadFeatureData.FromToWeldLength
        Debug.Print "   Reverse weld? " & swCosmeticWeldBeadFeatureData.FromToReverse
    End If
    Debug.Print "   Intermittent weld properties enabled? " & swCosmeticWeldBeadFeatureData.IntermittentWeld
    If swCosmeticWeldBeadFeatureData.IntermittentWeld = False Then
        swCosmeticWeldBeadFeatureData.IntermittentWeld = True
    End If
    If swCosmeticWeldBeadFeatureData.IntermittentWeld = True Then
        If swCosmeticWeldBeadFeatureData.GapOrPitch = True Then
            Debug.Print "   Intermittent gap: " & swCosmeticWeldBeadFeatureData.Gap
            Debug.Print "   Intermittent weld length: " & swCosmeticWeldBeadFeatureData.IntermittentWeldLength
        Else
            Debug.Print "   Intermittent pitch: " & swCosmeticWeldBeadFeatureData.Pitch
            Debug.Print "   Intermittent weld length: " & swCosmeticWeldBeadFeatureData.IntermittentWeldLength
            Debug.Print "   Stagger welds if welding on both sides? " & swCosmeticWeldBeadFeatureData.Staggered
        End If
    End If
    edges = swCosmeticWeldBeadFeatureData.GetReferenceEdges
    Debug.Print "   Number of reference edges: " & UBound(edges)
```

```
    Set swWeldFolder = swCosmeticWeldBeadFeatureData.GetWeldBeadFolder
```

```
    Debug.Print "Weld Bead1 properties:"
    Debug.Print "   Weld material was: " & swWeldFolder.Material
    swWeldFolder.Material = "Steel"
    Debug.Print "   Weld material is now: " & swWeldFolder.Material
    Debug.Print "   Welding cost per unit mass: " & swWeldFolder.CostPerUnitMass
    Debug.Print "   Weld mass per unit length: " & swWeldFolder.MassPerUnitLength
    Debug.Print "   Number of weld passes: " & swWeldFolder.NumberOfWeldPasses
    Debug.Print "   Weld process: " & swWeldFolder.Process
    Debug.Print "   Welding time per unit length: " & swWeldFolder.TimePerUnitLength
    Debug.Print "   Total welding cost: $" & swWeldFolder.TotalCost
    Debug.Print "   Total weld length: " & swWeldFolder.TotalLength
    Debug.Print "   Total weld mass: " & swWeldFolder.TotalMass & " lb"
    Debug.Print "   Total number of welds: " & swWeldFolder.TotalNumber
    Debug.Print "   Total welding time: " & swWeldFolder.TotalTime & " sec"
```

```
    status = swFeature.ModifyDefinition(swCosmeticWeldBeadFeatureData, swModel, Nothing)
```

```
End Sub
```
