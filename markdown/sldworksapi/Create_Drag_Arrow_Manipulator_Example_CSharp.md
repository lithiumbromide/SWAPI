---
title: "Create Drag Arrow Manipulator Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Drag_Arrow_Manipulator_Example_CSharp.htm"
---

# Create Drag Arrow Manipulator Example (C#)

This example shows how to create a drag arrow manipulator, which is called a handle in the user interface.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part or assembly and select a face.
 // 2. De-select Tools > Options > Stop VSTA debugger on macro exit.
 // 3. Select Project > Add Reference > .NET > SolidWorks.Interop.swpublished.
 // 4. Rename the namespace to match the name of your C# project.
 // 5. Open an Immediate window.
 //
 // Postconditions:
 // 1. A unidirectional drag arrow manipulator or handle is created on the selected face.
 // 2. Drag the handle to another location. The first time you drag the handle,
 //    IDragArrowManipulator::FixedLength is set to true,
 //    and the origin is moved in the direction of the drag. For second and
 //    subsequent drags, IDragArrowManipulator::FixedLength is set to false,
 //    and the origin is not changed.
 // 3. When you drag the handle a ruler displays.
 //    IDragArrowManipulator::ShowRuler is true.
 // 4. When you drag the handle past length = 0, the handle flips direction.
 //    IDragArrowManipulator::AllowFlip is true.
 // 5. Inspect the Immediate window.
 //--------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.swpublished;
 using System;
 using System.Runtime;
 using System.Diagnostics;
 namespace CreateDragArrow_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         Manipulator swManip;
         DragArrowManipulator swDrag;
         SwManHandler2 swDragHdlr = new SwManHandler2();

         public void Main()
         {

             Face2 swFace;
             MathUtility swMathUtil = default(MathUtility);
             ModelDoc2 swModel = default(ModelDoc2);
             ModelViewManager swModViewMgr = default(ModelViewManager);
             SelectionMgr swSelMgr = default(SelectionMgr);
             object vPickPt = null;
             MathPoint swPickPt = default(MathPoint);

             swMathUtil = (MathUtility)swApp.GetMathUtility();
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;
             swFace = (Face2)swSelMgr.GetSelectedObject6(1, 0);

             double[] nVector = new double[3];
             object vVector = null;
             nVector[0] = 0;
             nVector[1] = 1;
             nVector[2] = 0;
             vVector = nVector;

             MathVector swN = default(MathVector);
             swN = (MathVector)swMathUtil.CreateVector((vVector));

             vPickPt = swSelMgr.GetSelectionPoint2(1, -1);
             swPickPt = (MathPoint)swMathUtil.CreatePoint((vPickPt));
             swModViewMgr = swModel.ModelViewManager;

             swManip = swModViewMgr.CreateManipulator((int)swManipulatorType_e.swDragArrowManipulator, swDragHdlr);
             swDrag = (DragArrowManipulator)swManip.GetSpecificManipulator();

             swDrag.AllowFlip =  true;
             swDrag.ShowRuler =  true;
             swDrag.ShowOppositeDirection =  true;
             swDrag.Length = 0.02;
             swDrag.Direction = swN;
             swDrag.LengthOppositeDirection = 0.01;
             swDrag.Origin = swPickPt;
             swManip.Show(swModel);
             swDrag.Update();

             MathPoint origin = default(MathPoint);
             origin = swDrag.Origin;

             object pt = null;
             pt = origin.ArrayData;

         }
         public SldWorks swApp;
     }
     [System.Runtime.InteropServices.ComVisible(true)]
     public class SwManHandler2 : SwManipulatorHandler2
     {
         int doneonce;

         const int lenFact = 1;
         private bool SwManipulatorHandler2_OnHandleLmbSelected(object pManipulator)
         {

             Debug.Print("SwManipulatorHandler2_OnHandleLmbSelected");
             return true;

         }
          bool ISwManipulatorHandler2.OnHandleLmbSelected(object pManipulator)
         {
             return SwManipulatorHandler2_OnHandleLmbSelected(pManipulator);
         }

         private bool SwManipulatorHandler2_OnDelete(object pManipulator)
         {

             Debug.Print("SwManipulatorHandler2_OnDelete");
             return true;

         }
          bool ISwManipulatorHandler2.OnDelete(object pManipulator)
         {
             return SwManipulatorHandler2_OnDelete(pManipulator);
         }

         private void SwManipulatorHandler2_OnDirectionFlipped(object pManipulator)
         {

             Debug.Print("SwManipulatorHandler2_OnDirectionFlipped");

         }
          void ISwManipulatorHandler2.OnDirectionFlipped(object pManipulator)
         {
             SwManipulatorHandler2_OnDirectionFlipped(pManipulator);
         }

         private bool SwManipulatorHandler2_OnDoubleValueChanged(object pManipulator, int Id, ref double Value)
         {

             doneonce = doneonce + 1;
             Debug.Print("SwManipulatorHandler2_OnDoubleValueChanged");

             Debug.Print("  ID               = " + Id);

             Debug.Print("  Value            = " + Value);
             DragArrowManipulator swTmpManipulator = default(DragArrowManipulator);
             swTmpManipulator = (DragArrowManipulator)pManipulator;
             //Update origin
             MathPoint swMathPoint = default(MathPoint);
             swMathPoint = swTmpManipulator.Origin;
             double[] varMathPt = null;
             varMathPt = (double[])swMathPoint.ArrayData;
             varMathPt[1] = varMathPt[1] + lenFact / 1000;
             swMathPoint.ArrayData = varMathPt;
             if ((doneonce == 1))
             {
                 swTmpManipulator.FixedLength =  true;
             }
             swTmpManipulator.Origin = swMathPoint;

             swTmpManipulator.Update();
             return true;
         }
          bool ISwManipulatorHandler2.OnDoubleValueChanged(object pManipulator, int Id, ref double Value)
         {
             return SwManipulatorHandler2_OnDoubleValueChanged(pManipulator, Id,  ref Value);
         }

         private void SwManipulatorHandler2_OnEndDrag(object pManipulator, int handleIndex)
         {
             DragArrowManipulator swTmpManipulator = default(DragArrowManipulator);
             swTmpManipulator = (DragArrowManipulator)pManipulator;
             swTmpManipulator.FixedLength =  false;
             doneonce = doneonce + 1;
             Debug.Print("SwManipulatorHandler2_OnEndDrag");

             Debug.Print("  HandleIndex      = " + handleIndex);

             if ((handleIndex == (int)swDragArrowManipulatorOptions_e.swDragArrowManipulatorDirection2))
             {
                 Debug.Print(" Direction1");

             }
             else
             {
                 Debug.Print(" Direction2");

             }

         }
          void ISwManipulatorHandler2.OnEndDrag(object pManipulator, int handleIndex)
         {
             SwManipulatorHandler2_OnEndDrag(pManipulator, handleIndex);
         }

         private void SwManipulatorHandler2_OnEndNoDrag(object pManipulator, int handleIndex)
         {

             Debug.Print("SwManipulatorHandler2_OnEndNoDrag");

         }
          void ISwManipulatorHandler2.OnEndNoDrag(object pManipulator, int handleIndex)
         {
             SwManipulatorHandler2_OnEndNoDrag(pManipulator, handleIndex);
         }

         private void SwManipulatorHandler2_OnHandleRmbSelected(object pManipulator, int handleIndex)
         {
             Debug.Print("SwManipulatorHandler2_OnHandleRmbSelected");

             Debug.Print("  handleIndex      = " + handleIndex);

         }
          void ISwManipulatorHandler2.OnHandleRmbSelected(object pManipulator, int handleIndex)
         {
             SwManipulatorHandler2_OnHandleRmbSelected(pManipulator, handleIndex);
         }

         private void SwManipulatorHandler2_OnHandleSelected(object pManipulator, int handleIndex)
         {
             Debug.Print("SwManipulatorHandler2_OnHandleSelected");

             Debug.Print("  HandleIndex      = " + handleIndex);

         }
          void ISwManipulatorHandler2.OnHandleSelected(object pManipulator, int handleIndex)
         {
             SwManipulatorHandler2_OnHandleSelected(pManipulator, handleIndex);
         }

         private void SwManipulatorHandler2_OnItemSetFocus(object pManipulator, int Id)
         {

             Debug.Print("SwManipulatorHandler2_OnItemSetFocus");

             Debug.Print("  ID               = " + Id);

         }
          void ISwManipulatorHandler2.OnItemSetFocus(object pManipulator, int Id)
         {
             SwManipulatorHandler2_OnItemSetFocus(pManipulator, Id);
         }

         private bool SwManipulatorHandler2_OnStringValueChanged(object pManipulator, int Id, ref string Value)
         {

             Debug.Print("SwManipulatorHandler2_OnStringValueChanged");

             Debug.Print("  ID               = " + Id);

             Debug.Print("  Value            = " + Value);
             return true;

         }
          bool ISwManipulatorHandler2.OnStringValueChanged(object pManipulator, int Id, ref string Value)
         {
             return SwManipulatorHandler2_OnStringValueChanged(pManipulator, Id,  ref Value);
         }

         private void SwManipulatorHandler2_OnUpdateDrag(object pManipulator, int handleIndex, object newPosMathPt)
         {
             Debug.Print("SwManipulatorHandler2_OnUpdateDrag");

             Debug.Print("  HandleIndex      = " + handleIndex);

         }
          void ISwManipulatorHandler2.OnUpdateDrag(object pManipulator, int handleIndex, object newPosMathPt)
         {
             SwManipulatorHandler2_OnUpdateDrag(pManipulator, handleIndex, newPosMathPt);
         }

     }
 }
```
