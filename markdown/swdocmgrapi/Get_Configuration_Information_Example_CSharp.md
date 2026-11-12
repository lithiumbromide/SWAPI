---
title: "Get Configuration Information Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Configuration_Information_Example_CSharp.htm"
---

# Get Configuration Information Example (C#)

This example shows how to use the SOLIDWORKS Document Manager API to get configuration-related information for an external part document whose custom properties were transferred from the original part document.

```vb
 //--------------------------------------------------------------------------
 // Preconditions:
 // 1. Read the SOLIDWORKS Document Manager API Getting Started topic
 //    and ensure that the required DLLs have been registered.
 // 2. Copy and paste this class into a C# console application in Microsoft
 //    Visual Studio.
 // 3. Add the Solidworks.Interop.swdocumentmgr.dll and Microsoft.CSharp references
 //    to the project:
 //    a. Right-click the solution in Solution Explorer.
 //    b. Click Add Reference.
 //    c. Click Browse.
 //    d. Click install_dir\api\redist\Solidworks.Interop.swdocumentmgr.dll.
 //    e. Click Add.
 //    f. Click Microsoft.CSharp.
 //    g. Click Add.
 //    h. Click OK.
 // 4. In the code:
//    a. Substitute your_license_key with your SOLIDWORKS Document Manager license key.
 //    b. Ensure that the file pointed to by sDocFileName exists.
 // 5. Press F5 to run the program.
 //
 // Postconditions:
 // 1. Examine the Immediate Window.
 // 2. Verify that both fromparent+ prefaced and non-prefaced custom property
 //    values are shown.
 //--------------------------------------------------------------------------

 using System;
 using System.Collections.Generic;
 using System.Text;
 using System.Diagnostics;
 using SolidWorks.Interop.swdocumentmgr;

     class Program
     {

     public static void ProcessDocCustomProperties(SwDMDocument19 swDoc)
     {

         string[] vCustPropNameArr = null;
         string sCustPropStr = null;
         SwDmCustomInfoType nPropType = 0;

         vCustPropNameArr = (string[])swDoc.GetCustomPropertyNames();
         if ((vCustPropNameArr == null)) return;

         Debug.Print(" Document Custom Properties:");

         foreach (string vCustPropName in vCustPropNameArr)
         {
             sCustPropStr = swDoc.GetCustomProperty(vCustPropName, out nPropType);
             Debug.Print("   Prefaced      = " + vCustPropName + " <" + nPropType + "> = " + sCustPropStr);

             sCustPropStr = swDoc.GetCustomProperty2(vCustPropName, out nPropType);
             Debug.Print("   Not prefaced  = " + vCustPropName + " <" + nPropType + "> = " + sCustPropStr);

             Debug.Print("");
         }

         Debug.Print("");
     }

     public static void ProcessConfigCustomProperties(SwDMConfiguration14 swCfg)
     {
         string[] vCustPropNameArr = null;
         string sCustPropStr = null;
         SwDmCustomInfoType nPropType = 0;

         vCustPropNameArr = (string[])swCfg.GetCustomPropertyNames();

         if ((vCustPropNameArr == null)) return;
         Debug.Print(" Configuration Custom Properties:");

         foreach (string vCustPropName in vCustPropNameArr)
         {
             sCustPropStr = swCfg.GetCustomProperty(vCustPropName, out nPropType);
             Debug.Print("   Prefaced     = " + vCustPropName + " <" + nPropType + "> = " + sCustPropStr);

             sCustPropStr = swCfg.GetCustomProperty2(vCustPropName, out nPropType);
             Debug.Print("   Not prefaced = " + vCustPropName + " <" + nPropType + "> = " + sCustPropStr);

             Debug.Print("");
         }

         Debug.Print("");
     }

     static void Main(string[] args)
     {

         const string sLicenseKey = "your_license_key";
         //Specify license key

         const string sDocFileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2021\\samples\\tutorial\\api\\ExternalReferencedPart.sldprt";
         //Specify document

         SwDMClassFactory swClassFact = default(SwDMClassFactory);
         SwDMApplication swDocMgr = default(SwDMApplication);
         SwDMDocument19 swDoc = default(SwDMDocument19);
         SwDMConfigurationMgr2 swCfgMgr = default(SwDMConfigurationMgr2);
         string[] vCfgNameArr = null;
         SwDMConfiguration17 swCfg = default(SwDMConfiguration17);
         SwDmDocumentType nDocType = 0;
         SwDmDocumentOpenError nRetVal = 0;

         SwDMConfigurationError results = 0;

         // Determine type of SOLIDWORKS file based on file extension

         if (sDocFileName.EndsWith("sldprt")) {
             nDocType = SwDmDocumentType.swDmDocumentPart;
         }
         else if (sDocFileName.EndsWith("sldasm")) {
             nDocType = SwDmDocumentType.swDmDocumentAssembly;
         }
         else if (sDocFileName.EndsWith("slddrw")) {
             nDocType = SwDmDocumentType.swDmDocumentDrawing;
         }
         else {

             // Not a SOLIDWORKS file
             nDocType = SwDmDocumentType.swDmDocumentUnknown;

             // So cannot open
             return;
         }

         // Because drawing documents do not have configurations,
         // only continue running the project if the document
         // is a part or assembly document

         if ((nDocType != SwDmDocumentType.swDmDocumentDrawing)) {

             swClassFact = new SwDMClassFactory();
             swDocMgr = swClassFact.GetApplication(sLicenseKey);
             swDoc = (SwDMDocument19)swDocMgr.GetDocument(sDocFileName, nDocType, false, out nRetVal);
             Debug.Assert(SwDmDocumentOpenError.swDmDocumentOpenErrorNone == nRetVal);
             swCfgMgr = swDoc.ConfigurationManager;

             Debug.Print("File = " + swDoc.FullName);
             Debug.Print(" Active Configuration Name = " + swCfgMgr.GetActiveConfigurationName());
             Debug.Print("");
             Debug.Print(" Version = " + swDoc.GetVersion());
             Debug.Print(" Author = " + swDoc.Author);
             Debug.Print(" Comments = " + swDoc.Comments);
             Debug.Print(" Creation Date (string) = " + swDoc.CreationDate);
             Debug.Print(" Creation Date (numeric) = " + swDoc.CreationDate2);
             Debug.Print(" Keywords = " + swDoc.Keywords);
             Debug.Print(" Last Saved By = " + swDoc.LastSavedBy);
             Debug.Print(" Last Saved Date (string) = " + swDoc.LastSavedDate);
             Debug.Print(" Last Saved Date (numeric) = " + swDoc.LastSavedDate2);
             Debug.Print(" Subject = " + swDoc.Subject);
             Debug.Print(" Title = " + swDoc.Title);
             Debug.Print(" Last Update Timestamp = " + swDoc.GetLastUpdateStamp());
             Debug.Print(" Is Detached Drawing? " + swDoc.IsDetachedDrawing());
             Debug.Print("");

             vCfgNameArr = (string[])swCfgMgr.GetConfigurationNames2(out results);
             Debug.Print(" Number of configurations = " + wCfgMgr.GetConfigurationCount2(out results));

             foreach (string vCfgName in vCfgNameArr) {

                 swCfg = (SwDMConfiguration14)swCfgMgr.GetConfigurationByName2(vCfgName, out results);

                 Debug.Print(" " + vCfgName);
                 Debug.Print(" Description = " + swCfg.Description);
                 Debug.Print(" Parent Configuration Name = " + swCfg.GetParentConfigurationName());
                 Debug.Print(" Last Update Timestamp = " + swCfg.GetLastUpdateStamp());
                Debug.Print(" 3DExperience configuration type as defined by swDm3DExperienceCfgType_e  = " + swCfg.Get3DExperienceType());
                Debug.Print("    3DExperience physical product represented by this configuration  = " + swCfg.GetRepresentationParent());
                 Debug.Print("");

                 ProcessConfigCustomProperties(swCfg);
             }

             ProcessDocCustomProperties(swDoc);
         }
     }
 }
```
