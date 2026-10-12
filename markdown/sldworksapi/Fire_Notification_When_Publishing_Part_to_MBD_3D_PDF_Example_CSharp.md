---
title: "Fire Notification When Publishing Part to MBD 3D PDF Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_When_Publishing_Part_to_MBD_3D_PDF_Example_CSharp.htm"
---

# Fire Notification When Publishing Part to MBD 3D PDF Example (C#)

This example shows how to fire a notification when publishing a part document to SOLIDWORKS MBD 3D PDF.

```
//--------------------------------------------------------------
// Preconditions:
// 1. Verify that:
//    * specified part,
//    * SOLIDWORKS MBD 3D PDF theme, and
//    * c:\temp exist.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part.
// 2. Gets the MBD3DPdfData object.
// 3. Sets the path and file name for the SOLIDWORKS MBD 3D PDF.
// 4. Sets the theme for the SOLIDWORKS MBD 3D PDF.
// 5. Sets standard views for the SOLIDWORKS MBD 3D PDF.
// 6. Publishes the part document to SOLIDWORKS MBD 3D PDF.
// 7. Displays a message saying that the part document
//    was published to SOLIDWORKS MBD 3D PDF.
// 8. Click OK to close the message box.
// 9. Examine the Immediate window and c:\temp\MBDPart1.PDF.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//---------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System.Diagnostics;
using System.Windows.Forms;

namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public PartDoc swPart;

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            MBD3DPdfData swMBDPdfData = default(MBD3DPdfData);
            string fileName = null;
            object standardViews = null;
            int[] viewIDs = new int[3];
            int status = 0;
            int errors = 0;
            int warnings = 0;

            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\block.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Set up events
            swPart = (PartDoc)swModel;
            AttachEventHandlers();

            //Get MBD3DPdfData object
            swMBDPdfData = (MBD3DPdfData)swModelDocExt.GetMBD3DPdfData();

            //Set path and file name for SOLIDWORKS MBD 3D PDF
            swMBDPdfData.FilePath = "c:\\temp\\MBDPart1.PDF";

            //Set SOLIDWORKS MBD 3D PDF theme
            swMBDPdfData.ThemeName = "C:\\Program Files\\SolidWorks Corp\\SOLIDWORKS\\data\\themes\\simple part (a4, portrait)\\theme.xml";

            //Set standard views for SOLIDWORKS MBD 3D PDF
            viewIDs[0] = (int)swStandardViews_e.swFrontView;
            viewIDs[1] = (int)swStandardViews_e.swTopView;
            viewIDs[2] = (int)swStandardViews_e.swDimetricView;
            standardViews = (object)viewIDs;
            swMBDPdfData.SetStandardViews(standardViews);

            //Publish part document to SOLIDWORKS MBD 3D PDF
            status = swModelDocExt.PublishTo3DPDF(swMBDPdfData);
            Debug.Print("Status of publishing part to SOLIDWORKS MBD 3D PDF (0 = success): " + status);

        }

        public void AttachEventHandlers()
        {
            AttachSWEvents();
        }

        public void AttachSWEvents()
        {
            swPart.PublishTo3DPDFNotify += this.swPart_PublishTo3DPDFNotify;
        }

        private int swPart_PublishTo3DPDFNotify(string path)
        {
            MessageBox.Show("Part document published to SOLIDWORKS MBD 3D PDF: " + path);
            return 1;
        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```
