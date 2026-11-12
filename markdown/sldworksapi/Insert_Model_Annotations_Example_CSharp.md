---
title: "Insert Model Annotations Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Model_Annotations_Example_CSharp.htm"
---

# Insert Model Annotations Example (C#)

This example shows how to automatically insert a model's dimensions marked for drawings into a drawing.

```
//---------------------------------------------------------------------------
// Preconditions:
// 1. Assembly document to open exists.
// 2. Run the macro.
//
// Postconditions:
// 1. A new drawing document is opened.
// 2. A drawing view of the assembly document is created.
// 3. The dimensions in the assembly document that are marked for drawings,
//    including any duplicate dimensions, appear in the drawing view.
// 4. The dimensions in the drawing, which are annotations,
//    are selected and marked.
//---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace SelectAnnotationsCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel;
            ModelDocExtension swModelDocExt;
            DrawingDoc swDrawing;
            SelectionMgr swSelmgr;
            View swView;
            object[] annotations;
            object selAnnot;
            Annotation swAnnotation;
            SelectData swSelData;
            int mark;
            string retval;
            bool status;

            retval = swApp.GetUserPreferenceStringValue((int)swUserPreferenceStringValue_e.swDefaultTemplateDrawing);
            swModel = (ModelDoc2)swApp.NewDocument(retval, 0, 0, 0);
            swDrawing = (DrawingDoc)swModel;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            swSelmgr = (SelectionMgr)swModel.SelectionManager;

            // Create drawing from assembly
            swView = (View)swDrawing.CreateDrawViewFromModelView3("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2024\\samples\\tutorial\\api\\wrench.sldasm", "*Front", 0.1314541543147, 0.1407887187817, 0);

            // Select and activate the view
            status = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, false, 0, null, 0);
            status = swDrawing.ActivateView("Drawing View1");

            swModel.ClearSelection2(true);

            // Insert the annotations marked for the drawing
            annotations = (object[])swDrawing.InsertModelAnnotations4((int)swImportModelItemsSource_e.swImportModelItemsFromEntireModel, (int)swInsertAnnotation_e.swInsertDimensionsMarkedForDrawing, true, false, false, false, false, false);

            // Select and mark each annotation
            swSelData = swSelmgr.CreateSelectData();
            mark = 0;

            foreach (object annot in annotations)
            {
                selAnnot = annot;
                swAnnotation = (Annotation)selAnnot;
                status = swAnnotation.Select3(true, swSelData);
                swSelData.Mark = mark;
                mark = mark + 1;
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
