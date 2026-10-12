---
title: "Write Parasolid Partition Stream to File Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Write_Parasolid_Partition_Stream_to_File_Example_CSharp.htm"
---

# Write Parasolid Partition Stream to File Example (C#)

This example shows how to write a Parasolid partition stream to a file for a part.

**NOTE:** To get the name of the stream and a preview bitmap of the sheet active when the drawing was last saved, use ISwDMDocument10::GetPreviewBitmap and ISwDMDocument10::PreviewStreamName. To get the name of the streams and the preview bitmaps for all sheets in a drawing, use ISwDMSheet2::GetPreviewPNGBitmap and ISwDMSheet2::PreviewPNGStreamName.

```
//--------------------------------------------------------------------------
// Preconditions:
// 1. Read the SOLIDWORKS Document Manager API Getting Started
//    topic and verify that the required DLLs have been registered.
// 2. Create a C# macro in SOLIDWORKS.
// 3. Copy Main class into SolidWorksMacro.cs.
//    a. Specify your_license_key.
//    b. Verify that the specified part exists.
//    c. Add a reference to SolidWorks.Interop.swdocumentmgr.dll:
//       1. Right-click the project in the Project Explorer.
//       2. Click Add Reference.
//       3. Click Browse.
//       4. Click install_dir\api\redist\SolidWorks.Interop.swdocumentmgr.dll.
//    d. Add references to System.Drawing and stdole.
// 3. Create a class and copy Class1 into Class1.cs.
// 4. Verify that c:\temp exists.
// 5. Open the Immediate Window.
//
// Postconditions:
// 1. Creates c:\temp\multi-inter.bmp and c:\temp\Default.xmp_bin.
// 2. Examine the c:\temp and the Immediate Window.
//--------------------------------------------------------------------------
//Main class
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using SolidWorks.Interop.swdocumentmgr;
using System.Drawing;
using stdole;
using System.Windows.Forms;
using System.Diagnostics;

namespace Macro1CSharpMacro.csproj
{
    public partial class SolidWorksMacro
    {
        public enum SwDmDocumentVersion_e
        {
            SwDmDocumentVersionSOLIDWORKS_2000 = 1500,
            SwDmDocumentVersionSOLIDWORKS_2001 = 1750,
            SwDmDocumentVersionSOLIDWORKS_2001Plus = 1950,
            SwDmDocumentVersionSOLIDWORKS_2003 = 2200,
            SwDmDocumentVersionSOLIDWORKS_2004 = 2500,
            SwDmDocumentVersionSOLIDWORKS_2005 = 2800,
            SwDmDocumentVersionSOLIDWORKS_2006 = 3100,
            SwDmDocumentVersionSOLIDWORKS_2007 = 3400,
            SwDmDocumentVersionSOLIDWORKS_2008 = 3800,
            SwDmDocumentVersionSOLIDWORKS_2009 = 4100,
            SwDmDocumentVersionSOLIDWORKS_2010 = 4400,
            SwDmDocumentVersionSOLIDWORKS_2011 = 4700,
            SwDmDocumentVersionSOLIDWORKS_2012 = 5000,
            SwDmDocumentVersionSOLIDWORKS_2013 = 6000,
            SwDmDocumentVersionSOLIDWORKS_2014 = 7000,
            SwDmDocumentVersionSOLIDWORKS_2015 = 8000,
	    SwDmDocumentVersionSOLIDWORKS_2016 = 9000,
            SwDmDocumentVersionSOLIDWORKS_2017 = 10000,
            SwDmDocumentVersionSOLIDWORKS_2018 = 11000,
	    SwDmDocumentVersionSOLIDWORKS_2019 = 12000,
            SwDmDocumentVersionSOLIDWORKS_2020 = 13000,
	    SwDmDocumentVersionSOLIDWORKS_2021 = 14000,
            SwDmDocumentVersionSOLIDWORKS_2022 = 15000,
            SwDmDocumentVersionSOLIDWORKS_2023 = 16000,
            SwDmDocumentVersionSOLIDWORKS_2024 = 17000,
            SwDmDocumentVersionSOLIDWORKS_2025 = 18000,
            SwDmDocumentVersionSOLIDWORKS_2026 = 19000
```

