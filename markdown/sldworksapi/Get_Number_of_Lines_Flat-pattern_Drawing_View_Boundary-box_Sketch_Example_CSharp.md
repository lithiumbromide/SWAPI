---
title: "Get the Number of Lines in Flat-pattern Drawing View's Boundary-box Sketch (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_CSharp.htm"
---

# Get the Number of Lines in Flat-pattern Drawing View's Boundary-box Sketch (C#)

This example shows how to get the number of lines in a flat-pattern drawing view's boundary-box sketch.

//----------------------------------------------------------
// Preconditions:
// 1. Open `public_documents`**\samples\tutorial\api\SMGussetAPI.SLDPRT**.
// 2. Create a new drawing document.
// 3. Select **SMGussetAPI.SLDPRT** in the View
// Palette's dropdown list box.
// 4. Open the Immediate window.
//
// Postconditions:
// 1. Examine the Immediate window and the drawing.
// 2. If necessary, drag the drawing onto the drawing sheet
// and zoom in on the drawing view.
//
// NOTE: Because the part is used elsewhere, do not save
// changes.
//---------------------------------------------------------

```vb
  using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;

 namespace GetSMBoundaryBoxDisplayDataViewCSharp.csproj
 {
     partial  class  SolidWorksMacro
     {
         public  void Main()
         {

             ModelDoc2 swModel;
             DrawingDoc swDrawing;
             View swView;
             Sheet swSheet;
             DisplayData swDisplayData;
             double[] sheetProperties = null;
             double sheetScale = 0;
             swDwgPaperSizes_e paperSize;
             double width = 0;
             double height = 0;
             long numViews = 0;
             object[] viewNames = null;
             string viewPaletteName = "";
             string drawingViewName = "";
             int i = 0;
             bool status = false;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swDrawing = (DrawingDoc)swModel;

             // Get current sheet
             swSheet = (Sheet)swDrawing.GetCurrentSheet();
             sheetProperties = (double[])swSheet.GetProperties();
             sheetScale = (double)sheetProperties[2] / sheetProperties[3];
             paperSize = (swDwgPaperSizes_e)swSheet.GetSize(ref width, ref height);

             // Get number of views on View Palette
             numViews = 0;
             viewNames = (object[])swDrawing.GetDrawingPaletteViewNames();

             // Iterate through views on View Palette
             // When view name equals "Flat pattern", drop
             // that view in drawing
             if (!((viewNames == null)))
             {
                 numViews = viewNames.GetUpperBound(0) - viewNames.GetLowerBound(0);
                 for (i = 0; i <= numViews; i++)
                 {
                     viewPaletteName = (string)viewNames[i];
                     if ((viewPaletteName == "Flat pattern"))
                     {
                         Debug.Print("Dropping View Palette view named: " + viewPaletteName);
                         swView = (View)swDrawing.DropDrawingViewFromPalette2(viewPaletteName, 0.0, 0.0, 0.0);
                         drawingViewName = swView.GetName2();
                         Debug.Print("Dropped View Palette view into drawing view named: " + drawingViewName);
                         break;
                     }
                 }
             }

             // Activate view and get number of lines in
             // its boundary box sketch
             status = swDrawing.ActivateView(drawingViewName);
             swView = (View)swDrawing.ActiveDrawingView;

             // Make sure the bounding box sketch is visible
             status = ((ModelDocExtension)swModel.Extension).SelectByID2("Bounding-Box2@SMGussetAPI-1@DrawingView1", "SKETCH", 0, 0, 0, false, 0, null, 0);
            swModel.UnblankSketch();
            swDisplayData = (DisplayData)swView.GetSMBoundaryBoxDisplayData2();
             Debug.Print("Number of lines in boundary box of flat-pattern drawing view: " + swDisplayData.GetLineCount());
         }

         ///  <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;

     }

 }
```
