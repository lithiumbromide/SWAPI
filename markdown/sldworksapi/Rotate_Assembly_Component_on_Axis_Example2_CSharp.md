---
title: "Rotate Assembly Component on Axis Using IDragOperator::DragAsUI Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_Assembly_Component_on_Axis_Example2_CSharp.htm"
---

# Rotate Assembly Component on Axis Using IDragOperator::DragAsUI Example (C#)

This example shows how to rotate an assembly component about an assembly axis using IDragOperator::DragAsUI.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Assembly document is open.
 // 2. Component in the assembly document is selected.
 //
 // Postconditions: Transform matrix is set.
 //----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;
 namespace DragOperatorAddComponent_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         const double PI = 3.14159;
         const double RadPerDeg = PI / 180.0;

         //   DragOperator::TransformType
         //       Translation     0
         //       Transform is translation-only.
         //
         //       Axial rotation  1
         //       Transform is rotation-only.
         //
         //       General         2
         //       Transform can be translation, rotation, or both.
         //
         //   DragOperator::DragMode
         //       Minimum Move    0
         //       Move smallest number of geometries.
         //
         //       Maximum Move    1
         //       Move geometries rigidly if possible.
         //
         //       Relaxation      2
         //       Solve geometries using relaxation.

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             AssemblyDoc swAssy = default(AssemblyDoc);
             DragOperator swDragOp = default(DragOperator);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Component2[] swComp = new Component2[2];
             object vComp = null;
             MathTransform swXform = default(MathTransform);
             MathUtility swMathUtil = default(MathUtility);
             MathPoint swOriginPt = default(MathPoint);
             MathVector swX_Axis = default(MathVector);
             double[] nPts = new double[3];
             object vData = null;
             int i = 0;
             bool bRet = false;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swAssy = (AssemblyDoc)swModel;
             swDragOp = (DragOperator)swAssy.GetDragOperator();
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swComp[0] = (Component2)swSelMgr.GetSelectedObjectsComponent(1);
             swComp[1] = (Component2)swSelMgr.GetSelectedObjectsComponent(2);
             swMathUtil = (MathUtility)swApp.GetMathUtility();

             vComp = swComp;

             nPts[0] = 0.0;
             nPts[1] = 0.0;
             nPts[2] = 0.0;

             vData = nPts;

             swOriginPt = (MathPoint)swMathUtil.CreatePoint(vData);

             nPts[0] = 1.0;
             nPts[1] = 0.0;
             nPts[2] = 0.0;
             vData = nPts;

             swX_Axis = (MathVector)swMathUtil.CreateVector(vData);

             // This is an incremental rotation,
             // so angle is always the same.
             swXform = (MathTransform)swMathUtil.CreateTransformRotateAxis(swOriginPt, swX_Axis, 1.0 * RadPerDeg);

             bRet = swDragOp.AddComponent(swComp[0],  false);
             Debug.Assert(bRet);

             swDragOp.DynamicClearanceEnabled =  false;

             // Axial rotation
             swDragOp.TransformType = 1;

             // Solve by relaxation
             swDragOp.DragMode = 2;

             bRet = swDragOp.BeginDrag();
             Debug.Assert(bRet);

             for (i = 0; i <= 500; i++)
             {
                 bRet = swDragOp.DragAsUI(swXform);
             }

             bRet = swDragOp.EndDrag();
             Debug.Assert(bRet);

         }

         public SldWorks swApp;

     }

 }
```
