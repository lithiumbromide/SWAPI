---
title: "Get General Table Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_General_Table_Feature_Example_CSharp.htm"
---

# Get General Table Feature Example (C#)

This example shows how to get a general table feature and some of its table annotation data.

```
//-----------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified drawing document to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified drawing document.
// 2. Inserts a table annotation.
// 3. Gets the general table feature.
// 4. Prints the name of the general table feature and
//    some of its annotation table data the Immediate window.
// 5. Examine the Immediate window.
//
// NOTE: Because the drawing document is used elsewhere, do not
// save changes.
//-----------------------------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace GeneralTableFeatureCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            DrawingDoc swDrawing = default(DrawingDoc);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            string fileName = null;
            TableAnnotation swTableAnnotation = default(TableAnnotation);
            GeneralTableFeature swGeneralTableFeature = default(GeneralTableFeature);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            Feature swFeature = default(Feature);
            int nbrTableAnnotations = 0;
            object[] tableAnnotations = null;
            int i = 0;
            bool anchorAttached = false;
            int anchorType = 0;
            int nbrColumns = 0;
            int nbrRows = 0;

            //Open drawing document
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\assem20.slddrw";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Insert table annotation
            swDrawing = (DrawingDoc)swModel;
            swTableAnnotation = (TableAnnotation)swDrawing.InsertTableAnnotation2(false, 0.0275123456559767, 0.132124518483965, 1, "", 2, 2);
            if ((swTableAnnotation != null))
            {
                swTableAnnotation.BorderLineWeight = 0;
                swTableAnnotation.GridLineWeight = 0;
            }

            //Select and get general table feature
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("General Table1", "GENERALTABLEFEAT", 0, 0, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swGeneralTableFeature = (GeneralTableFeature)swSelectionMgr.GetSelectedObject6(1, -1);
            swFeature = (Feature)swGeneralTableFeature.GetFeature();
            Debug.Print("General table feature name: " + swFeature.Name);

            //Get general table feature's annotation data
            nbrTableAnnotations = swGeneralTableFeature.GetTableAnnotationCount();
            Debug.Print("Number of annotations = " + nbrTableAnnotations);
            tableAnnotations = (object[])swGeneralTableFeature.GetTableAnnotations();
            for (i = 0; i <= (nbrTableAnnotations - 1); i++)
            {
                swTableAnnotation = (TableAnnotation)tableAnnotations[i];
                anchorAttached = swTableAnnotation.Anchored;
                Debug.Print("Table anchored        = " + anchorAttached);
                anchorType = swTableAnnotation.AnchorType;
                Debug.Print("Anchor type           = " + anchorType);
                nbrColumns = swTableAnnotation.ColumnCount;
                Debug.Print("Number of columns     = " + nbrColumns);
                nbrRows = swTableAnnotation.RowCount;
                Debug.Print("Number of rows        = " + nbrRows);
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
