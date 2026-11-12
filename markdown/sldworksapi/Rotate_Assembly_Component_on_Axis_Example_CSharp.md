---
title: "Rotate Assembly Component on Axis Using IDragOperator::Drag Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_Assembly_Component_on_Axis_Example_CSharp.htm"
---

# Rotate Assembly Component on Axis Using IDragOperator::Drag Example (C#)

This example shows how to rotate an assembly component about an assembly axis using IDragOperator::Drag.

**NOTE:** The code shows how to use a MathUtility object to directly create a transformation matrix (object) that represents rotation about a point and an axis, without having to know details of the OpenGL transformations.

```
//------------------------------------------------------------------
// Preconditions: Verify that the specified assembly document exists.
//
// Postconditions:
// 1. Opens the specified assembly document, which is fully resolved.
// 2. Selects a floating component.
// 3. Watch the selected component in the graphics area rotate 90°
//    about the assembly's x axis.
//
// NOTE: Because this assembly is used elsewhere, do not save any changes.
//------------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace IDragOperatorCSharp.csproj
{
    public partial class SolidWorksMacro
    {
        const double PI = 3.14159;
        const double RadPerDeg = PI / 180.0;

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            AssemblyDoc swAssy = default(AssemblyDoc);
            DragOperator swDragOp = default(DragOperator);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Component2 swComp = default(Component2);
            MathTransform swXform = default(MathTransform);
            MathUtility swMathUtil = default(MathUtility);
            MathPoint swOriginPt = default(MathPoint);
            MathVector swX_Axis = default(MathVector);
            string fileName = null;
            int errors = 0;
            int warnings = 0;
            bool status = false;
            double[] nPts = new double[3];
            object vData = null;
            System.DateTime nNow;
            int i = 0;
            bool bRet = false;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\assem2.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Part3^Assem2-1@assem2", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            swAssy = (AssemblyDoc)swModel;

            swDragOp = (DragOperator)swAssy.GetDragOperator();
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swComp = (Component2)swSelMgr.GetSelectedObjectsComponent2(1);
            swMathUtil = (MathUtility)swApp.GetMathUtility();

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
            // so angle is always the same
            swXform = (MathTransform)swMathUtil.CreateTransformRotateAxis(swOriginPt, swX_Axis, 1.0 * RadPerDeg);

            bRet = swDragOp.AddComponent(swComp, false);

            swDragOp.CollisionDetectionEnabled = false;
            swDragOp.DynamicClearanceEnabled = false;

            // Axial rotation
            swDragOp.TransformType = 1;

            // Solve by relaxation
            swDragOp.DragMode = 2;

            bRet = swDragOp.BeginDrag();

            for (i = 0; i <= 90; i++)
            {
                // Returns false if drag fails
                bRet = swDragOp.Drag(swXform);
                // Wait for 0.01 secs
                nNow = System.DateTime.Now;
                while (System.DateTime.Now < nNow.AddSeconds(.01))
                {
                    // Process event loop
                    System.Windows.Forms.Application.DoEvents();
                }
            }

            bRet = swDragOp.EndDrag();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
