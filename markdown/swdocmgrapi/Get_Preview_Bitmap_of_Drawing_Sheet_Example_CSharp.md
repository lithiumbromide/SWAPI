---
title: "Get Preview Bitmap of Drawing Sheet Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Preview_Bitmap_of_Drawing_Sheet_Example_CSharp.htm"
---

# Get Preview Bitmap of Drawing Sheet Example (C#)

This example shows how to get a BMP preview bitmap of the sheet that was active when the drawing was last saved.

```
//-----------------------------------------------------------------------------
// Preconditions:
// 1. Read the SOLIDWORKS Document Manager API Getting Started topic
//    and verify that the required DLLs are registered.
// 2. Create a C# macro in SOLIDWORKS.
// 3. Copy Main into SolidWorksMacro.cs.
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
// 1. Creates a preview bitmap of the sheet active when the drawing was last saved.
// 2. Right-click c:\temp\foodprocessor.bmp and click Preview.
// 3. Examine the Immediate Window.
//---------------------------------------------------------------------------
//Main
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using SolidWorks.Interop.swdocumentmgr;
using System.Drawing;
using stdole;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            const string sLicenseKey = "your_license_key"
            const string sDocFileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\foodprocessor.slddrw";
            const string sExtractDir = "c:\\temp\\";
            const string sFilename = "foodprocessor";
            SwDMClassFactory swClassFact = default(SwDMClassFactory);
            SwDMApplication swDocMgr = default(SwDMApplication);
            SwDMDocument swDoc = default(SwDMDocument);
            SwDMDocument10 swDoc10 = default(SwDMDocument10);
            SwDmDocumentType nDocType = 0;
            SwDmDocumentOpenError nRetVal = 0;
            SwDmPreviewError nError = 0;

            // Determine type of SOLIDWORKS file based on file extension
            if (sDocFileName.EndsWith("sldprt"))
            {
                nDocType = SwDmDocumentType.swDmDocumentPart;
            }
            else if (sDocFileName.EndsWith("sldasm"))
            {
                nDocType = SwDmDocumentType.swDmDocumentAssembly;
            }
            else if (sDocFileName.EndsWith("slddrw"))
            {
                nDocType = SwDmDocumentType.swDmDocumentDrawing;
            }
            else
            {
                // Probably not a SOLIDWORKS file,
                // so cannot open
                nDocType = SwDmDocumentType.swDmDocumentUnknown;
                return;
            }

            swClassFact = new SwDMClassFactory();
            swDocMgr = (SwDMApplication)swClassFact.GetApplication(sLicenseKey);
            swDoc = (SwDMDocument)swDocMgr.GetDocument(sDocFileName, nDocType, true, out nRetVal);
            Debug.Print("File = " + swDoc.FullName);
            Debug.Print("  Version          = " + swDoc.GetVersion());
            Debug.Print("  Author           = " + swDoc.Author);
            Debug.Print("  Comments         = " + swDoc.Comments);
            Debug.Print("  CreationDate     = " + swDoc.CreationDate);
            Debug.Print("  Keywords         = " + swDoc.Keywords);
            Debug.Print("  LastSavedBy      = " + swDoc.LastSavedBy);
            Debug.Print("  LastSavedDate    = " + swDoc.LastSavedDate);
            Debug.Print("  Subject          = " + swDoc.Subject);
            Debug.Print("  Title            = " + swDoc.Title);

            swDoc10 = (SwDMDocument10)swDoc;
            // SwDMDocument10::GetPreviewBitmap throws an unmanaged COM exception
            // for out-of-process C# console applications
            // Use the following code in SOLIDWORKS C# macros and add-ins
            object objBitMap = swDoc10.GetPreviewBitmap(out nError);
            System.Drawing.Image imgPreview = PictureDispConverter.Convert(objBitMap);
            imgPreview.Save(sExtractDir + sFilename + ".bmp", System.Drawing.Imaging.ImageFormat.Bmp);
            imgPreview.Dispose();

            Debug.Print("    Preview stream   = " + swDoc10.PreviewStreamName);

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
