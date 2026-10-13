---
title: "Keep SOLIDWORKS Design Invisible While Activating Documents Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_CSharp.htm"
---

# Keep SOLIDWORKS Design Invisible While Activating Documents Example (C#)

This example shows how to keep SOLIDWORKS Design invisible while activating documents, including assembly component files, and saving those documents as PDF files.

```
//------------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly file exists.
// 2. Verify that c:\temp exists.
// 3. Open the Immediate window.
//
// Postconditions:
// 1. Saves the specified assembly file and its
//    component files as PDF files to the c:\temp.
// 2. Examine the Immediate window and c:\temp.
//--------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.IO;

namespace Macro1CSharp.csproj
{
    public
 partial class SolidWorksMacro
    {
        public
 ModelDoc2 swModel;
        public ModelDocExtension swExtension;
```

```vb
         public void Main()
         {
             Frame pFrame;
             string Document = null;
             string Output = null;
             try
             {
                 // Allow SOLIDWORKS Design to run in the background
                 // and be invisible
                 swApp.UserControl = false;

                 // If the following property is true, then the
                 // SOLIDWORKS Design frame will be visible on a call to
                 // ISldWorks::ActivateDoc2; so, set it to false
                 swApp.Visible = false;

                 // Keep SOLIDWORKS Design frame invisible when
                 // ISldWorks::ActivateDoc2 is called
                 pFrame = (Frame)swApp.Frame();
                 pFrame.KeepInvisible = true;

                 Document = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\blade shaft.sldasm";
                 Output = "c:\\temp\\";
                 Debug.Print("--- Save files as PDF ---");
                 SaveToPDF(Document, Output);
                 swApp.CloseAllDocuments(true);
                 Debug.Print("--- Done ---");

                 // Show SOLIDWORKS Design frame and SOLIDWORKS Design
                 pFrame.KeepInvisible = false;
                 swApp.Visible = true;
             }
             catch
             {
                 Debug.Print("Execution failed.");
             }
         }

         private void SaveToPDF(string docFileName, string outputpath)
         {
             AssemblyDoc swAssembly = default(AssemblyDoc);
            int doctype = 0;
             int errors = 0;
             int warnings = 0;
             string modelpath = "";
             string modelFileName = "";
             string convFileName = "";
             bool Success = false;
             object[] vComponents = null;
             long i = 0;

             // Determine the type of SOLIDWORKS Design file based on
             // its filename extension
             string extension = "";
             extension = Path.GetExtension(docFileName);
             if (extension == ".sldprt")
             {
                 doctype = (int)swDocumentTypes_e.swDocPART;
             }
             else if (extension == ".SLDPRT")
             {
                 doctype = (int)swDocumentTypes_e.swDocPART;
             }
            else if (extension == ".sldasm")
             {
                 doctype = (int)swDocumentTypes_e.swDocASSEMBLY;
             }
             else if (extension == ".SLDASM")
             {
                 doctype = (int)swDocumentTypes_e.swDocASSEMBLY;
             }
             else if (extension == ".slddrw")
             {
                 doctype = (int)swDocumentTypes_e.swDocDRAWING;
             }
             else if (extension == ".SLDDRW")
             {
                 doctype = (int)swDocumentTypes_e.swDocDRAWING;
             }
             else
             {
                 doctype = (int)swDocumentTypes_e.swDocNONE;
             }

             //Open document
             swModel = (ModelDoc2)swApp.OpenDoc6(docFileName, doctype, (int)swOpenDocOptions_e.swOpenDocOptions_Silent | (int)swOpenDocOptions_e.swOpenDocOptions_ReadOnly, "", ref errors, ref warnings);
             if (swModel == null)
             {
                 Debug.Print("Failed to open document " + modelpath + ". Errors: " + errors);
             }
             // Activate the document, which should remain invisible
             // due to earlier call to IFrame::KeepInvisible
             swModel = (ModelDoc2)swApp.ActivateDoc2(docFileName, true, ref errors);

             // Build destination filename
             modelpath = swModel.GetPathName();
             modelFileName = Path.GetFileNameWithoutExtension(modelpath);
             convFileName = outputpath + modelFileName + ".pdf";
             swExtension = (ModelDocExtension)swModel.Extension;

             // Save document as PDF
             Success = swExtension.SaveAs(convFileName, (int)swSaveAsVersion_e.swSaveAsCurrentVersion, (int)swSaveAsOptions_e.swSaveAsOptions_Silent, null, ref errors,
 ref warnings);
             if (Success)
             {
                 Debug.Print("Document, " + modelpath + ", saved as " + convFileName + ". ");
             }
             else
             {
                 Debug.Print("Document not saved: ");
                 Debug.Print(" Errors: " + errors + modelpath + " as " + convFileName + ". ");
             }
             // Process all components
             if (doctype == (int)swDocumentTypes_e.swDocASSEMBLY)
             {
                 swAssembly = (AssemblyDoc)swModel;
                 vComponents = (object[])swAssembly.GetComponents(true);
                 for (i = 0; i < vComponents.Length; i++)
                 {
                     Component2 swComponent = default(Component2);
                     swComponent = (Component2)vComponents[i];
                     SaveToPDF(swComponent.GetPathName(), outputpath);
                 }
             }
         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>
         public SldWorks swApp;
     }
 }
```
