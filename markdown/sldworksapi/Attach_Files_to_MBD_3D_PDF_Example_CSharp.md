---
title: "Attach Files to MBD 3D PDF Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Attach_Files_to_MBD_3D_PDF_Example_CSharp.htm"
---

# Attach Files to MBD 3D PDF Example (C#)

This example shows how to attach files to a SOLIDWORKS MBD 3D PDF.

```
//---------------------------------------------------------------
// Preconditions:
// 1. Verify that the specified SOLIDWORKS MBD 3D PDF theme,
//    files to attach, and C:\temp exist.
// 2. Open public_documents\samples\tutorial\api\block.sldprt.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Gets the MBD3DPdfData object.
// 2. Sets the path and file name for the SOLIDWORKS MBD 3D PDF.
// 3. Sets the theme for the SOLIDWORKS MBD 3D PDF.
// 4. Sets the standard views for the SOLIDWORKS MBD 3D PDF.
// 5. Sets the level of accuracy for lossy compression, whether to
//    apply lossy compression to polygons in the model, and
//    whether to export SOLIDWORKS Design parts and assemblies with PMI
//    annotations to STEP 242 format.
// 6. Sets the files to attach to SOLIDWORKS MBD 3D PDF.
// 7. Creates the SOLIDWORKS MBD 3D PDF.
// 8. Examine the Immediate window.
// 9. Open C:\temp\block.PDF and click the paper clip (Attachments:
//    View file attachments) in the left-side panel.
//
// NOTE: Because the part is used elsewhere, do not save
// changes.
//---------------------------------------------------------------
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
            MBD3DPdfData swMBDPdfData = default(MBD3DPdfData);
            object standardViews = null;
            int[] viewIDs = new int[3];
            string[] filesToAttach = new string[2];
            object attachedFiles = null;
            int status = 0;

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Get MBD3DPdfData object
            swMBDPdfData = (MBD3DPdfData)swModelDocExt.GetMBD3DPdfData();

            //Set path and file name for SOLIDWORKS MBD 3D PDF
            swMBDPdfData.FilePath = "C:\\temp\\block.PDF";

            //Set standard views for SOLIDWORKS MBD 3D PDF
            viewIDs[0] = (int)swStandardViews_e.swFrontView;
            viewIDs[1] = (int)swStandardViews_e.swTopView;
            viewIDs[2] = (int)swStandardViews_e.swDimetricView;
            standardViews = viewIDs;
            swMBDPdfData.SetStandardViews(standardViews);

            //Set SOLIDWORKS MBD 3D PDF theme
            swMBDPdfData.ThemeName = "C:\\Program Files\\SolidWorks Corp\\SOLIDWORKS\\data\\themes\\simple part (a4, portrait)\\theme.xml";

            //Set the level of accuracy for lossy compression, whether to apply
            //lossy compression to polygons in the model, and whether to export
            //SOLIDWORKS Design parts and assemblies with PMI annotations to STEP 242
            //format
            swMBDPdfData.Accuracy = (int)sw3DPDFAccuracy_e.swLow;
            swMBDPdfData.CompressLossyTessellation = true;
            swMBDPdfData.CreateAttachSTEP242 = true;

            //Set the files to attach
            filesToAttach[0] = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\2012-sm.slddrw";
            filesToAttach[1] = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\2012-sm.sldprt";
            attachedFiles = filesToAttach;
            swMBDPdfData.SetAttachments(attachedFiles);

            //Publish to PDF
            status = swModelDocExt.PublishTo3DPDF(swMBDPdfData);
            Debug.Print("Status of publishing part to SOLIDWORKS MBD 3D PDF (0 = success): " + status);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
