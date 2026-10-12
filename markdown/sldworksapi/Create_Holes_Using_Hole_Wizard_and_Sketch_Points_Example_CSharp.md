---
title: "Create Holes Using Hole Wizard and Sketch Points Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Holes_Using_Hole_Wizard_and_Sketch_Points_Example_CSharp.htm"
---

# Create Holes Using Hole Wizard and Sketch Points Example (C#)

This example shows how to create holes using the Hole Wizard and sketch points.

```vb
 //---------------------------------------------------------------------------
 // Problem:
 // When adding a number of Hole Wizard hole features,
 // it is often helpful to use a sketch with a number of
 // sketch points. However, IFeatureManager::HoleWizard
 // requires selection points to be on a face and in the
 // space of the model.
 //
 // This example shows how to transform a sketch point
 // from the space of a sketch to the space of the model.
 //
 // Preconditions:
 // 1. Open a part or assembly document.
 // 2. Fully resolve the assembly.
 // 3. Select a sketch with at least one sketch point.
 //
 // Postconditions:
 // 1. Inserts counterbore hole features at each sketch point.
 // 2. Inspect the Immediate window.
 //
 // NOTES:
 // 1. Hole creation can fail due to geometry conditions.
 // 2. To access:
 //    * IWizardHoleFeatureData2::Face
 //    * IWizardHoleFeatureData2::Vertex
 //    * IWizardHoleFeatureData2::GetEndConditionReference
 //    the feature must be rolled back with a call to
 //    IWizardHoleFeatureData2::AccessSelections
 //    because these are geometric entities that
 //    can be consumed by subsequent features.
 //---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace WizardHoleFeatureData_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public bool CreateHoleWizardFeature(SldWorks swApp, ModelDoc2 swModel)
         {
             bool functionReturnValue = false;

             FeatureManager swFeatMgr = default(FeatureManager);
             Feature swFeat = default(Feature);
             WizardHoleFeatureData2 swWizHole = default(WizardHoleFeatureData2);

             swFeatMgr = swModel.FeatureManager;
             swFeat = swFeatMgr.HoleWizard((int)swWzdGeneralHoleTypes_e.swWzdCounterBore, (int)swWzdHoleStandards_e.swStandardISO, (int)swWzdHoleStandardFastenerTypes_e.swStandardISOHexCapScrew, "M6", (int)swWzdHoleThreadEndCondition_e.swEndThreadTypeBLIND, 0.0066, 0.02, 0.014547, 0.004, 0.0,
             1.0, 2.059488517353, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0);

             // Hole creation can fail due to geometry conditions
             if (swFeat == null)
             {
                 functionReturnValue = false;
                 return functionReturnValue;
             }

             swWizHole = (WizardHoleFeatureData2)swFeat.GetDefinition();

             Debug.Print("Feature = " + swFeat.Name);
             Debug.Print("  Type                         = " + swWizHole.Type);
             Debug.Print("");
             Debug.Print("  CosmeticThreadType           = " + swWizHole.CosmeticThreadType);
             Debug.Print("  CounterBoreDepth             = " + swWizHole.CounterBoreDepth * 1000.0 + " mm");
             Debug.Print("  CounterBoreDiameter          = " + swWizHole.CounterBoreDiameter * 1000.0 + " mm");
             //1 radian = 180º/p = 57.295779513º or approximately 57.3º
             Debug.Print("  CounterDrillAngle            = " + swWizHole.CounterDrillAngle * 57.3 + " deg");
             Debug.Print("  CounterDrillDepth            = " + swWizHole.CounterDrillDepth * 1000.0 + " mm");
             Debug.Print("  CounterDrillDiameter         = " + swWizHole.CounterDrillDiameter * 1000.0 + " mm");
             Debug.Print("  CounterSinkAngle             = " + swWizHole.CounterSinkAngle * 57.3 + " deg");
             Debug.Print("  CounterSinkDiameter          = " + swWizHole.CounterSinkDiameter * 1000.0 + " mm");
             Debug.Print("  Depth                        = " + swWizHole.Depth * 1000.0 +  " mm");
             Debug.Print("  Diameter                     = " + swWizHole.Diameter * 1000.0 +  " mm");
             Debug.Print("  DrillAngle                   = " + swWizHole.DrillAngle * 57.3 +  " deg");
             Debug.Print("  EndCondition                 = " + swWizHole.EndCondition);
             Debug.Print("  FarCounterSinkAngle          = " + swWizHole.FarCounterSinkAngle * 57.3 + " deg");
             Debug.Print("  FarCounterSinkDiameter       = " + swWizHole.FarCounterSinkDiameter * 1000.0 + " mm");
             Debug.Print("  FastenerSize                 = " + swWizHole.FastenerSize);
             Debug.Print("  FastenerType                 = " + swWizHole.FastenerType2);
             Debug.Print("  HeadClearance                = " + swWizHole.HeadClearance * 1000.0 + " mm");
             Debug.Print("  HeadClearanceType            = " + swWizHole.HeadClearanceType);
             Debug.Print("  HoleDepth                    = " + swWizHole.HoleDepth * 1000.0 +  " mm");
             Debug.Print("  HoleDiameter                 = " + swWizHole.HoleDiameter * 1000.0 + " mm");
             Debug.Print("  MajorDiameter                = " + swWizHole.MajorDiameter * 1000.0 + " mm");
             Debug.Print("  MidCounterSinkAngle          = " + swWizHole.MidCounterSinkAngle * 57.3 + " deg");
             Debug.Print("  MidCounterSinkDiameter       = " + swWizHole.MidCounterSinkDiameter * 1000.0 + " mm");
             Debug.Print("  MinorDiameter                = " + swWizHole.MinorDiameter * 1000.0 + " mm");
             Debug.Print("  NearCounterSinkAngle         = " + swWizHole.NearCounterSinkAngle * 57.3 + " deg");
             Debug.Print("  NearCounterSinkDiameter      = " + swWizHole.NearCounterSinkDiameter * 1000.0 + " mm");
             Debug.Print("  Standard                     = " + swWizHole.Standard2);
             Debug.Print("  TapDrillDepth                = " + swWizHole.TapDrillDepth * 1000.0 + " mm");
             Debug.Print("  TapDrillDiameter             = " + swWizHole.TapDrillDiameter * 1000.0 + " mm");
             Debug.Print("  ThreadAngle                  = " + swWizHole.ThreadAngle * 57.3 +  " deg");
             Debug.Print("  ThreadDepth                  = " + swWizHole.ThreadDepth * 1000.0 +  " mm");
             Debug.Print("  ThreadDiameter               = " + swWizHole.ThreadDiameter * 1000.0 + " mm");
             Debug.Print("  ThruHoleDepth                = " + swWizHole.ThruHoleDepth * 1000.0 + " mm");
             Debug.Print("  ThruHoleDiameter             = " + swWizHole.ThruHoleDiameter * 1000.0 + " mm");
             Debug.Print("  ThruTapDrillDepth            = " + swWizHole.ThruTapDrillDepth * 1000.0 + " mm");
             Debug.Print("  ThruTapDrillDiameter         = " + swWizHole.ThruTapDrillDiameter * 1000.0 + " mm");

             functionReturnValue = true;
             return functionReturnValue;

         }

         public void Main()
         {
             MathUtility swMathUtil = default(MathUtility);
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Feature swFeat = default(Feature);
             Sketch swSketch = default(Sketch);
             object[] vSketchPtArr = null;
             object vSketchPt = null;
             SketchPoint swSketchPt = default(SketchPoint);
             MathTransform swSketchXform = default(MathTransform);
             object vPtArr = null;
             MathPoint swPt = default(MathPoint);
             bool bRet = false;
             double[] nPtData = new double[3];

             swMathUtil = (MathUtility)swApp.GetMathUtility();
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);
             swSketch = (Sketch)swFeat.GetSpecificFeature2();
             swSketchXform = swSketch.ModelToSketchTransform;
             swSketchXform = (MathTransform)swSketchXform.Inverse();

             vSketchPtArr = (object[])swSketch.GetSketchPoints();

             foreach (object vSketchPt_loopVariable in vSketchPtArr)
             {
                 vSketchPt = vSketchPt_loopVariable;
                 swSketchPt = (SketchPoint)vSketchPt;
                 nPtData[0] = swSketchPt.X;
                 nPtData[1] = swSketchPt.Y;
                 nPtData[2] = swSketchPt.Z;
                 vPtArr = nPtData;

                 swPt = (MathPoint)swMathUtil.CreatePoint(vPtArr);
                 swPt = (MathPoint)swPt.MultiplyTransform(swSketchXform);

                 bRet = swModel.Extension.SelectByID2("", "FACE", ((double[])swPt.ArrayData)[0], ((double[])swPt.ArrayData)[1], ((double[])swPt.ArrayData)[2], true, 0, null, 0);
                 bRet = CreateHoleWizardFeature(swApp, swModel);

             }
         }

         public SldWorks swApp;

     }

 }
```
