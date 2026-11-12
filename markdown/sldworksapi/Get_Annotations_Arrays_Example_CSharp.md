---
title: "Get Annotations Arrays Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Annotations_Arrays_Example_CSharp.htm"
---

# Get Annotations Arrays Example (C#)

Methods added to the IView interface in SOLIDWORKS API 2009 SP1 can return arrays of each annotation type in a drawing view. This example shows how to call these methods.

```
//-----------------------------------------------------------------------------
// Preconditions: Verify that the specified path and template file exist.
//
// Postconditions:
// 1. Creates a part with annotations.
// 2. Click Save.
// 3. Creates a drawing with third-angle views of the part
//    and annotations.
// 4. Iterates through each annotation array and pops up message boxes
//    containing information about each annotation in the drawing views.
// 5. Click OK to close each message box.
//---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
namespace GetAnnotationsArrays.csproj
{
    partial class SolidWorksMacro
    {
        const string filedir = "C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2016\\templates\\";
        const string TemplateName = "C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2016\\templates\\drawing.drwdot";
        const int TemplateSize = (int)swDwgTemplates_e.swDwgTemplateBsize;
        const int PaperSize = (int)swDwgPaperSizes_e.swDwgPaperBsize;
        const double ScaleNum = 1.0;
        const double ScaleDenom = 2.0;
        ModelDoc2 swModel;
        FeatureManager swFeatMgr;
        DrawingDoc swDraw;
        Sheet swSheet;
        long j;
        bool retval;
        View swView;
        long count;
        string msg;

        public void Main()
        {
            // Create a part
            Build_Part();

            // Create a drawing of the part
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swDraw = (DrawingDoc)swApp.NewDocument(TemplateName, PaperSize, 0.0, 0.0);
            swDraw.ActivateSheet("Sheet1");
            swSheet = (Sheet)swDraw.GetCurrentSheet();
            swSheet.SetSize(PaperSize, 0.0, 0.0);
            swSheet.SetScale(ScaleNum, ScaleDenom, true, true);

            // Create 3rd-angle drawing views
            // Pop up Save As dialog
            // Click Save in the dialog
            retval = swDraw.Create3rdAngleViews2(swModel.GetPathName());
            double LocX = 0;
            double LocY = 0;
            LocX = 0.2635088599471;
            LocY = 0.1934578136726;
            // Create isometric drawing view
            swDraw.CreateDrawViewFromModelView3(swModel.GetPathName(), "*Isometric", LocX, LocY, 0);
            swDraw.ViewDisplayShaded();
            // Insert display dimension annotations from the current model
            swDraw.InsertModelAnnotations3(0, (int)swInsertAnnotation_e.swInsertDimensionsMarkedForDrawing, true, true, false, true);
            // Insert datum target symbol annotations from the current model
            swDraw.InsertModelAnnotations3(0, (int)swInsertAnnotation_e.swInsertDatumTargets, true, true, false, true);
            // Insert geometric tolerance annotations from the current model
            swDraw.InsertModelAnnotations3(0, (int)swInsertAnnotation_e.swInsertGTols, true, true, false, true);
            // Insert surface finish symbol annotations from the current model
            swDraw.InsertModelAnnotations3(0, (int)swInsertAnnotation_e.swInsertSFSymbols, true, true, false, true);
            // Insert datum tag annotations from the current model
            swDraw.InsertModelAnnotations3(0, (int)swInsertAnnotation_e.swInsertDatums, true, true, false, true);
            // Insert dowel symbol on a selected arc or circle - not applicable to this model
            //swDraw.InsertDowelSymbol
            // Insert center line on a selected entity
            //swDraw.InsertCenterLine2
            // Insert cosmetic thread
            //swDraw.InsertThreadCallout
            // Insert weld symbol on the last edge selection
            //swDraw.InsertWeldSymbol
            // Insert weld bead
            // Insert table
            //swDraw.InsertTableAnnotation2

            swDraw.ForceRebuild();

            // Iterate through all the views on the drawing to find display dimensions
            swView = (View)swDraw.GetFirstView();
            while ((swView != null))
            {
                count = swView.GetDisplayDimensionCount();
                DisplayDimension DisplayDimension = default(DisplayDimension);
                Dimension swDim = default(Dimension);
                // Iterate through all the display dimension annotations in each drawing view that has them
                if (count > 0)
                {
                    Object[] Annotations = (Object[])swView.GetDisplayDimensions();
                    for (j = 0; j <= Annotations.GetUpperBound(0); j++)
                    {
                        DisplayDimension = (DisplayDimension)Annotations[j];
                        swDim = (Dimension)DisplayDimension.GetDimension();
                        // For each annotation in each drawing view, pop up a message box with the
                        // annotation name and corresponding dimension
                        msg = "Display dimension found: " + swView.GetName2() + ":" + ((Annotation)DisplayDimension.GetAnnotation()).GetName() + " = " + swDim.GetSystemValue2("") + " meters";
                        swApp.SendMsgToUser2(msg, (int)swMessageBoxIcon_e.swMbInformation, (int)swMessageBoxBtn_e.swMbOk);
                    }
                }
                swView = (View)swView.GetNextView();
            }
            // Iterate through all the views on the drawing to find datum target symbols
            swView = (View)swDraw.GetFirstView();
            while ((swView != null))
            {
                count = swView.GetDatumTargetSymCount();
                DatumTargetSym dtsymbol = default(DatumTargetSym);
                // Iterate through all the datum target symbol annotations in each drawing view that has them
                if (count > 0)
                {
                    Object[] Annotations = (Object[])swView.GetDatumTargetSyms();
                    for (j = 0; j <= Annotations.GetUpperBound(0); j++)
                    {
                        dtsymbol = (DatumTargetSym)Annotations[j];
                        // For each annotation in each drawing view, pop up a message box with the
                        // annotation name and name of each datum target symbol found
                        msg = "Datum target symbol found: " + swView.GetName2() + ":" + ((Annotation)dtsymbol.GetAnnotation()).GetName();
                        swApp.SendMsgToUser2(msg, (int)swMessageBoxIcon_e.swMbInformation, (int)swMessageBoxBtn_e.swMbOk);
                    }
                }
                swView = (View)swView.GetNextView();
            }
            // Iterate through all the views on the drawing to find surface finish symbols
            swView = (View)swDraw.GetFirstView();
            while ((swView != null))
            {
                count = swView.GetSFSymbolCount();
                SFSymbol sfsymbol = default(SFSymbol);
                // Iterate through all the surface finish symbol annotations in each drawing view that has them
                if (count > 0)
                {
                    Object[] Annotations = (Object[])swView.GetSFSymbols();
                    for (j = 0; j <= Annotations.GetUpperBound(0); j++)
                    {
                        sfsymbol = (SFSymbol)Annotations[j];
                        // For each annotation in each drawing view, pop up a message box with the
                        // annotation name and name of each surface finish symbol found
                        msg = "Surface finish symbol found: " + swView.GetName2() + ":" + ((Annotation)sfsymbol.GetAnnotation()).GetName();
                        swApp.SendMsgToUser2(msg, (int)swMessageBoxIcon_e.swMbInformation, (int)swMessageBoxBtn_e.swMbOk);
                    }
                }
                swView = (View)swView.GetNextView();
            }
            // Iterate through all the views on the drawing to find datum tags
            swView = (View)swDraw.GetFirstView();
            while ((swView != null))
            {
                count = (int)swView.GetDatumTagCount();
                DatumTag dTag = default(DatumTag);
                // Iterate through all the datum tags in each drawing view that has them
                if (count > 0)
                {
                    Object[] Annotations = (Object[])swView.GetDatumTags();
                    for (j = 0; j <= Annotations.GetUpperBound(0); j++)
                    {
                        dTag = (DatumTag)Annotations[j];
                        // For each annotation in each drawing view, pop up a message box with the
                        // annotation name and name of each datum tag found
                        msg = "Datum tag found: " + swView.GetName2() + ":" + ((Annotation)dTag.GetAnnotation()).GetName();
                        swApp.SendMsgToUser2(msg, (int)swMessageBoxIcon_e.swMbInformation, (int)swMessageBoxBtn_e.swMbOk);
                    }
                }
                swView = (View)swView.GetNextView();
            }
            // Iterate through all the views on the drawing to find geometric tolerances
            swView = (View)swDraw.GetFirstView();
            while ((swView != null))
            {
                count = (int)swView.GetGTolCount();
                Gtol gtol = default(Gtol);
                // Iterate through all the geometric tolerance symbols in each drawing view that has them
                if (count > 0)
                {
                    Object[] Annotations = (Object[])swView.GetGTols();
                    for (j = 0; j <= Annotations.GetUpperBound(0); j++)
                    {
                        gtol = (Gtol)Annotations[j];
                        // For each annotation in each drawing view, pop up a message box with the
                        // annotation name and name of each geometric tolerance found
                        msg = "Geometric tolerance symbol found: " + swView.GetName2() + ":" + ((Annotation)gtol.GetAnnotation()).GetName();
                        swApp.SendMsgToUser2(msg, (int)swMessageBoxIcon_e.swMbInformation, (int)swMessageBoxBtn_e.swMbOk);
                    }
                }
                swView = (View)swView.GetNextView();
            }
            // In a similar fashion:
            // Get other annotations on the drawing, if they exist
            // Iterate through all the views on the drawing
            // Get the annotation count, and if greater than zero, get the annotation array
            // Iterate on each array, and Set an annotation object to each array member:
            // Annotations = swView.GetDowelSymbols
            // Annotations = swView.GetMultiJogLeaders
            // Annotations = swView.GetDatumOrigins
            // Annotations = swView.GetCenterLines
            // Annotations = swView.GetCThreads
            // Annotations = swView.GetWeldSymbols
            // Annotations = swView.GetWeldBeads
            // Annotations = swView.GetTableAnnotations

            swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swInputDimValOnCreate, true);
            swModel.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swDisplayAnnotations, false);
        }
        private void Build_Part()
        {
            // Builds a part with these annotations:
            // display dimensions, geometric tolerance symbol,
            // surface finish symbol, datum tag symbol, and datum target symbol
            swModel = (ModelDoc2)swApp.NewDocument(filedir + "part.prtdot", 0, 0.0, 0.0);
            swModel.SetUserPreferenceIntegerValue((int)swUserPreferenceIntegerValue_e.swUnitsLinear, (int)swLengthUnit_e.swMETER);
            swModel.SetUserPreferenceDoubleValue((int)swUserPreferenceDoubleValue_e.swMaterialPropertyDensity, 7800);
            swModel.SetUserPreferenceStringValue((int)swUserPreferenceStringValue_e.swMaterialPropertyCrosshatchPattern, "ISO (Steel)");
            swModel.SketchManager.InsertSketch(false);
            double Height = 0;
            double Width = 0;
            Height = 0.05;
            Width = 0.05;
            swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swInputDimValOnCreate, false);
            swModel.SketchManager.CreateLine(0.01, 0.01, 0, 0.01, 0.01 + Height, 0);
            swModel.ViewZoomtofit2();
            // Add display dimension to line
            swModel.AddDimension2(0, 0.01 + Height / 2, 0);
            // Add geometric tolerance to line
            swModel.InsertGtol();
            swModel.SketchManager.CreateLine(0.01, 0.01, 0, 0.01 + Width, 0.01, 0);
            swModel.ViewZoomtofit2();
            // Add display dimension
            swModel.AddDimension2(0.01 + Width / 2, 0, 0);
            // Add surface finish symbol to line
            swModel.Extension.InsertSurfaceFinishSymbol3((int)swSFSymType_e.swSFBasic, (int)swLeaderStyle_e.swSTRAIGHT, 0.01, 0.01, 0.01, (int)swSFLaySym_e.swSFCircular, (int)swArrowStyle_e.swDOT_ARROWHEAD, "", "", "",
            "", "", "", "");
            swModel.SketchManager.CreateLine(0, 0, 0, 0, 0.01, 0).ConstructionGeometry = true;
            swModel.ClearSelection2(true);
            swModel.ViewZoomtofit2();
            double Thick = 0;
            Thick = 0.05;
            double Depth = 0;
            Depth = 0.05;
            swFeatMgr = swModel.FeatureManager;
            swFeatMgr.FeatureExtrusionThin2(true, false, true, 0, 0, Depth, 0, false, false, false,
            false, 0, 0, false, false, false, false, false, Thick, 0,
            0, 0, 0, false, 0.0, false, false, (int)swStartConditions_e.swStartSketchPlane, 0.0, false
            );
            swModel.ViewZoomtofit2();
            swModel.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swDisplayAnnotations, true);
            swModel.ShowNamedView2("Isometric", 7);
            swModel.ViewZoomtofit2();
            // Add datum tag to line
            retval = swModel.Extension.SelectByID2("", "EDGE", 0.06001738353251, -0.01284975502705, -0.05001738353241, false, 0, null, 0);
            DatumTag dTag = default(DatumTag);
            dTag = (DatumTag)swModel.InsertDatumTag2();
            // Add datum target symbol to line
            retval = swModel.Extension.SelectByID2("", "EDGE", 0.06001738353251, -0.01284975502705, -0.05001738353241, false, 0, null, 0);
            object myDatumTarget = null;
            myDatumTarget = swModel.Extension.InsertDatumTargetSymbol2("", "", "", 0, false, 0.03, 0.03, "", "", true,
            12, 0, false, true, true);

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;

    }
}
```
