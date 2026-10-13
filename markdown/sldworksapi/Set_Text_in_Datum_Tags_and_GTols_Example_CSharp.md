---
title: "Set Text in Datum Tags and GTols Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Text_in_Datum_Tags_and_GTols_Example_CSharp.htm"
---

# Set Text in Datum Tags and GTols Example (C#)

This example shows how to set the text in datum tags and geometric tolerances.

```vb
//----------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a drawing that contains at least one view, a datum feature,
 //    and a geometric tolerance.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Sets prefix, suffix, and callouts for the first GTol.
 // 2. Inserts below frame text in the first GTol.
 // 3. Edits below frame text.
 // 4. Deletes the first line of the below frame.
 // 5. Gets the datum tag label.
 // 6. Examine the Immediate window.
 // ---------------------------------------------------------------------------

 using System;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;

 namespace InsertEditBelowFrame_CSharp
 {
     public partial class SolidWorksMacro
     {
         public void Main()
         {

             ModelDoc2 swModel = default(ModelDoc2);
             ModelView swModelView = default(ModelView);
             DrawingDoc swDraw = default(DrawingDoc);
             View swView = default(View);
             Gtol swDispGtol = default(Gtol);
             DatumTag swDatumTag = default(DatumTag);
             double Rect = 0;
             bool bRet = false;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelView = (ModelView)swModel.ActiveView;
             swDraw = (DrawingDoc)swModel;
             swView = (View)swDraw.GetFirstView();
             //sheet
             swView = (View)swView.GetNextView();

             //Set text parts
             swDispGtol = (Gtol)swView.GetFirstGTOL();
             swDispGtol.SetText((int)swGTolTextParts_e.swGTolTextPrefix, "Prefix");
             swDispGtol.SetText((int)swGTolTextParts_e.swGTolTextSuffix, "Suffix");
             swDispGtol.SetText((int)swGTolTextParts_e.swGTolTextCalloutAbove, "Above");
             swDispGtol.SetText((int)swGTolTextParts_e.swGTolTextCalloutBelow, "Below");
             swDispGtol.SetText((int)swGTolTextParts_e.swGTolTextCalloutBelow, "Below1");
             swDispGtol.SetText((int)swGTolTextParts_e.swGTolTextCalloutBelow, "Below2");

             swModelView.GraphicsRedraw(Rect);

             //Get text parts
             Debug.Print("Callout above: " + swDispGtol.GetText((int)swGTolTextParts_e.swGTolTextCalloutAbove));
             Debug.Print("Callout below: " + swDispGtol.GetText((int)swGTolTextParts_e.swGTolTextCalloutBelow));
             Debug.Print("Prefix: " + swDispGtol.GetText((int)swGTolTextParts_e.swGTolTextPrefix));
             Debug.Print("Suffix: " + swDispGtol.GetText((int)swGTolTextParts_e.swGTolTextSuffix));

             //Insert below frame text
             bRet = swDispGtol.InsertBelowFrameTextAt(1, "Line 1 of below frame");
             bRet = swDispGtol.InsertBelowFrameTextAt(2, "Line 2 of below frame");
             bRet = swDispGtol.InsertBelowFrameTextAt(3, "Line 3 of below frame");

             //Get below frame text
             Debug.Print("Below frame text:");
             Debug.Print("  swDispGtol.GetBelowFrameTextAt(1)");
             Debug.Print("  swDispGtol.GetBelowFrameTextAt(2)");
             Debug.Print("  swDispGtol.GetBelowFrameTextAt(3)");

             //Inserts a line at index position 2, because overwrite is set to False
             bRet = swDispGtol.SetBelowFrameTextAt(2, "Line 2 edited in below frame", false);
             Debug.Print("  swDispGtol.GetBelowFrameTextAt(2)");

             bRet = swDispGtol.DeleteBelowFrameTextAt(1);
             //Deletes the first line in the below frame
             //bRet = swDispGtol.DeleteBelowFrameTextAt(-1)  'Deletes all below frame text

             swDatumTag = (DatumTag)swView.GetFirstDatumTag();
             swDatumTag.SetText((int)swDatumTagTextParts_e.swDatumTagTextPrefix, "prefix");
             swDatumTag.SetText((int)swDatumTagTextParts_e.swDatumTagTextSuffix, "suffix");
             swDatumTag.SetText((int)swDatumTagTextParts_e.swDatumTagTextCalloutAbove, "above");
             swDatumTag.SetText((int)swDatumTagTextParts_e.swDatumTagTextCalloutBelow, "below");
             Debug.Print("Datum tag label: " + swDatumTag.GetLabel());

             swModelView.GraphicsRedraw(Rect);
         }

         // The SldWorks swApp variable is pre-assigned for you.
         public SldWorks swApp;

     }
 }
```
