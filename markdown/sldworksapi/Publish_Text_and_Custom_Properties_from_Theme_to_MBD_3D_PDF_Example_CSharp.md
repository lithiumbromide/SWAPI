---
title: "Publish Text and Custom Properties from Theme to MBD 3D PDF Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_CSharp.htm"
---

# Publish Text and Custom Properties from Theme to MBD 3D PDF Example (C#)

This example shows how to publish text and custom properties from a theme to SOLIDWORKS MBD 3D PDF.

```
//--------------------------------------------------------------
// Preconditions:
//  1. Verify that:
//     * specified part,
//     * SOLIDWORKS MBD 3D PDF theme, and
//     * c:\temp exist.
//  2. Open the Immediate window.
//
// Postconditions:
//  1. Opens the specified part.
//  2. Gets the MBD3DPdfData object.
//  3. Sets the path and file name for the SOLIDWORKS MBD 3D PDF.
//  4. Sets to display SOLIDWORKS MBD 3D PDF after publishing.
//  5. Sets the theme for the SOLIDWORKS MBD 3D PDF.
//  6. Sets standard views for the SOLIDWORKS MBD 3D PDF.
//  7. Creates and sets custom views for the SOLIDWORKS MBD 3D PDF.
//  8. Gets the text and custom properties from the specified
//     theme for the SOLIDWORKS MBD 3D PDF and sets the custom
//     property names.
//  9. Creates the SOLIDWORKS MBD 3D PDF.
// 10. Examine the Immediate window and c:\temp\MBDPart1.PDF.
//
// NOTE: Because the part is used elsewhere, do not save changes.
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
            TextAndCustomProperty swTextAndCustomProperty = default(TextAndCustomProperty);
            string fileName = null;
            object standardViews = null;
            int[] viewIDs = new int[3];
            string[] viewNames = new string[2];
            object[] textAndCustomProperties = null;
            int nbrTextAndCustomProperties = 0;
            int status = 0;
            int errors = 0;
            int warnings = 0;
            string custProp = null;
            int i = 0;

            fileName = "C:\\temp\\box.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            //Get MBD3DPdfData object
            swMBDPdfData = (MBD3DPdfData)swModelDocExt.GetMBD3DPdfData();

            //Set path and file name for SOLIDWORKS MBD 3D PDF
            swMBDPdfData.FilePath = "c:\\temp\\MBDPart1.PDF";

            //Display SOLIDWORKS MBD 3D PDF
            swMBDPdfData.ViewPdfAfterSaving = true;

            //Set SOLIDWORKS MBD 3D PDF theme
            swMBDPdfData.ThemeName = "C:\\Program Files\\SolidWorks Corp\\SOLIDWORKS\\data\\themes\\simple part (a4, portrait)\\theme.xml";

            //Set standard views for SOLIDWORKS MBD 3D PDF
            viewIDs[0] = (int)swStandardViews_e.swFrontView;
            viewIDs[1] = (int)swStandardViews_e.swTopView;
            viewIDs[2] = (int)swStandardViews_e.swDimetricView;
            standardViews = viewIDs;
            swMBDPdfData.SetStandardViews(standardViews);

            //Create and set custom views for SOLIDWORKS MBD 3D PDF
            swModel.NameView("CustomView1");
            swModel.NameView("CustomView2");
            viewNames[0] = "CustomView1";
            viewNames[1] = "CustomView2";
            swMBDPdfData.SetMoreViews(viewNames);

            //Get text and custom properties from theme for SOLIDWORKS MBD
            //3D PDF
            textAndCustomProperties = (object[])swMBDPdfData.GetTextAndCustomProperties();
            if ((textAndCustomProperties != null))
            {
                nbrTextAndCustomProperties = textAndCustomProperties.GetUpperBound(0);
                Debug.Print("Text and custom properties from theme:");
                for (i = 0; i <= nbrTextAndCustomProperties; i++)
                {
                    swTextAndCustomProperty = (TextAndCustomProperty)textAndCustomProperties[i];
                    if (swTextAndCustomProperty.IsCustomProperty == false)
                    {
                        Debug.Print(" Text:");
                        Debug.Print("  Description: " + swTextAndCustomProperty.Description);
                        Debug.Print("  Field name: " + swTextAndCustomProperty.Name);
                    }
                    else
                    {
                        Debug.Print(" Custom property:");
                        custProp = "CustomProperty " + Convert.ToString(i);
                        swTextAndCustomProperty.CustomPropertyName = custProp;
                        Debug.Print("  Custom property name: " + swTextAndCustomProperty.CustomPropertyName);
                        Debug.Print("  Description: " + swTextAndCustomProperty.Description);
                        Debug.Print("  Field name: " + swTextAndCustomProperty.Name);
                        Debug.Print("  Value: " + swTextAndCustomProperty.Value);
                    }
                }
            }
            else
            {
                Debug.Print("No text or custom properties in theme.");
            }

            //Create SOLIDWORKS MBD 3D PDF
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