```
        }

        public void Main()
        {
            const string sLicenseKey = "your_license_key";
            const string sDocFileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2024\\samples\\tutorial\\multibody\\multi_inter.sldprt";
            const string sExtractDir = "c:\\temp\\";

            SwDMClassFactory swClassFact = default(SwDMClassFactory);
            SwDMApplication swDocMgr = default(SwDMApplication);
            SwDMDocument10 swDoc = default(SwDMDocument10);
            SwDMConfigurationMgr swCfgMgr = default(SwDMConfigurationMgr);
            string[] vCfgNameArr = null;
            SwDMConfiguration2 swCfg = default(SwDMConfiguration2);
            SwDmDocumentType nDocType = 0;
            SwDmPreviewError nError = 0;
            SwDmBodyError nBodyError = 0;
            SwDmDocumentOpenError nRetVal = 0;
            int i = 0;
            string sFileName = "multi-inter";

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
                swDocMgr = (SwDMApplication)swClassFact.GetApplication(sLicenseKey);
                swDoc = (SwDMDocument10)swDocMgr.GetDocument(sDocFileName, nDocType, true, out nRetVal);

                swCfgMgr = swDoc.ConfigurationManager;

                Debug.Print("File = " + swDoc.FullName);
                Debug.Print(" Active Configuration Name = " + swCfgMgr.GetActiveConfigurationName());
                Debug.Print("");
                Debug.Print(" Version = " + swDoc.GetVersion());
                Debug.Print(" Author = " + swDoc.Author);
                Debug.Print(" Comments = " + swDoc.Comments);
                Debug.Print(" Creation Date = " + swDoc.CreationDate);
                Debug.Print(" Keywords = " + swDoc.Keywords);
                Debug.Print(" Last Saved By = " + swDoc.LastSavedBy);
                Debug.Print(" Last Saved Date = " + swDoc.LastSavedDate);
                Debug.Print(" Subject = " + swDoc.Subject);
                Debug.Print(" Title = " + swDoc.Title);

                vCfgNameArr = (string[])swCfgMgr.GetConfigurationNames();

                foreach (string vCfgName in vCfgNameArr)
                {
                    swCfg = (SwDMConfiguration2)swCfgMgr.GetConfigurationByName(vCfgName);

                    // SwDMConfiguration::GetPreviewBitmap throws an unmanaged COM exception
                    // for out-of-process C# console applications
                    // Use the following code in SOLIDWORKS C# macros and add-ins
                    object objBitMap = swCfg.GetPreviewBitmap(out nError);
                    System.Drawing.Image imgPreview = PictureDispConverter.Convert(objBitMap);
                    imgPreview.Save("c:\\temp\\" + sFileName + ".bmp", System.Drawing.Imaging.ImageFormat.Bmp);
                    imgPreview.Dispose();

                    Debug.Print(" " + vCfgName);
                    Debug.Print("   Description = " + swCfg.Description);
                    Debug.Print("   Parent ConfigurationName = " + swCfg.GetParentConfigurationName());
                    Debug.Print("   Preview stream = " + swCfg.PreviewStreamName);

                    switch ((SwDmDocumentVersion_e)swDoc.GetVersion())
                    {
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2000:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2001:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2001Plus:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2003:
                            Debug.Print("  Body stream = " + swCfg.StreamName);
                            Debug.Print("  Body count = " + (swCfg.GetBodiesCount() - 1));

                            for (i = 0; i <= swCfg.GetBodiesCount() - 1; i++)
                            {
                                nBodyError = swCfg.GetBody(i, sExtractDir + vCfgName + "_" + i.ToString() + ".x_b");
                            }

                            break;
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2004:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2005:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2006:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2007:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2008:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2009:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2010:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2011:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2012:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2013:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2014:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2015:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2016:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2017:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2018:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2019:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2020:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2021:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2022:
			case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2023:
			case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2024:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2025:
                        case SwDmDocumentVersion_e.SwDmDocumentVersionSOLIDWORKS_2026:
                            Debug.Print("   Partition stream = " + swCfg.StreamName);
                            // SwDMConfiguration2::GetPartitionStream takes file name as an input and writes
                            // to it. The extensions .xmp_bin (for NTFS) and .p_b (for FAT) are
                            // the valid extensions of a partition file. PK_PARTITION_receive_u takes
                            // this file name as input to get partitions and bodies in it.
                            // Refer to Parasolid documentation for details.
                            nBodyError = swCfg.GetPartitionStream(sExtractDir + vCfgName + ".xmp_bin");
                            break;
                        default:
                            break;
                    }
                }
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
