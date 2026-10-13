---
title: "Create Holes Using Hole Wizard and Sketch Points Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Holes_Using_Hole_Wizard_and_Sketch_Points_Example_VBNET.htm"
---

# Create Holes Using Hole Wizard and Sketch Points Example (VB.NET)

This example shows how to create holes using the Hole Wizard and sketch points.

```vb
 '---------------------------------------------------------------------------
 ' Problem:
 ' When adding a number of Hole Wizard hole features,
 ' it is often helpful to use a sketch with a number of
 ' sketch points. However,  IFeatureManager::HoleWizard'
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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Function CreateHoleWizardFeature(ByVal swApp As SldWorks, ByVal swModel As ModelDoc2) As Boolean

         Dim swFeatMgr As FeatureManager
         Dim swFeat As Feature
         Dim swWizHole As WizardHoleFeatureData2

         swFeatMgr = swModel.FeatureManager
         swFeat = swFeatMgr.HoleWizard _
                         ( _
                         swWzdGeneralHoleTypes_e.swWzdCounterBore, _
                         swWzdHoleStandards_e.swStandardISO, _
                         swWzdHoleStandardFastenerTypes_e.swStandardISOHexCapScrew, _
                         "M6", _
                         swWzdHoleThreadEndCondition_e.swEndThreadTypeBLIND, _
                         0.0066, _
                         0.02, _
                         0.014547, _
                         0.004, _
                         0.0#, _
                         1.0#, _
                         2.059488517353, _
                         0.0#, _
                         0.0#, _
                         0.0#, _
                         0.0#, _
                         0.0#, _
                         0.0#, _
                         0.0# _
                         )

         ' Hole creation can fail due to geometry conditions
         If swFeat Is Nothing Then
             CreateHoleWizardFeature = False
             Exit Function
         End If

         swWizHole = swFeat.GetDefinition

         Debug.Print("Feature = " + swFeat.Name)
         Debug.Print("  Type                         = " & swWizHole.Type)
         Debug.Print("")
         Debug.Print("  CosmeticThreadType           = " & swWizHole.CosmeticThreadType)
         Debug.Print("  CounterBoreDepth             = " & swWizHole.CounterBoreDepth * 1000.0# & " mm")
         Debug.Print("  CounterBoreDiameter          = " & swWizHole.CounterBoreDiameter * 1000.0# & " mm")
         '1 radian = 180º/p = 57.295779513º or approximately 57.3º
         Debug.Print("  CounterDrillAngle            = " & swWizHole.CounterDrillAngle * 57.3 & " deg")
         Debug.Print("  CounterDrillDepth            = " & swWizHole.CounterDrillDepth * 1000.0# & " mm")
         Debug.Print("  CounterDrillDiameter         = " & swWizHole.CounterDrillDiameter * 1000.0# & " mm")
         Debug.Print("  CounterSinkAngle             = " & swWizHole.CounterSinkAngle * 57.3 & " deg")
         Debug.Print("  CounterSinkDiameter          = " & swWizHole.CounterSinkDiameter * 1000.0# & " mm")
         Debug.Print("  Depth                        = " & swWizHole.Depth * 1000.0# & " mm")
         Debug.Print("  Diameter                     = " & swWizHole.Diameter * 1000.0# & " mm")
         Debug.Print("  DrillAngle                   = " & swWizHole.DrillAngle * 57.3 & " deg")
         Debug.Print("  EndCondition                 = " & swWizHole.EndCondition)
         Debug.Print("  FarCounterSinkAngle          = " & swWizHole.FarCounterSinkAngle * 57.3 & " deg")
         Debug.Print("  FarCounterSinkDiameter       = " & swWizHole.FarCounterSinkDiameter * 1000.0# & " mm")
         Debug.Print("  FastenerSize                 = " & swWizHole.FastenerSize)
         Debug.Print("  FastenerType                 = " & swWizHole.FastenerType2)
         Debug.Print("  HeadClearance                = " & swWizHole.HeadClearance * 1000.0# & " mm")
         Debug.Print("  HeadClearanceType            = " & swWizHole.HeadClearanceType)
         Debug.Print("  HoleDepth                    = " & swWizHole.HoleDepth * 1000.0# & " mm")
         Debug.Print("  HoleDiameter                 = " & swWizHole.HoleDiameter * 1000.0# & " mm")
         Debug.Print("  MajorDiameter                = " & swWizHole.MajorDiameter * 1000.0# & " mm")
         Debug.Print("  MidCounterSinkAngle          = " & swWizHole.MidCounterSinkAngle * 57.3 & " deg")
         Debug.Print("  MidCounterSinkDiameter       = " & swWizHole.MidCounterSinkDiameter * 1000.0# & " mm")
         Debug.Print("  MinorDiameter                = " & swWizHole.MinorDiameter * 1000.0# & " mm")
         Debug.Print("  NearCounterSinkAngle         = " & swWizHole.NearCounterSinkAngle * 57.3 & " deg")
         Debug.Print("  NearCounterSinkDiameter      = " & swWizHole.NearCounterSinkDiameter * 1000.0# & " mm")
         Debug.Print("  Standard                     = " & swWizHole.Standard2)
         Debug.Print("  TapDrillDepth                = " & swWizHole.TapDrillDepth * 1000.0# & " mm")
         Debug.Print("  TapDrillDiameter             = " & swWizHole.TapDrillDiameter * 1000.0# & " mm")
         Debug.Print("  ThreadAngle                  = " & swWizHole.ThreadAngle * 57.3 & " deg")
         Debug.Print("  ThreadDepth                  = " & swWizHole.ThreadDepth * 1000.0# & " mm")
         Debug.Print("  ThreadDiameter               = " & swWizHole.ThreadDiameter * 1000.0# & " mm")
         Debug.Print("  ThruHoleDepth                = " & swWizHole.ThruHoleDepth * 1000.0# & " mm")
         Debug.Print("  ThruHoleDiameter             = " & swWizHole.ThruHoleDiameter * 1000.0# & " mm")
         Debug.Print("  ThruTapDrillDepth            = " & swWizHole.ThruTapDrillDepth * 1000.0# & " mm")
         Debug.Print("  ThruTapDrillDiameter         = " & swWizHole.ThruTapDrillDiameter * 1000.0# & " mm")

         CreateHoleWizardFeature = True

     End Function

     Sub main()

         Dim swMathUtil As MathUtility
         Dim swModel As ModelDoc2
         Dim swSelMgr As SelectionMgr
         Dim swFeat As Feature
         Dim swSketch As Sketch
         Dim vSketchPtArr As Object
         Dim vSketchPt As Object
         Dim swSketchPt As SketchPoint
         Dim swSketchXform As MathTransform
         Dim vPtArr As Object
         Dim swPt As MathPoint
         Dim bRet As Boolean
         Dim nPtData(2) As Double

         swMathUtil = swApp.GetMathUtility
         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swSketch = swFeat.GetSpecificFeature2
         swSketchXform = swSketch.ModelToSketchTransform
         swSketchXform = swSketchXform.Inverse

         vSketchPtArr = swSketch.GetSketchPoints

         For Each vSketchPt In vSketchPtArr

             swSketchPt = vSketchPt
             nPtData(0) = swSketchPt.X
             nPtData(1) = swSketchPt.Y
             nPtData(2) = swSketchPt.Z
             vPtArr = nPtData

             swPt = swMathUtil.CreatePoint(vPtArr)
             swPt = swPt.MultiplyTransform(swSketchXform)

             bRet = swModel.Extension.SelectByID2("", "FACE", swPt.ArrayData(0), swPt.ArrayData(1), swPt.ArrayData(2),  True, 0,  Nothing, 0)

             bRet = CreateHoleWizardFeature(swApp, swModel)

         Next

     End Sub

     Public swApp As SldWorks

 End  Class
```
