---
title: "Get Coordinates of the Plane's Bounding Box Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Coordinates_of_the_Plane's_Bounding_Box_Example_CSharp.htm"
---

# Get Coordinates of the Plane's Bounding Box Example (C#)

This example shows how to get top-left and bottom-right coordinates for a reference plane's bounding box.

```
//-----------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document template
//    exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens a new part document.
// 2. Inserts a reference plane.
// 3. Gets the top-left and bottom-right coordinates
//    of the reference plane's bounding box.
// 4. Examine the Immediate window.
//------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            FeatureManager swFeatureMgr = default(FeatureManager);
            RefPlane swRefPlane = default(RefPlane);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            MathPoint swMathPoint = default(MathPoint);
            bool status = false;
            object[] mathPoints = null;
            double[] arrData = null;
            int i = 0;

            //Create reference plane
            swModel = (ModelDoc2)swApp.NewDocument("C:\\ProgramData\\SolidWorks\\SolidWorks 2015\\templates\\Part.prtdot", 0, 0, 0);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, true, 0, null, 0);
            swFeatureMgr = (FeatureManager)swModel.FeatureManager;
            swRefPlane = (RefPlane)swFeatureMgr.InsertRefPlane(8, 0.0889, 0, 0, 0, 0);

            //Get top-left and bottom-right coordinates
            //of the reference plane's bounding box
            mathPoints = (object[])swRefPlane.BoundingBox;
            //Two (2) MathPoint objects are always returned
            for (i = 0; i <= (mathPoints.Length - 1); i++)
            {
                swMathPoint = (MathPoint)mathPoints[i];
                arrData = (double[])swMathPoint.ArrayData;
                Debug.Print(" Points x, y, z = " + arrData[0] + ", " + arrData[1] + ", " + arrData[2]);
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
