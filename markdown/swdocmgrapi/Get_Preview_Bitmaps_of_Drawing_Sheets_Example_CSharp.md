---
title: "Get Preview Bitmaps of Drawing Sheets Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Preview_Bitmaps_of_Drawing_Sheets_Example_CSharp.htm"
---

# Get Preview Bitmaps of Drawing Sheets Example (C#)

This example shows how to get PNG preview bitmaps of the sheets in a drawing document.

```
//-----------------------------------------------------------------------------
// Preconditions:
// 1. Read the SOLIDWORKS Document Manager API Getting Started topic
//    and verify that the required DLLs are registered.
// 2. Create a C# macro in SOLIDWORKS.
// 3. Copy Main class into SolidWorksMacro.cs.
//    a. Specify your_license_key.
//    b. Verify that the specified file to open exists.
//    c. Add a reference to SolidWorks.Interop.swdocumentmgr.dll:
//       1. Right-click the project in the Project Explorer.
//       2. Click Add Reference.
//       3. Click Browse.
//       4. Click install_dir\api\redist\SolidWorks.Interop.swdocumentmgr.dll.
//    d. Add references to System.Drawing and stdole.
// 4. Create a class and copy Class1 into Class1.cs.
// 5. Verify that c:\temp exists.
// 6. Open the Immediate Window.
//
// Postconditions:
// 1. Creates preview bitmaps of the sheets in the drawing document.
// 2. Right-click each c:\temp\Sheetn.png and click Preview.
// 3. Examine the Immediate Window.
//---------------------------------------------------------------------------
//Main class
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.swdocumentmgr;
using System.Drawing;
using stdole;
using System.Runtime.InteropServices;
using System;
using System.Windows.Forms;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {

            SwDMClassFactory swClassFact = default(SwDMClassFactory);
            SwDMApplication swDocMgr = default(SwDMApplication);
            SwDMDocument10 swDoc = default(SwDMDocument10);
            string sDocFileName = null;
            SwDmDocumentType nDocType = default(SwDmDocumentType);
            SwDmDocumentOpenError nRetVal = default(SwDmDocumentOpenError);
            string sLicenseKey = null;

            // Specify your license key
            sLicenseKey = "your_license_key"

            // If the following drawing document does not exist,
            // then substitute the name of a drawing document that does
            sDocFileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\foodprocessor.slddrw";
            nDocType = SwDmDocumentType.swDmDocumentDrawing;

            swClassFact = new SwDMClassFactory();
            swDocMgr = (SwDMApplication)swClassFact.GetApplication(sLicenseKey);
            swDoc = (SwDMDocument10)swDocMgr.GetDocument(sDocFileName, nDocType, true, out nRetVal);
            if ((swDoc == null))
            {
                MessageBox.Show("Unable to open document.");
            }

            object[] Sheets = null;
            SwDMSheet2 Sheet = default(SwDMSheet2);
            SwDmPreviewError nError;
            byte[] PreviewPNGByteArray = null;

            // Get the sheets in the drawing document
            Sheets = (object[])swDoc.GetSheets();
            int nbrSheets = 0;
            nbrSheets = Sheets.Length;
            string snbrSheets = Convert.ToString(nbrSheets);
            Debug.Print("Number of sheets: " + snbrSheets);
            Debug.Print(" ");

            int i = 0;
            for (i = 0; i < Sheets.Length; i++)
            {
                Sheet = (SwDMSheet2)Sheets[i];
                Debug.Print("Name of sheet: " + (Sheet.Name));
                Debug.Print("Name of preview PNG's stream: " + (Sheet.PreviewPNGStreamName));
                // SwDMSheet2::GetPreviewPNGBitmap throws an unmanaged COM exception
                // for out-of-process C# console applications
                // Use the following code in SOLIDWORKS C# macros and add-ins
                object objBitMap = Sheet.GetPreviewPNGBitmap(out nError);
                if (nError == 0)
                {
                    // For each sheet, convert the picture to an
                    // image and save it as .png file
                    System.Drawing.Image imgPreview = PictureDispConverter.Convert(objBitMap);
                    imgPreview.Save("c:\\temp\\" + Sheet.Name + ".png", System.Drawing.Imaging.ImageFormat.Png);
                    imgPreview.Dispose();

                    // Get the preview's PNG byte array
                    PreviewPNGByteArray = (byte[])Sheet.GetPreviewPNGBitmapBytes(out nError);
                    int nbrPreviewPNGBitmapBytes = 0;
                    nbrPreviewPNGBitmapBytes = PreviewPNGByteArray.Length;
                    string snbrPreviewPNGBitmapBytes = Convert.ToString(nbrPreviewPNGBitmapBytes);
                    Debug.Print("Number of bytes in preview's PNG byte array: " + snbrPreviewPNGBitmapBytes);
                    Debug.Print("");
                }
                else
                {
                    switch (nError)
                    {
                        case SwDmPreviewError.swDmPreviewErrorNoPreview:
                            Debug.Print("Error: No preview data stored with document.");
                            break;
                        case SwDmPreviewError.swDmPreviewErrorMakeBmpFail:
                            Debug.Print("Error: Failed to make the bitmap.");
                            break;
                    }
                }
            }

            swDoc.CloseDoc();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```

```
//Class1
```

```
public class PictureDispConverter : System.Windows.Forms.AxHost
{

    public PictureDispConverter()
        : base("56174C86-1546-4778-8EE6-B6AC606875E7")
    {
    }

    public static System.Drawing.Image Convert(object objIDispImage)
    {
        System.Drawing.Image objPicture = default(System.Drawing.Image);
        objPicture = (System.Drawing.Image)System.Windows.Forms.AxHost.GetPictureFromIPicture(objIDispImage);
        return objPicture;
    }

}
```
