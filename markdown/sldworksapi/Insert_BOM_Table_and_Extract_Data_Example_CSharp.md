---
title: "Insert BOM Table and Extract Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_BOM_Table_and_Extract_Data_Example_CSharp.htm"
---

# Insert BOM Table and Extract Data Example (C#)

This example shows how to insert a BOM table and extract data from it.

```
//-------------------------------------------------------
// Preconditions:
// 1. Verify that the specified drawing document to open
//    exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified drawing document.
// 2. Selects a drawing view.
// 3. Inserts a BOM table at the point where the drawing
//    was selected.
// 4. Examine the drawing and Immediate window.
//
// NOTE: Because the drawing is used elsewhere, do not
// save changes.
//-------------------------------------------------------
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
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            DrawingDoc swDrawing = default(DrawingDoc);
            SelectionMgr swSelMgr = default(SelectionMgr);
            View swView = default(View);
            BomTableAnnotation swBomTable = default(BomTableAnnotation);
            TableAnnotation swTable = default(TableAnnotation);
            double[] vPickPt = null;
            int nNumCol = 0;
            int nNumRow = 0;
            string sRowStr = null;
            string bomText = null;
            int len = 0;
            string subRowStr = null;
            int i = 0;
            int j = 0;
            bool bRet = false;
            string fileName = null;
            int errors = 0;
            int warnings = 0;

            //Open drawing document and select drawing view
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\driveworksxpress\\mobile gantry.slddrw";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swDrawing = (DrawingDoc)swModel;
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            bRet = swDrawing.ActivateView("Drawing View4");
            bRet = swModelDocExt.SelectByID2("Drawing View4", "DRAWINGVIEW", 0.130207615492954, 0.11628112033195, 0, false, 0, null, 0);

            //Insert BOM table
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swView = (View)swSelMgr.GetSelectedObject6(1, -1);
            vPickPt = (double[])swSelMgr.GetSelectionPoint2(1, -1);
            swBomTable = (BomTableAnnotation)swView.InsertBomTable2(false, vPickPt[0], vPickPt[1], (int)swBOMConfigurationAnchorType_e.swBOMConfigurationAnchor_TopLeft, (int)swBomType_e.swBomType_Indented, "", "");
            swTable = (TableAnnotation)swBomTable;
            nNumCol = swTable.ColumnCount;
            nNumRow = swTable.RowCount;

            //List BOM contents
            for (i = 0; i <= nNumRow - 1; i++)
            {
                sRowStr = "";
                for (j = 0; j <= nNumCol - 1; j++)
                {
                    bomText = swTable.get_Text2(i, j, true);
                    sRowStr = sRowStr + bomText + ",";
                }
                len = sRowStr.Length - 1;
                subRowStr = sRowStr.Substring(0, len);
                Debug.Print(subRowStr);
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
