---
title: "Get PNG Preview Bitmap and Stream for Configuration Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_PNG_Preview_Bitmap_and_Stream_for_Configuration_Example_CSharp.htm"
---

# Get PNG Preview Bitmap and Stream for Configuration Example (C#)

This example shows how to get the name of the stream and the PNG preview bitmap for a configuration in a part.

**NOTE**: To get the name of the stream and a preview bitmap of the sheet active when the drawing was last saved, use ISwDMDocument10::GetPreviewBitmap and ISwDMDocument10::PreviewStreamName. To get the name of the streams and the preview bitmaps for all sheets in a drawing, use ISwDMSheet2::GetPreviewPNGBitmap and ISwDMSheet2::PreviewPNGStreamName.

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
// 5. Verify that C:\temp exists.
// 6. Open the Immediate Window.
//
// Postconditions:
// 1. Creates a preview bitmap of the Default configuration.
// 2. Right-click C:\temp\Default.PNG and click Preview.
// 3. Examine the Immediate Window.
//---------------------------------------------------------------------------
//Main class
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.swdocumentmgr;
using System.Drawing;
using stdole;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {

            const string sDocFileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\multibody\\multi_inter.sldprt";
            SwDMClassFactory swClassFact = default(SwDMClassFactory);
            SwDMApplication swDocMgr = default(SwDMApplication);
            SwDMDocument swDoc = default(SwDMDocument);
            SwDMConfigurationMgr swCfgMgr = default(SwDMConfigurationMgr);
            string[] vCfgNameArr = null;
            SwDMConfiguration7 swCfg = default(SwDMConfiguration7);
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
                // Not a SOLIDWORKS file, so cannot open
                nDocType = SwDmDocumentType.swDmDocumentUnknown;
                return;
            }

            // Because drawing documents do not have configurations,
            // only continue running the macro if the document
            // is a part or assembly document
            if ((nDocType != SwDmDocumentType.swDmDocumentDrawing))
            {

                swClassFact = new SwDMClassFactory();
                swDocMgr = (SwDMApplication)swClassFact.GetApplication("your_license_key");
                swDoc = (SwDMDocument)swDocMgr.GetDocument(sDocFileName, nDocType, true, out nRetVal);

                swCfgMgr = swDoc.ConfigurationManager;

                Debug.Print("File = " + swDoc.FullName);
                Debug.Print("Active configuration name = " + swCfgMgr.GetActiveConfigurationName());
                vCfgNameArr = (string[])swCfgMgr.GetConfigurationNames();

                foreach (string vCfgName in vCfgNameArr)
                {

                    swCfg = (SwDMConfiguration7)swCfgMgr.GetConfigurationByName(vCfgName);
                    // SwDMConfiguration7::GetPreviewPNGBitmap throws an unmanaged COM exception
                    // for out-of-process C# console applications
                    // Use the following code in SOLIDWORKS C# macros and add-ins
                    object objBitMap = swCfg.GetPreviewPNGBitmap(out nError);
                    System.Drawing.Image imgPreview = PictureDispConverter.Convert(objBitMap);
                    imgPreview.Save("C:\\temp\\" + vCfgName + ".PNG", System.Drawing.Imaging.ImageFormat.Png);
                    imgPreview.Dispose();

                    Debug.Print("   " + vCfgName);
                    Debug.Print("     PNG preview stream = " + swCfg.PreviewPNGStreamName);

                    Debug.Print(" ");
                }

                swDoc.CloseDoc();
            }
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
