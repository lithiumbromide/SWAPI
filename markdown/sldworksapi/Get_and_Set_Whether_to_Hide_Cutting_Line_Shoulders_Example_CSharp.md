---
title: "Get and Set Whether to Hide Cutting Line Shoulders Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Whether_to_Hide_Cutting_Line_Shoulders_Example_CSharp.htm"
---

# Get and Set Whether to Hide Cutting Line Shoulders Example (C#)

This example shows how to get and set whether to hide cutting line shoulders in a section view.

```
//--------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the part and templates exist.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the part.
// 2. Creates a drawing of the part.
// 3. Creates a section view.
// 4. Gets and sets whether to hide cutting line shoulders in the section
//    view.
// 5. Examine the Immediate window.
//
// NOTE: Because the part is used elsewhere, do not save it or the drawing.
//--------------------------------------------------------------------------
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
            DrawingDoc swDrawing = default(DrawingDoc);
            Sheet swSheet = default(Sheet);
            View swView = default(View);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SketchSegment swSketchSegment = default(SketchSegment);
            SketchManager swSketchMgr = default(SketchManager);
            DrSection swSectionView = default(DrSection);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;
            double swSheetWidth = 0;
            double swSheetHeight = 0;
            string drawingTemplate = null;
            string sheetTemplate = null;

            //Open part
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\cam roller.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Create drawing of part
            swSheetWidth = 1.189;
            swSheetHeight = 0.841;
            drawingTemplate = "C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2017\\templates\\Drawing.drwdot";
            swDrawing = (DrawingDoc)swApp.NewDocument(drawingTemplate, (int)swDwgPaperSizes_e.swDwgPapersUserDefined, swSheetWidth, swSheetHeight);
            swSheet = (Sheet)swDrawing.GetCurrentSheet();
            swSheet.SetProperties2((int)swDwgPaperSizes_e.swDwgPapersUserDefined, (int)swDwgTemplates_e.swDwgTemplateCustom, 1, 2, false, swSheetWidth, swSheetHeight, true);
            sheetTemplate = "C:\\ProgramData\\SolidWorks\\SOLIDWORKS 2017\\lang\\english\\sheetformat\\a0 - iso.slddrt";
            swSheet.SetTemplateName(sheetTemplate);
            swSheet.ReloadTemplate(true);
            status = swDrawing.GenerateViewPaletteViews(fileName);
            swView = (View)swDrawing.DropDrawingViewFromPalette2("*Left", 0.580930433566434, 0.431525272727273, 0);

            //Create section view
            swDrawing = (DrawingDoc)swApp.ActiveDoc;
            status = swDrawing.ActivateView("Drawing View1");
            swModel.ClearSelection2(true);
            swModel = (ModelDoc2)swDrawing;
            swSketchMgr = (SketchManager)swModel.SketchManager;
            swSketchSegment = (SketchSegment)swSketchMgr.CreateLine(0.0, 0.0, 0.0, 0.012168, 0.021283, 0.0);
            swSketchSegment = (SketchSegment)swSketchMgr.CreateLine(0.0, 0.0, 0.0, 0.024347, -0.010966, 0.0);
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0.690604633175108, 0.625483883858213, 0, false, 0, null, 0);
            status = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0.747211061353527, 0.357889859742052, 0, true, 0, null, 0);
            swView = (View)swDrawing.CreateSectionViewAt5(0.676815388637685, 0.116110180826413, 0, "A", (int)swCreateSectionViewAtOptions_e.swCreateSectionView_OffsetSection, null, 0);
            status = swDrawing.ActivateView("Drawing View2");
            swModel.ClearSelection2(true);

            //Get section view and get and set whether to hide cutting line shoulders
            swSectionView = (DrSection)swView.GetSection();
            if (swSectionView.CuttingLineShoulders)
            {
                Debug.Print("Hide cutting line shoulders = True");
                Debug.Print("Setting hide cutting line shoulders to False");
                swSectionView.CuttingLineShoulders = false;
                Debug.Print("  Hide cutting line shoulders = " + swSectionView.CuttingLineShoulders);
            }
            else
            {
                Debug.Print("Hide cutting line shoulders = False");
                Debug.Print("Setting hide cutting line shoulders to True");
                swSectionView.CuttingLineShoulders = true;
                Debug.Print("  Hide cutting line shoulders = " + swSectionView.CuttingLineShoulders);
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
