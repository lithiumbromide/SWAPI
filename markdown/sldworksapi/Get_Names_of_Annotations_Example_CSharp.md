---
title: "Get Names of Annotations Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Names_of_Annotations_Example_CSharp.htm"
---

# Get Names of Annotations Example (C#)

This example shows show to:

- get the names of all of the annotations in a drawing.
- select all of the annotations in a drawing.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified drawing document to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified drawing document.
// 2. Iterates the drawing views and gets and selects
//    each annotation in each drawing view.
// 3. Examine the Immediate window and drawing.
//--------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace GetNamesCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            DrawingDoc swDrawing = default(DrawingDoc);
            View swDrView = default(View);
            object[] annArray = null;
            object obj = null;
            Annotation currAnn = default(Annotation);
            string fileName = null;
            int errors = 0;
            int warnings = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\cylinder20.SLDDRW";
            swDrawing = (DrawingDoc)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Get drawing views and names of annotations in
            //each drawing view
            swDrView = (View)swDrawing.GetFirstView();
            //First drawing view is the sheet, so get next drawing view
            swDrView = (View)swDrView.GetNextView();
            while ((swDrView != null))
            {
                Debug.Print("Name of drawing view: " + swDrView.GetName2());
                annArray = (object[])swDrView.GetAnnotations();
                if ((annArray != null))
                {
                    foreach (object obj_loopVariable in annArray)
                    {
                        obj = (object)obj_loopVariable;
                        currAnn = (Annotation)obj;
                        Debug.Print("  Name of annotation: " + currAnn.GetName());
                        currAnn.Select3(true, null);
                    }
                }
                swDrView = (View)swDrView.GetNextView();
            }
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
