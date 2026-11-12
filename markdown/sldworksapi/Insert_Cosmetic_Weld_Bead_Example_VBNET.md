---
title: "Insert Cosmetic Weld Bead Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Cosmetic_Weld_Bead_Example_VBNET.htm"
---

# Insert Cosmetic Weld Bead Example (VB.NET)

This example shows how to insert a cosmetic weld bead feature and access an existing cosmetic weld bead feature's properties.

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swFeatureManager As FeatureManager
        Dim swCosmeticWeldBeadFeatureData As CosmeticWeldBeadFeatureData
        Dim swWeldFolder As CosmeticWeldBeadFolder
        Dim swSelectionMgr As SelectionMgr
        Dim swFeature As Feature
        Dim edges() As Object
        Dim status As Boolean

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension

        'Insert Weld Bead2
        status = swModelDocExt.SelectByID2("", "FACE", -0.0344320907599354, 0.0170180000000641, -0.00227566098720899, False, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "FACE", -0.0161637176506133, 0.0503122973344716, -0.0013752238241409, True, 0, Nothing, 0)
        swFeatureManager = swModel.FeatureManager
        swFeature = swFeatureManager.InsertCosmeticWeldBead(0.51)

        swModel.ClearSelection2(True)

        'Get Weld Bead1 and get and set some properties
        status = swModelDocExt.SelectByID2("Weld Bead1", "COSMETIC_WELD", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swFeature = swSelectionMgr.GetSelectedObject6(1, 0)
        swCosmeticWeldBeadFeatureData = swFeature.GetDefinition
        swCosmeticWeldBeadFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print("Weld Bead1 settings: ")
        Debug.Print("   Weld bead size: " & swCosmeticWeldBeadFeatureData.BeadSize * 39.37 & " in")
        Debug.Print("   Tangent propagation? " & swCosmeticWeldBeadFeatureData.TangentPropagation)
        Debug.Print("   Weld sides as defined in swCosmeticWeldBeadSide_e (1 = swCosmeticWeldBeadSide_selection): " & swCosmeticWeldBeadFeatureData.Side)
        Debug.Print("   From/to length properties enabled? " & swCosmeticWeldBeadFeatureData.FromToLength)
        If swCosmeticWeldBeadFeatureData.FromToLength = False Then
            swCosmeticWeldBeadFeatureData.FromToLength = True
        End If
        If swCosmeticWeldBeadFeatureData.FromToLength = True Then
            Debug.Print("   Start weld at: " & swCosmeticWeldBeadFeatureData.FromToStartPoint)
            Debug.Print("   Weld length: " & swCosmeticWeldBeadFeatureData.FromToWeldLength)
            Debug.Print("   Reverse weld? " & swCosmeticWeldBeadFeatureData.FromToReverse)
        End If
        Debug.Print("   Intermittent weld properties enabled? " & swCosmeticWeldBeadFeatureData.IntermittentWeld)
        If swCosmeticWeldBeadFeatureData.IntermittentWeld = False Then
            swCosmeticWeldBeadFeatureData.IntermittentWeld = True
        End If
        If swCosmeticWeldBeadFeatureData.IntermittentWeld = True Then
            If swCosmeticWeldBeadFeatureData.GapOrPitch = True Then
                Debug.Print("   Intermittent gap: " & swCosmeticWeldBeadFeatureData.Gap)
                Debug.Print("   Intermittent weld length: " & swCosmeticWeldBeadFeatureData.IntermittentWeldLength)
            Else
                Debug.Print("   Intermittent pitch: " & swCosmeticWeldBeadFeatureData.Pitch)
                Debug.Print("   Intermittent weld length: " & swCosmeticWeldBeadFeatureData.IntermittentWeldLength)
                Debug.Print("   Stagger welds if welding on both sides? " & swCosmeticWeldBeadFeatureData.Staggered)
            End If
        End If
        edges = swCosmeticWeldBeadFeatureData.GetReferenceEdges
        Debug.Print("   Number of reference edges: " & UBound(edges))

        swWeldFolder = swCosmeticWeldBeadFeatureData.GetWeldBeadFolder

        Debug.Print("Weld Bead1 properties:")
        Debug.Print("   Weld material was: " & swWeldFolder.Material)
        swWeldFolder.Material = "Steel"
        Debug.Print("   Weld material is now: " & swWeldFolder.Material)
        Debug.Print("   Welding cost per unit mass: " & swWeldFolder.CostPerUnitMass)
        Debug.Print("   Weld mass per unit length: " & swWeldFolder.MassPerUnitLength)
        Debug.Print("   Number of weld passes: " & swWeldFolder.NumberOfWeldPasses)
        Debug.Print("   Weld process: " & swWeldFolder.Process)
        Debug.Print("   Welding time per unit length: " & swWeldFolder.TimePerUnitLength)
        Debug.Print("   Total welding cost: $" & swWeldFolder.TotalCost)
        Debug.Print("   Total weld length: " & swWeldFolder.TotalLength)
        Debug.Print("   Total weld mass: " & swWeldFolder.TotalMass & " lb")
        Debug.Print("   Total number of welds: " & swWeldFolder.TotalNumber)
        Debug.Print("   Total welding time: " & swWeldFolder.TotalTime & " sec")

        status = swFeature.ModifyDefinition(swCosmeticWeldBeadFeatureData, swModel, Nothing)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
