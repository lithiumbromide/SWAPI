---
title: "Get Persistent IDs Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Persistent_IDs_Example_CSharp.htm"
---

# Get Persistent IDs Example (C#)

## Get Sheet IDs Example (C#)

This example shows how to get the IDs of drawing sheets.

```vb
//--------------------------------------------------------------------------
 // Preconditions:
 // 1. Read the SOLIDWORKS Document Manager API Help
 //    Getting Started topic and ensure that the required DLLs
 //    have been registered.
 // 2. Open SOLIDWORKS and copy the code below to a C# macro.
 // 3. Convert the drawing document specified in sDocFileName
 //    to the latest supported version by opening and saving it
 //    to another name in SOLIDWORKS.
 //
 //    NOTE: Because this document is used elsewhere, do not
 //    save any changes when closing it.
 //
 // 4. Ensure that the latest SolidWorks.Interop.swdocumentmgr.dll
 //    interop assembly is loaded in the project.
 //    (Right-click the project in Project Explorer,
 //    click Add Reference,  click the interop assembly in
 //    the .NET tab, or browse for the DLL in
 //    install_dir\api\redist directory).
 // 5. Substitute your license key for your_license_key
 //    in the code.
 //
 // Postconditions: Inspect the Immediate Window for the sheet IDs.
 //---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.swdocumentmgr;
using System;
using System.Diagnostics;

    partial class SolidWorksMacro
    {
        public void Main()
        {
            SwDMClassFactory swClassFact = default(SwDMClassFactory);
            SwDMApplication swDocMgr = default(SwDMApplication);
            SwDMDocument14 swDoc = default(SwDMDocument14);
            string sDocFileName = null;
            SwDmDocumentType nDocType = default(SwDmDocumentType);
            SwDmDocumentOpenError nRetVal = default(SwDmDocumentOpenError);
            string sLicenseKey = null;

            // Specify your license key
            sLicenseKey = "your_license_key";

            // If this drawing document doesn't exist on your system,
            // then substitute the name of drawing document that does
            sDocFileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\foodprocessor.slddrw";

            nDocType = SwDmDocumentType.swDmDocumentDrawing;
            swClassFact = new SwDMClassFactory();
            swDocMgr = swClassFact.GetApplication(sLicenseKey);
            swDoc = (SwDMDocument14)swDocMgr.GetDocument(sDocFileName, nDocType, true, out nRetVal);
            if ((swDoc == null))
            {
                System.Windows.Forms.MessageBox.Show("Unable to open document. Correct path to file or register Document Manager DLL.");
            }
            SwDMSheet3 Sheet = default(SwDMSheet3);
            object[] Sheets = null;
            int i = 0;
            Sheets = (Object[])swDoc.GetSheets();
            for (i = 0; i <= Sheets.GetUpperBound(0); i++)
            {
                Sheet = (SwDMSheet3)Sheets[i];
                Debug.Print(Sheet.Name + " ID: " + Sheet.GetID());
            }
            swDoc.CloseDoc();
        }
        public SldWorks swApp;
    }
```
