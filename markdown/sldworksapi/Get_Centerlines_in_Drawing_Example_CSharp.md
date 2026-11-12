---
title: "Get Centerlines in Drawing Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Centerlines_in_Drawing_Example_CSharp.htm"
---

# Get Centerlines in Drawing Example (C#)

This example shows how to get all of the centerlines in all of the drawing views in a drawing.

```
//------------------------------------
// Preconditions:
// 1. Verify that the drawing document to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified drawing.
// 2. Inserts a centerline annotation.
// 3. Prints the path and file name of the drawing document
//    to the Immediate window.
// 4. Iterates the sheet and drawing view, prints their names, and
//    prints the name of the centerline annotation to
//    the Immediate window.
// 5. Examine the Immediate window.
//
// NOTE: Because this drawing document is used elsewhere,
// do not save any changes.
//------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace CenterLinesCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            DrawingDoc swDrawing = default(DrawingDoc);
            View swView = default(View);
            Centerline swCenterLine = default(Centerline);
            Annotation swAnnotation = default(Annotation);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\cylinder20.SLDDRW";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swDrawing = (DrawingDoc)swModel;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            status = swDrawing.ActivateView("Drawing View1");
            status = swModelDocExt.SelectByID2("cylinder20-9@Drawing View1", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            status = swModelDocExt.SelectByID2("", "FACE", 0.513454307125032, 0.454946591641617, 250.013794595267, false, 0, null, 0);

            swCenterLine = (Centerline)swDrawing.InsertCenterLine2();
            swModel.ClearSelection2(true);

            swView = (View)swDrawing.GetFirstView();
            Debug.Print("File = " + swModel.GetPathName());

            while ((swView != null))
            {
                Debug.Print("  View = " + swView.GetName2());
                swCenterLine = (Centerline)swView.GetFirstCenterLine();
                while ((swCenterLine != null))
                {
                    swAnnotation = (Annotation)swCenterLine.GetAnnotation();
                    Debug.Print("    Name       = " + swAnnotation.GetName());
                    swCenterLine = swCenterLine.GetNext();
                }
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
