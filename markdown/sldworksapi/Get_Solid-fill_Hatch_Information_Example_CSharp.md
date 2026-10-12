---
title: "Get Solid-fill Hatch Information Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Solid-fill_Hatch_Information_Example_CSharp.htm"
---

# Get Solid-fill Hatch Information Example (C#)

This example shows how to get information about solid-fill hatches in a detail view in the current drawing sheet.

```
//-----------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\introsw\bolt-assembly.slddrw.
// 2. Verify that c:\temp exists.
// 3. Create a detail view of Section View A-A:
//    a. Click Insert > Drawing View > Detail.
//    b. Sketch the profile for the detail view of Section View A-A.
//    c. Move the pointer while dragging drawing view. When the view
//       is where you want it to be, click to place the view.
//    d. Click OK to close the Detail View PropertyManager page.
// 4. Right-click the detail view in the drawing to open the
//    Area Hatch/Fill PropertyManager page.
//    a. Clear the Material crosshatch check box.
//    b. Select Solid.
//    c. Click OK.
//
// Postconditions:
// 1. Traverses the drawing views.
// 2. Gets data about the solid-fill hatches in the detail view.
// 3. Open c:\temp\SolidFillData.txt in a text editor and examine the
//    contents of the file.
//
// NOTE: Because the drawing is used elsewhere, do not save changes.
//-----------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using Microsoft.VisualBasic;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            DrawingDoc swDrawing = default(DrawingDoc);
            Sheet swSheet = default(Sheet);
            View swView = default(View);
            long nbrSolidFillHatches = 0;
            int ArraySize = 0;
            long i = 0;
            Double[] boundaryData = new Double[4];
            System.IO.StreamWriter file = new System.IO.StreamWriter("c:\\temp\\SolidFillData.txt", false);

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swDrawing = (DrawingDoc)swModel;

            // Get drawing sheet
            swSheet = (Sheet)swDrawing.GetCurrentSheet();

            // Get name of drawing sheet
            file.WriteLine(" Number of drawing views on drawing sheet: " + swDrawing.GetViewCount());

            // First view is the current drawing sheet
            swView = (View)swDrawing.GetFirstView();
            file.WriteLine(" First drawing view is the current drawing sheet, so...");

            // Get first drawing view on drawing sheet
            swView = (View)swView.GetNextView();
            nbrSolidFillHatches = 0;
            ArraySize = 0;
            while ((swView != null))
            {
                file.WriteLine(" Get next drawing view on drawing sheet...");
                file.WriteLine(" View name: " + swView.Name);
                nbrSolidFillHatches = swView.GetSolidHatchCount(out ArraySize);
                file.WriteLine(" Number of solid-fill hatches in this view: " + nbrSolidFillHatches);
                file.WriteLine(" Size of array for the boundary data for the solid-fill hatch(es): " + ArraySize);
                if (ArraySize > 0)
                {
                    boundaryData = (Double[])swView.GetSolidHatchInfo();
                    file.WriteLine(" Is the loop an outer loop (first)? " + boundaryData[0]);
                    file.WriteLine(" Number of polylines in loop: " + boundaryData[1]);
                    file.WriteLine(" Type ( 0 = polyline; 1 = arc or circle): " + boundaryData[2]);
                    file.WriteLine(" Size of geometric data array (will be 0 if Type = 0): " + boundaryData[3]);
                    file.WriteLine(" See IView::GetSolidHatchInfo's API Help topic for descriptions of these array elements: ");
                    for (i = 4; i <= ArraySize - 1; i++)
                    {
                        file.WriteLine(" Boundary data, array element " + i + ": " + boundaryData[i]);
                    }
                }
                // Get next drawing view
                swView = (View)swView.GetNextView();
            }
            file.Close();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
