---
title: "Export BOM's Second Column to BOM Table Area Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Export_BOM's_Second_Column_to_BOM_Table_Area_Example_CSharp.htm"
---

# Export BOM's Second Column to BOM Table Area Example (C#)

This example shows how to export a BOM's second column to a BOM Table Area of a SOLIDWORKS MBD 3D PDF.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Verify that:
//    * specified assembly,
//    * specified SOLIDWORKS MBD 3D PDF theme, and
//    * c:\temp exist.
// 2. Open an Immediate window.
//
// Postconditions:
// 1. Inserts an indented BOM table in the assembly.
// 2. Gets the title of the second column in the BOM table
//    to export that column to the SOLIDWORKS MBD 3D PDF.
// 3. Gets the name of the BOM to map to the SOLIDWORKS
//    MBD 3D PDF.
// 4. Gets the SOLIDWORKS MBD 3D PDF data object.
//    a. Sets to display the SOLIDWORKS MBD 3D PDF after
//       publishing it.
//    b. Sets the path for the SOLIDWORKS MBD 3D PDF.
//    c. Sets the SOLIDWORKS MBD 3D PDF theme.
//    d. Sets the standard views for the SOLIDWORKS MBD 3D PDF.
//    e. Maps the BOM and exports its second column to a BOM
//       Table Area in the SOLIDWORKS MBD 3D PDF.
//    f. Publishes and displays the SOLIDWORKS MBD 3D PDF.
// 5. Examine c:\temp\MBDAssembly1.PDF and the Immediate window.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
//---------------------------------------------------------------------------
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
            BomTableAnnotation swBOMAnnotation = default(BomTableAnnotation);
            TableAnnotation swTableAnnotation = default(TableAnnotation);
            BomFeature swBOMFeature = default(BomFeature);
            MBD3DPdfData swMBDPdfData = default(MBD3DPdfData);
            string fileName = null;
            int errors = 0;
            int warnings = 0;
            int bomType = 0;
            string tableTemplate = null;
            string[] columnNames = new string[1];
            object columns = null;
            string BOMTableName = null;
            object standardViews = null;
            int[] viewIDs = new int[3];
            int nbrBOMTableAreas = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\bladed shaft.sldasm";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            // Insert indented BOM table in assembly
            bomType = (int)swBomType_e.swBomType_Indented;
            tableTemplate = "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\lang\\english\\bom-standard.sldbomtbt";
            swBOMAnnotation = (BomTableAnnotation)swModelDocExt.InsertBomTable3(tableTemplate, 0, 1, bomType, "Default", false, (int)swNumberingType_e.swNumberingType_Detailed, true);

            // Get title of second column in BOM table to export to SOLIDWORKS MBD 3D PDF
            swTableAnnotation = (TableAnnotation)swBOMAnnotation;
            columnNames[0] = swTableAnnotation.GetColumnTitle(1);
            Debug.Print("Title of second column to export to SOLIDWORKS MBD 3D PDF: " + columnNames[0]);
            columns = (object)columnNames;

            // Get name of BOM to map to SOLIDWORKS MBD 3D PDF
            swBOMFeature = (BomFeature)swBOMAnnotation.BomFeature;
            BOMTableName = swBOMFeature.Name;
            Debug.Print("Name of BOM to map to SOLIDWORKS MBD 3D PDF: " + BOMTableName);

            // Get MBD3PdfData object
            swMBDPdfData = (MBD3DPdfData)swModelDocExt.GetMBD3DPdfData();

            // Set to display SOLIDWORKS MBD 3D PDF
            swMBDPdfData.ViewPdfAfterSaving = true;

            // Set path for SOLIDWORKS MBD 3D PDF
            swMBDPdfData.FilePath = "c:\\temp\\MBDAssembly1.PDF";

            // Set SOLIDWORKS MBD 3D PDF theme
            swMBDPdfData.ThemeName = "c:\\program files\\solidworks corp\\solidworks\\data\\themes\\simple assembly (a4, landscape)\\theme.xml";

            // Set standard views for SOLIDWORKS MBD 3D PDF
            viewIDs[0] = (int)swStandardViews_e.swFrontView;
            viewIDs[1] = (int)swStandardViews_e.swTopView;
            viewIDs[2] = (int)swStandardViews_e.swDimetricView;
            standardViews = (object)viewIDs;
            swMBDPdfData.SetStandardViews(standardViews);

            // Map BOM and export its second column to BOM Table Area
            nbrBOMTableAreas = swMBDPdfData.GetBomAreaCount();
            if (nbrBOMTableAreas > 0)
            {
                swMBDPdfData.SetBomTable(0, BOMTableName, columns);
            }

            // Publish SOLIDWORKS MBD 3D PDF
            swModelDocExt.PublishTo3DPDF(swMBDPdfData);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
