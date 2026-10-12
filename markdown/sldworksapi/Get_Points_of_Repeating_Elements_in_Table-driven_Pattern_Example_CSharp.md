---
title: "Get Points of Repeating Elements in Table-driven Pattern (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_CSharp.htm"
---

# Get Points of Repeating Elements in Table-driven Pattern (C#)

This example shows that the points that describe the locations of the repeating elements in a table-driven pattern are based on the table-driven pattern's coordinate system.

```
//---------------------------------------------
// Preconditions:
// 1. Verify that the part to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Gets the coordinates of the
//    points for the two repeating elements in the
//    table-driven pattern.
// 2. Examine the Immediate window.
//
// NOTE: Because the part is used elsewhere, do
// not save changes.
//---------------------------------------------

	using SolidWorks.Interop.sldworks;

	using SolidWorks.Interop.swconst;

	using System;

	using System.Diagnostics;

	namespace PatternCS.csproj

	{

	    partial class SolidWorksMacro

	    {

	        public void Main()

	        {

	            ModelDoc2 swModel = default(ModelDoc2);

	            ModelDocExtension swModelDocExt = default(ModelDocExtension);

	            SelectionMgr swSelMgr = default(SelectionMgr);

	            Feature swFeat = default(Feature);

	            CoordinateSystemFeatureData swCoordinateData = default(CoordinateSystemFeatureData);

	            TablePatternFeatureData swTablePatternFeatData = default(TablePatternFeatureData);

	            MathTransform swMathTransform = default(MathTransform);

	            MathUtility swMathUtility = default(MathUtility);

	            MathPoint swMathPoint = default(MathPoint);

	            bool status = false;

	            int errors = 0;

	            int warnings = 0;

	            string filename = null;

	            double[]
	points = null;

	            string point = null;

	            double[] pointsArray = new double[3];

	            int i = 0;

	            filename = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS
	2018\\samples\\tutorial\\api\\tablepattern.sldprt";

	            swModel = (ModelDoc2)swApp.OpenDoc6(filename, (int)swDocumentTypes_e.swDocPART,
	(int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

	            swModelDocExt = (ModelDocExtension)swModel.Extension;

	            swSelMgr = (SelectionMgr)swModel.SelectionManager;

	            // Select the table-driven
	pattern

	            status = swModelDocExt.SelectByID2("TPattern1", "BODYFEATURE",
	0, 0, 0, false,
	0, null,
	0);

	            swFeat = (Feature)swSelMgr.GetSelectedObject6(1, -1);

	            swTablePatternFeatData = (TablePatternFeatureData)swFeat.GetDefinition();

	            swTablePatternFeatData.AccessSelections(swModel, null);

	            // Get the points of the
	repeating elements in the table-driven pattern

	            //
	and transform them to coordinates

	            swCoordinateData = ((Feature)swTablePatternFeatData.CoordinateSystem).GetDefinition() as CoordinateSystemFeatureData;

	            swCoordinateData.AccessSelections(swModel, null);

	            swMathTransform = swCoordinateData.Transform;

	            swCoordinateData.ReleaseSelectionAccess();

	            swMathUtility = (MathUtility)swApp.GetMathUtility();

	            points = (double[])swTablePatternFeatData.PointArray;
```

```vb
            Debug.Print("Number of points: " + swTablePatternFeatData.GetPointCount());

             for (i = 0; i < points.Length; i += 3)
             {
                 pointsArray[0] = points[i];
                 pointsArray[1] = points[i + 1];
                 pointsArray[2] = points[i + 2];
                 swMathPoint = (MathPoint)swMathUtility.CreatePoint(pointsArray);

                 swMathPoint = swMathPoint.MultiplyTransform(swMathTransform.Inverse()) as MathPoint;

                 // Print the coordinates for the two repeating elements in the table-driven pattern
                 point =  "x: " + ((double[])swMathPoint.ArrayData)[0].ToString() + " y: " + ((double[])swMathPoint.ArrayData)[1].ToString() + " z: " + ((double[])swMathPoint.ArrayData)[2].ToString();

                 Debug.Print(point);

             }

             swTablePatternFeatData.ReleaseSelectionAccess();

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
