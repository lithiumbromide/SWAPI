---
title: "Get the Current Name of the Configuration of a Suppressed Component (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm"
---

# Get the Current Name of the Configuration of a Suppressed Component (C#)

## Get Current Name of Configuration of Suppressed Component (C#)

This example shows how to obtain the current name of the configuration of a suppressed component.

```vb
//----------------------------------------------------------------------------
 // Preconditions:
 // 1. Read the SOLIDWORKS Document Manager API Getting Started topic
 //    and ensure that the required DLLs are registered.
 // 2. Copy and paste this code into a C# console application
 //    in Microsoft Visual Studio.
 // 3. Add the SolidWorks.Interop.swdocumentmgr.dll reference
 //    to the project:
 //    a. Right-click the solution in Solution Explorer.
 //    b. Click Add Reference.
 //    c. Click Browse.
 //    d. Click install_dir\api\redist\SolidWorks.Interop.swdocumentmgr.dll.
 //    e. Click Add.
 //    f. Click OK.
 // 4. Substitute your_license_key with your SOLIDWORKS
 //    Document Manager license key.
 // 5. Substitute assembly_with_suppressed_comps with the path to an assembly
 //    that contains one or more suppressed components.
 // 6. Open the Immediate window.
 //
 // Postconditions: Examine the Immediate window for configuration information.
 //----------------------------------------------------------------------------

 using System;
 using SolidWorks.Interop.swdocumentmgr;
 using System.Diagnostics;
 using System.IO;
 using System.Collections;

 namespace ConsoleApplication1
 {
     class Program
     {
         static void Main()
         {
             //Specify your license key and path and filename of assembly document
             const string sLicenseKey = "your_license_key";
             const string sDocFileName = "assembly_with_suppressed_comps";

             SwDMClassFactory swClassFact = default(SwDMClassFactory);
             SwDMApplication4 swDocMgr = default(SwDMApplication4);
             SwDMDocument18 swDoc = default(SwDMDocument18);
             SwDMDocument18 swDoc2 = default(SwDMDocument18);
             SwDmDocumentOpenError nRetVal = 0;
             SwDMExternalReferenceOption2 dmExtRefOption;
             SwDMSearchOption dmSearchOpt;
             int numExtRefs;

             swClassFact = new SwDMClassFactory();
             swDocMgr = (SwDMApplication4)swClassFact.GetApplication(sLicenseKey);
             swDoc = (SwDMDocument18)swDocMgr.GetDocument(sDocFileName, GetDocType(sDocFileName), false, out nRetVal);
             Debug.Assert(SwDmDocumentOpenError.swDmDocumentOpenErrorNone == nRetVal);

             Debug.Print("File = " + swDoc.FullName);
             Debug.Print("");

             dmExtRefOption = swDocMgr.GetExternalReferenceOptionObject2();
             dmSearchOpt = swDocMgr.GetSearchOptionObject();
             dmExtRefOption.SearchOption = dmSearchOpt;
             dmExtRefOption.Configuration = "Default";
             dmExtRefOption.NeedSuppress = true;

             numExtRefs = swDoc.GetExternalFeatureReferences3(dmExtRefOption);
             Array arrExtRefs = (Array)(dmExtRefOption.ExternalReferences);

             SwDMConfiguration12 config;
             SwDMConfigurationMgr configMgr = swDoc.ConfigurationManager;
             config=(SwDMConfiguration12)configMgr.GetConfigurationByName(configMgr.GetActiveConfigurationName());
             object comps=config.GetComponents();
             Array arrComps = (Array)comps;

             foreach (SwDMComponent9 swComp in arrComps)
             {
                 Debug.Print("Component name: " + swComp.Name2);
                 Debug.Print("Component Configuration name: " + swComp.ConfigurationName);
                 Debug.Print("Component Configuration ID: " + swComp.ConfigurationID);
                 Debug.Print("Component Component ID: " + swComp.GetID());
                 Debug.Print("");

                 string ComponentPathName = swComp.PathName;
                 //Check validity of the Component's path name
                 //It might be out of date if the path changed after
                 //the component was suppressed
                 if (!File.Exists(ComponentPathName))
                     //If that file cannot be found, look for an external
                     //reference with the same name
                     ComponentPathName = FindExtRefPath(swComp.PathName, arrExtRefs);

                 swDoc2 = (SwDMDocument18)swDocMgr.GetDocument(ComponentPathName, GetDocType(ComponentPathName), false, out nRetVal);
                 SwDMConfiguration12 config2;
                 SwDMConfigurationMgr configMgr2 = swDoc2.ConfigurationManager;
                 string[] confignames = (string[])configMgr2.GetConfigurationNames();
                 ArrayList arrConfigNames = new ArrayList(confignames);

                 // If the configuration name for the component doesn't match an
                 // existing config name in the reference part, go find the updated
                 // config name from the part
                 if (!arrConfigNames.Contains(swComp.ConfigurationName))
                 {

                     foreach (string configName in arrConfigNames)
                     {
                         config2 = (SwDMConfiguration12)configMgr2.GetConfigurationByName(configName);
                         if (config2.GetID() == swComp.ConfigurationID)
                             Debug.Print("Reference part configuration name: " + config2.Name2);
                     }
                 }

                 swDoc2.CloseDoc();
             }
         }
         static string FindExtRefPath(string name, Array arrComps)
         {
             string ExtrefPathName = name;
             string[] nameParts = name.Split('\\');
             string justName = nameParts.GetValue(nameParts.GetUpperBound(0)).ToString();

             int i = arrComps.GetLowerBound(0);
             Boolean found = false;
             while ((i<=arrComps.GetUpperBound(0)) && !found)
             {
                 string extref = (arrComps.GetValue(i)).ToString();
                 string[] extrefParts = extref.Split('\\');
                 string justextrefName = extrefParts.GetValue(extrefParts.GetUpperBound(0)).ToString();
                 if (justextrefName == justName)
                 {
                     found = true;
                     ExtrefPathName = extref;
                 }
                 i++;
             }

             return ExtrefPathName;
         }
         static SwDmDocumentType  GetDocType(string name)
         {
             SwDmDocumentType nDocType = SwDmDocumentType.swDmDocumentUnknown;
             if (name.EndsWith("SLDPRT"))
             {
                 nDocType = SwDmDocumentType.swDmDocumentPart;
             }
             else if (name.EndsWith("SLDASM"))
             {
                 nDocType = SwDmDocumentType.swDmDocumentAssembly;
             }

             return nDocType;
         }
     }
 }
```
