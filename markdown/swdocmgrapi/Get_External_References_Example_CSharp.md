---
title: "Get External References Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_External_References_Example_CSharp.htm"
---

# Get External References Example (C#)

This example shows how to get all of the external references for the base part using the SOLIDWORKS Document Manager API.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Read the SOLIDWORKS Document Manager API Getting Started topic and
 //    ensure that the required DLLs are registered.
 // 2. Copy and paste this code into a C# console application
 //    in Microsoft Visual Studio.
 // 3. Modify the path of the specified assembly.
 // 4. Rename the namespace to match the name of your C# project.
 // 5. Add the SolidWorks.Interop.swdocumentmgr.dll
 //    reference to the project:
 //    a. Right-click the solution in Solution Explorer.
 //    b. Click Add Reference.
 //    c. Click Browse.
 //    d. Click:
 //       install_dir\api\redist\SolidWorks.Interop.swdocumentmgr.dll
 // 6. Substitute your_license_key with your SOLIDWORKS Document Manager license key.
 // 7. Ensure that c:\temp exists.
 //
 // Postconditions:
 // 1.  Inspect the Immediate Window for the external  references and their
 //    configurations.
 // 2. Inspect c:\temp\extRef.xml for more information about the external
 //    references.
 //--------------------------------------------------------------------------
```

```vb
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
        static  SwDmXmlDataError xmlError;

         const string docPath = "public_documents\\samples\\tutorial\\api\\assem2.sldasm";
         const string licenseKey = "your_license_key";

         static void Main()
         {

             setDocType();

             dmClassFact = new SwDMClassFactory();
             dmDocMgr = (SwDMApplication4)dmClassFact.GetApplication(licenseKey);
             dmDoc = (SwDMDocument18)dmDocMgr.GetDocument(docPath, dmDocType, true, out status);

             if ((dmDoc != null))
             {
                 NewMethod();
                dmDoc.GetXmlStream("c:\\temp\\extRef.xml", ref xmlError);
                 dmDoc.CloseDoc();
             }
             else
             {
                 Debug.Print("Unable to open document. Check 'docPath' variable.");
             }

         }

         public static void NewMethod()
         {
             dmExtRefOption = (SwDMExternalReferenceOption2)dmDocMgr.GetExternalReferenceOptionObject2();
             dmSearchOpt = dmDocMgr.GetSearchOptionObject();

             dmExtRefOption.SearchOption = dmSearchOpt;
             dmExtRefOption.Configuration = "Default";
             dmExtRefOption.NeedSuppress = true;
             numExtRefs = dmDoc.GetExternalFeatureReferences2(dmExtRefOption);

             PrintStrings("FilePath", dmExtRefOption.ExternalReferences);
             PrintStrings("ConfigName", dmExtRefOption.ReferencedConfigurations);

             dmSearchOpt = null;
             dmExtRefOption = null;

         }

         public static void setDocType()
         {
             string typeStr = null;

             typeStr = docPath.Substring((docPath.Length - 6),6);
             typeStr = typeStr.ToUpper();

             if ((typeStr == "SLDPRT"))
             {
                 dmDocType =  SwDmDocumentType.swDmDocumentPart;
             }
             else if ((typeStr == "SLDASM"))
             {
                 dmDocType =  SwDmDocumentType.swDmDocumentAssembly;
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
