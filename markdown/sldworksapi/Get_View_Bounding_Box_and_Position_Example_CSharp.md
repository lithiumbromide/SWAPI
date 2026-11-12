---
title: "Get View Bounding Box and Position Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_View_Bounding_Box_and_Position_Example_CSharp.htm"
---

# Get View Bounding Box and Position Example (C#)

This example shows how to get the bounding box, geometric center, and position lock status of all drawing views in the drawing sheet.

```
//---------------------------------------------------------
// Preconditions:
// 1. Verify that the drawing document to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified drawing document.
// 2. Gets each drawing view's:
//    * x and y coordinates of the geometric center relative
//      to the drawing sheet origin
//    * bounding box
//    * position lock status
// 3. Examine the Immediate window.
//
// NOTE: Because the drawing is used elsewhere, do not save
// changes.
//----------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            DrawingDoc swDraw = default(DrawingDoc);
            View swView = default(View);
            double[] outline = null;
            double[] pos = null;
            string fileName = null;
            int errors = 0;
            int warnings = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\replaceview.slddrw";
            swDraw = (DrawingDoc)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swView = (View)swDraw.GetFirstView();
            while ((swView != null))
            {
                outline = (double[])swView.GetOutline();
                pos = (double[])swView.Position;
                Debug.Print("View = " + swView.Name);
                Debug.Print("  X and Y positions = (" + pos[0] * 1000.0 + ", " + pos[1] * 1000.0 + ") mm");
                Debug.Print("  X and Y bounding box minimums = (" + outline[0] * 1000.0 + ", " + outline[1] * 1000.0 + ") mm");
                Debug.Print("  X and Y bounding box maximums = (" + outline[2] * 1000.0 + ", " + outline[3] * 1000.0 + ") mm");
		Debug.Print("  Position locked?" + swView.PositionLocked);
                swView = (View)swView.GetNextView();
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
