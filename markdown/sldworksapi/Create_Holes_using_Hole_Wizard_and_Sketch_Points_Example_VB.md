---
title: "Create Holes Using Hole Wizard and Sketch Points Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Holes_using_Hole_Wizard_and_Sketch_Points_Example_VB.htm"
---

# Create Holes Using Hole Wizard and Sketch Points Example (VBA)

This example shows how to create holes using the Hole Wizard and sketch points.

```vb
 '---------------------------------------------------------------------------
 ' Problem:
 ' When adding a number of Hole Wizard hole features,
 ' it is often helpful to use a sketch with a number of
 ' sketch points. However, IFeatureManager::HoleWizard
 ' requires selection points to be on a face and in the
 ' space of the model.
 '
 ' This example shows how to transform a sketch point
 ' from the space of a sketch to the space of the model.
 '
 ' Preconditions:
 ' 1. Open a part or assembly document.
 ' 2. Fully resolve the assembly.
 ' 3. Select a sketch with at least one sketch point.
 '
 ' Postconditions:
 ' 1. Inserts counterbore hole features at each sketch point.
 ' 2. Inspect the Immediate window.
 '
 ' NOTES:
 ' 1. Hole creation can fail due to geometry conditions.
 ' 2. To access:
 '    * IWizardHoleFeatureData2::Face
 '    * IWizardHoleFeatureData2::Vertex
 '    * IWizardHoleFeatureData2::GetEndConditionReference
 '    the feature must be rolled back with a call to
 '    IWizardHoleFeatureData2::AccessSelections
 '    because these are geometric entities that
 '    can be consumed by subsequent features.
 '---------------------------------------------------------------------------
Option Explicit
Function CreateHoleWizardFeature(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2) As Boolean
    Dim swFeatMgr               As SldWorks.FeatureManager
     Dim swFeat                  As SldWorks.Feature
     Dim swWizHole               As SldWorks.WizardHoleFeatureData2
    Set swFeatMgr = swModel.FeatureManager
     Set swFeat = swFeatMgr.HoleWizard _
                     ( _
                     swWzdCounterBore, _
                     swStandardISO, _
                     swStandardISOHexCapScrew, _
                     "M6", _
                     swEndThreadTypeBLIND, _
                     0.0066, _
                     0.02, _
                     0.014547, _
                     0.004, _
                     0#, _
                     1#, _
                     2.059488517353, _
                     0#, _
                     0#, _
                     0#, _
                     0#, _
                     0#, _
                     0#, _
                     0# _
                     )

     ' Hole creation can fail due to geometry conditions
     If swFeat Is Nothing Then
         CreateHoleWizardFeature = False
         Exit Function
     End If
    Set swWizHole = swFeat.GetDefinition
    Debug.Print "Feature = " + swFeat.Name
     Debug.Print "  Type                         = " & swWizHole.Type
     Debug.Print ""
     Debug.Print "  CosmeticThreadType           = " & swWizHole.CosmeticThreadType
     Debug.Print "  CounterBoreDepth             = " & swWizHole.CounterBoreDepth * 1000# & " mm"
     Debug.Print "  CounterBoreDiameter          = " & swWizHole.CounterBoreDiameter * 1000# & " mm"
     '1 radian = 180º/p = 57.295779513º or approximately 57.3º
     Debug.Print "  CounterDrillAngle            = " & swWizHole.CounterDrillAngle * 57.3 & " deg"
     Debug.Print "  CounterDrillDepth            = " & swWizHole.CounterDrillDepth * 1000# & " mm"
     Debug.Print "  CounterDrillDiameter         = " & swWizHole.CounterDrillDiameter * 1000# & " mm"
     Debug.Print "  CounterSinkAngle             = " & swWizHole.CounterSinkAngle * 57.3 & " deg"
     Debug.Print "  CounterSinkDiameter          = " & swWizHole.CounterSinkDiameter * 1000# & " mm"
     Debug.Print "  Depth                        = " & swWizHole.Depth * 1000# & " mm"
     Debug.Print "  Diameter                     = " & swWizHole.Diameter * 1000# & " mm"
     Debug.Print "  DrillAngle                   = " & swWizHole.DrillAngle * 57.3 & " deg"
     Debug.Print "  EndCondition                 = " & swWizHole.EndCondition
     Debug.Print "  FarCounterSinkAngle          = " & swWizHole.FarCounterSinkAngle * 57.3 & " deg"
     Debug.Print "  FarCounterSinkDiameter       = " & swWizHole.FarCounterSinkDiameter * 1000# & " mm"
     Debug.Print "  FastenerSize                 = " & swWizHole.FastenerSize
     Debug.Print "  FastenerType                 = " & swWizHole.FastenerType2
     Debug.Print "  HeadClearance                = " & swWizHole.HeadClearance * 1000# & " mm"
     Debug.Print "  HeadClearanceType            = " & swWizHole.HeadClearanceType
     Debug.Print "  HoleDepth                    = " & swWizHole.HoleDepth * 1000# & " mm"
     Debug.Print "  HoleDiameter                 = " & swWizHole.HoleDiameter * 1000# & " mm"
     Debug.Print "  MajorDiameter                = " & swWizHole.MajorDiameter * 1000# & " mm"
     Debug.Print "  MidCounterSinkAngle          = " & swWizHole.MidCounterSinkAngle * 57.3 & " deg"
     Debug.Print "  MidCounterSinkDiameter       = " & swWizHole.MidCounterSinkDiameter * 1000# & " mm"
     Debug.Print "  MinorDiameter                = " & swWizHole.MinorDiameter * 1000# & " mm"
     Debug.Print "  NearCounterSinkAngle         = " & swWizHole.NearCounterSinkAngle * 57.3 & " deg"
     Debug.Print "  NearCounterSinkDiameter      = " & swWizHole.NearCounterSinkDiameter * 1000# & " mm"
     Debug.Print "  Standard                     = " & swWizHole.Standard2
     Debug.Print "  TapDrillDepth                = " & swWizHole.TapDrillDepth * 1000# & " mm"
     Debug.Print "  TapDrillDiameter             = " & swWizHole.TapDrillDiameter * 1000# & " mm"
     Debug.Print "  ThreadAngle                  = " & swWizHole.ThreadAngle * 57.3 & " deg"
     Debug.Print "  ThreadDepth                  = " & swWizHole.ThreadDepth * 1000# & " mm"
     Debug.Print "  ThreadDiameter               = " & swWizHole.ThreadDiameter * 1000# & " mm"
     Debug.Print "  ThruHoleDepth                = " & swWizHole.ThruHoleDepth * 1000# & " mm"
     Debug.Print "  ThruHoleDiameter             = " & swWizHole.ThruHoleDiameter * 1000# & " mm"
     Debug.Print "  ThruTapDrillDepth            = " & swWizHole.ThruTapDrillDepth * 1000# & " mm"
     Debug.Print "  ThruTapDrillDiameter         = " & swWizHole.ThruTapDrillDiameter * 1000# & " mm"

    CreateHoleWizardFeature = True

End Function
Sub main()
    Dim swApp                   As SldWorks.SldWorks
     Dim swMathUtil              As SldWorks.MathUtility
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swSelMgr                As SldWorks.SelectionMgr
     Dim swFeat                  As SldWorks.Feature
     Dim swSketch                As SldWorks.Sketch
     Dim vSketchPtArr            As Variant
     Dim vSketchPt               As Variant
     Dim swSketchPt              As SldWorks.SketchPoint
     Dim swSketchXform           As SldWorks.MathTransform
     Dim vPtArr                  As Variant
     Dim swPt                    As SldWorks.MathPoint
     Dim bRet                    As Boolean
     Dim nPtData(2) As Double
    Set swApp = Application.SldWorks
     Set swMathUtil = swApp.GetMathUtility
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swSketch = swFeat.GetSpecificFeature2
     Set swSketchXform = swSketch.ModelToSketchTransform
     Set swSketchXform = swSketchXform.Inverse
    vSketchPtArr = swSketch.GetSketchPoints
    For Each vSketchPt In vSketchPtArr

        Set swSketchPt = vSketchPt
         nPtData(0) = swSketchPt.X
         nPtData(1) = swSketchPt.Y
         nPtData(2) = swSketchPt.Z
         vPtArr = nPtData
        Set swPt = swMathUtil.CreatePoint(vPtArr)
         Set swPt = swPt.MultiplyTransform(swSketchXform)
        bRet = swModel.Extension.SelectByID2("", "FACE", swPt.ArrayData(0), swPt.ArrayData(1), swPt.ArrayData(2), True, 0, Nothing, 0)

        bRet = CreateHoleWizardFeature(swApp, swModel)
    Next
End Sub
```
