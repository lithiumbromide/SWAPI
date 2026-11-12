---
title: "Create Extruded Thin Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Extruded_Thin_Feature_Example_VB.htm"
---

# Create Extruded Thin Feature Example (VBA)

This example shows how to create an extruded thin feature using a variety of parameter values.

```vb
'-----------------------------------------------------------------------------
' Preconditions: None.
'
' Postconditions: When the macro stops, press F5 five more times to create
 ' five different thin extrusion features.
'----------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim myFeature As SldWorks.Feature
 Dim swPart As SldWorks.PartDoc
 Dim nStartCondition As Long
 Dim nEndcondition1 As Long
 Dim nEndcondition2 As Long
 Dim lCase As Long
 Dim dStartOffset As Double
 Dim bFlipOffset As Boolean
 Dim dThickness As Double
 Dim swExtrusionData As SldWorks.ExtrudeFeatureData2
 Dim lThinFeatureType As Long
 Dim lCapEnds As Long
 Dim bValue As Boolean
Dim boolstatus As Boolean
Option Explicit
Sub main()
    Set swApp = Application.SldWorks

    'New model document
     Dim swSheetWidth As Double
     swSheetWidth = 0
     Dim swSheetHeight As Double
     swSheetHeight = 0
     Set Part = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2018\templates\Part.prtdot", 0, swSheetWidth, swSheetHeight)

    Set swPart = Part
     Set Part = swApp.ActiveDoc

    'Set some parameters used for all cases
     nEndcondition1 = swEndCondBlind
     nEndcondition2 = swEndCondBlind
     dThickness = 0.001
     lThinFeatureType = 2 ' Mid-plane
     lCapEnds = 0
    'Create sketch
     boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", -4.75777316877496E-02, 1.30140669704215E-02, 0.016264555537633, False, 0, Nothing, 0)
     Part.SketchManager.InsertSketch True
     Part.ClearSelection2 True
    Dim vSkLines As Variant
     vSkLines = Part.SketchManager.CreateCornerRectangle(-4.72149072628614E-02, 2.51029484316118E-02, 0, 6.72972660081509E-02, -4.56125914055245E-02, 0)
     Part.ClearSelection2 True
     Part.SketchManager.InsertSketch True

    Part.ClearSelection2 True

    For lCase = 1 To 6
        Part.ClearSelection2 True

        bValue = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)

        Select Case lCase
             Case 1
                 nStartCondition = swStartSketchPlane
                 dStartOffset = 0#
                 bFlipOffset = False

            Case 2
                 nStartCondition = swStartOffset
                 dStartOffset = 0#
                 bFlipOffset = False

            Case 3
                 nStartCondition = swStartOffset
                 dStartOffset = 0#
                 bFlipOffset = True

            Case 4
                 nStartCondition = swStartOffset
                 dStartOffset = 0.01
                 bFlipOffset = False

            Case 5
                 nStartCondition = swStartOffset
                 dStartOffset = 0.01
                 bFlipOffset = True

            Case 6
                 nStartCondition = swStartVertex
                 dStartOffset = 0#
                 bFlipOffset = True
                 dThickness = 0.01

            bValue = Part.Extension.SelectByID2("", "VERTEX", -0.05999251028807, 0.05489880658436, 0, True, 0, Nothing, 0)

        End Select

        Set myFeature = Part.FeatureManager.FeatureExtrusionThin2(True, False, False, nEndcondition1, nEndcondition2, 0.00254, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, dThickness, 0.00254, 0.00254, lThinFeatureType, lCapEnds, False, 0.005, True, True, nStartCondition, dStartOffset, bFlipOffset)

        Debug.Print myFeature.Name & " [" & myFeature.GetTypeName & "]"

        Set swExtrusionData = myFeature.GetDefinition

        bValue = swExtrusionData.AccessSelections(Part, Nothing)

        If (swExtrusionData.IsThinFeature = False) Then
             Debug.Print "ERROR: Must be a thin feature."
         End If

        Select Case swExtrusionData.FromType

            Case SwConst.swExtrudeFrom_e.swExtrudeFrom_SketchPlane

                Debug.Print "  from: sketchplane"

            Case SwConst.swExtrudeFrom_e.swExtrudeFrom_Offset

                Debug.Print "  from: offset"

                Debug.Print "    distance = " & swExtrusionData.FromOffsetDistance
                 Debug.Print "    reverse  = " & swExtrusionData.FromOffsetReverse

            Case SwConst.swExtrudeFrom_e.swExtrudeFrom_SurfaceFacePlane

                Debug.Print "  from: surface"

            Case SwConst.swExtrudeFrom_e.swExtrudeFrom_Vertex

                Debug.Print "  from: vertex"

        End Select

        swExtrusionData.ReleaseSelectionAccess

        ' Examine the feature
         Stop
         ' Now delete the feature
         ' The sketch remains, so that you can select it again
         bValue = myFeature.Select2(True, 0)

        bValue = Part.Extension.DeleteSelection2(swDelete_Children)

    Next lCase
End Sub
```
