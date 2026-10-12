---
title: "Transform Point from Component Space to Assembly Space Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Transform_Point_from_Component_Space_to_Assembly_Space_Example_CSharp.htm"
---

# Transform Point from Component Space to Assembly Space Example (C#)

This example shows how to transform a point from component space to assembly space.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly document to open
//    exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified assembly document.
// 2. Selects a component.
// 3. Transforms the component's origin to a point in
//    assembly space.
// 4. Examine the Immediate window.
//--------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Transform2.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            MathUtility swMathUtil = default(MathUtility);
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Component2 swComp = default(Component2);
            MathTransform swXform = default(MathTransform);
            double[] nPt = new double[3];
            object vPt = null;
            MathPoint swPt = default(MathPoint);
            bool bRet = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;

            // Open assembly
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\smartcomponents\\stepped_shaft.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            bRet = swModelDocExt.SelectByID2("stepped_shaft-1@stepped_shaft", "COMPONENT", 0, 0, 0, false, 0, null, 0);

            swMathUtil = (MathUtility)swApp.GetMathUtility();
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swComp = (Component2)swSelMgr.GetSelectedObjectsComponent(1);
            swXform = (MathTransform)swComp.Transform2;

            // Point at component origin
            nPt[0] = 0.0;
            nPt[1] = 0.0;
            nPt[2] = 0.0;
            vPt = nPt;
            swPt = (MathPoint)swMathUtil.CreatePoint(vPt);
            swPt = (MathPoint)swPt.MultiplyTransform(swXform);
            Debug.Print("File = " + swModel.GetPathName());
            Debug.Print("  Component = " + swComp.Name2 + " [" + swComp.GetPathName() + "]");
            Debug.Print("    Point in component = (" + nPt[0] * 1000.0 + ", " + nPt[1] * 1000.0 + ", " + nPt[2] * 1000.0 + ") mm");
            Debug.Print("    Point in assembly = (" + ((double[])swPt.ArrayData)[0] * 1000.0 + ", " + ((double[])swPt.ArrayData)[1] * 1000.0 + ", " + ((double[])swPt.ArrayData)[2] * 1000.0 + ") mm");

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
