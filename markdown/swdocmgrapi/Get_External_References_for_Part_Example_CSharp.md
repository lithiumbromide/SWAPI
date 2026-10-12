---
title: "Get External References for Part Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_External_References_for_Part_Example_CSharp.htm"
---

# Get External References for Part Example (C#)

This example shows how to get all of the external references for a part document.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Read the SOLIDWORKS Document Manager API Getting Started
 //    topic and ensure that the required DLLs are registered.
 // 2. Copy and paste this code into a C# console application
 //    in Microsoft Visual Studio.
 // 3. Substitute part_path_and_filename with the path and filename
 //    of a part document containing one or more external references
 //    to other part documents.
 // 4. Rename the namespace to match the name of your C# project.
 // 5. Add the SolidWorks.Interop.swdocumentmgr.dll
 //    reference to the project:
 //    a. Right-click the solution in Solution Explorer.
 //    b. Click Add Reference.
 //    c. Click Browse.
 //    d. Click:
 //       install_dir\api\redist\SolidWorks.Interop.swdocumentmgr.dll
 // 6. Substitute your_license_key with your SOLIDWORKS Document
 //    Manager license key.
 // 7. Ensure that c:\temp exists.
 //
 // Postconditions:
 // 1. Examine the Immediate Window for the external references.
 // 2. Examine c:\temp\extRefPart.xml for more information about the external
 //    references.
 //--------------------------------------------------------------------------

 using System;
 using System.Collections.Generic;
 using System.Text;
 using System.Diagnostics;
 using SolidWorks.Interop.swdocumentmgr;

 namespace GetExtRef_CSharp
 {
     class Program
     {

         static SwDMClassFactory dmClassFact;
         static SwDMApplication4 dmDocMgr;
         static SwDMDocument18 dmDoc;
         static SwDmDocumentType dmDocType;
         static SwDMSearchOption dmSearchOpt;
         static SwDmDocumentOpenError status;
         static SwDMExternalReferenceOption2 dmExtRefOption;
         static int numExtRefs;
         static SwDmXmlDataError xmlError;
         static string[] extRefs;
         static string[] refConfigs;
         static int[] refIDs;
         static bool featStatus;
         static object featNames;
         static string[] strFeatNames;
         static object featTypes;
         static string[] strFeatTypes;
         static int[] brokenStatus;
         static int numFeat;
         static int i;
         static int j;

         const string docPath = "part_path_and_filename";
         const string licenseKey = "your_license_key";

         static void Main()
         {

             setDocType();

             dmClassFact = new SwDMClassFactory();
             dmDocMgr = (SwDMApplication4)dmClassFact.GetApplication(licenseKey);
             dmDoc = (SwDMDocument18)dmDocMgr.GetDocument(docPath, dmDocType, true, out status);

             if ((dmDoc != null))
             {
                 GetReferences();
                 dmDoc.GetXmlStream("c:\\temp\\extRefPart.xml", ref xmlError);
                 dmDoc.CloseDoc();
             }
             else
             {
                 Debug.Print("Unable to open document. Check 'docPath' variable.");
             }

         }

         public static void GetReferences()
         {
             dmExtRefOption = dmDocMgr.GetExternalReferenceOptionObject2();
             dmExtRefOption.Configuration = "Default";
             dmExtRefOption.NeedSuppress = true;
             dmSearchOpt = dmDocMgr.GetSearchOptionObject();
             dmSearchOpt.SearchFilters = ((int)SwDmSearchFilters.SwDmSearchExternalReference + (int)SwDmSearchFilters.SwDmSearchForPart);
             dmExtRefOption.SearchOption = dmSearchOpt;

             // Gets the paths and filenames of the external references, whether the
             // external references are broken, and the names of their
             // referenced configurations
             numExtRefs = dmDoc.GetExternalFeatureReferences3(dmExtRefOption);
             extRefs = (string[])dmExtRefOption.ExternalReferences;
             refConfigs = (string[])dmExtRefOption.ReferencedConfigurations;
             brokenStatus = (int[])dmExtRefOption.BrokenStatus;
             refIDs = (int[])dmExtRefOption.IDs;

             if (numExtRefs > 0)
             {
                 for (i = 0; i < numExtRefs; i++)
                 {
                     Debug.Print("External references: " + extRefs[i]);
                     Debug.Print("  Broken reference (1=broken; 2=not broken; 0=older version or N/A): " + brokenStatus[i]);
                     Debug.Print("  Configuration name: " + refConfigs[i]);
                     Debug.Print("  ID: " + refIDs[i]);
                     Debug.Print("");
                 }

                 // Get the referenced feature names and types in the part document
                 featStatus = dmExtRefOption.ReferencedFeatures(out featNames, out featTypes);
                 strFeatNames = (string[])featNames;
                 strFeatTypes = (string[])featTypes;
                 Debug.Print("Referenced feature names and types in part document: ");
                 numFeat = 0;
                 if (strFeatNames.Length > 0)
                 {
                     for (j = 0; j < extRefs.Length; j++)
                     {
                         Debug.Print("  Feature name: " + strFeatNames[j]);
                         Debug.Print("  Feature type: " + strFeatTypes[j]);
                         Debug.Print("");
                         numFeat = numFeat + 1;
                     }
                 }
             }
         }

         public static void setDocType()
         {
             string typeStr = null;

             typeStr = docPath.Substring((docPath.Length - 6),6);
             typeStr = typeStr.ToUpper();

             if ((typeStr == "SLDPRT"))
             {
                 dmDocType = SwDmDocumentType.swDmDocumentPart;
             }
             else if ((typeStr == "SLDASM"))
             {
                 dmDocType = SwDmDocumentType.swDmDocumentAssembly;
             }

         }

         public static void PrintStrings(string name, object varInp)
         {
             int I = 0;
             String[] arrInp;
             arrInp = (String[])varInp;
             for (I = 0; I < arrInp.Length; I++)
             {
                 string str = null;
                 str = arrInp[I];
                 Debug.Print(name + " : " + str);
             }

         }

     }
 }
```
