---
title: "Get, Add, Change, And Delete Cut-List Custom Properties (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_CSharp.htm"
---

# Get, Add, Change, And Delete Cut-List Custom Properties (C#)

## Get, Add, Change, And Delete Cut-List Custom Properties Example (C#)

This example shows how to get cut-list items and their custom properties and how to add, modify, and delete a cut-list custom property.

//--------------------------------------------------------------------------
// Preconditions:
// 1. Read the SOLIDWORKS Document Manager API **Getting Started** topic
// and ensure that the required DLLs have been registered.
// 2. Copy and paste this class into a C# console application in
// Microsoft Visual Studio.
// 3. Ensure that the specified part exists or point to another
// document that contains a cut list with custom properties).
// 4. Add the **SolidWorks.Interop.swdocumentmgr.dll** reference to
// the project:
// a. Right-click the solution in Solution Explorer.
// b. Click **Add Reference**.
// c. Click **Browse**.
// d. Click `install_dir`**\api\redist\SolidWorks.Interop.swdocumentmgr.dl**l.
// e. Click **Add**.
// f. Click **Close**.
// 5. Substitute `your_license_code` with your SOLIDWORKS
// Document Manager license code.
// 6. Compile and run this program in Debug mode.
//
// Postconditions: Inspect the Output Window and the code to see how
// the API is used.
//--------------------------------------------------------------------------

using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Text;
using SolidWorks.Interop.swdocumentmgr;

class Program
{
static void Main(string[] args)
{
SwDMClassFactory swClassFact = default(SwDMClassFactory);
SwDMApplication swDocMgr = default(SwDMApplication);
SwDMDocument10 swDocument10 = default(SwDMDocument10);
SwDMDocument13 swDocument13 = default(SwDMDocument13);

```vb
             SwDMConfiguration16 config = default(SwDMConfiguration16);
             SwDMConfigurationMgr SwDMConfigurationMgr = default(SwDMConfigurationMgr);
```

string sDocFileName = null;
SwDmDocumentType nDocType = default(SwDmDocumentType);
SwDmDocumentOpenError nRetVal = default(SwDmDocumentOpenError);
string sLicenseKey = null;

sLicenseKey = "`your_license_code`";
// Specify your SOLIDWORKS Document Manager license key
sDocFileName = ("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2019\\samples\\tutorial\\weldments\\weldment_box2.sldprt");
// Specify your model document
nDocType = SwDmDocumentType.swDmDocumentPart;
swClassFact = new SwDMClassFactory();

swDocMgr = (SwDMApplication)swClassFact.**GetApplication**(sLicenseKey);
swDocument10 = (SwDMDocument10)swDocMgr.GetDocument(sDocFileName, nDocType, false, out nRetVal);
swDocument13 = (SwDMDocument13)swDocument10;

Debug.Print("Last Update Stamp: " + swDocument13.**GetLastUpdateTimeStamp**());

```vb
            SwDMConfigurationMgr = swDocument13.ConfigurationManager;
             config = (SwDMConfiguration16)SwDMConfigurationMgr.GetConfigurationByName("Default");

             object[] vCutListItems = null;
             vCutListItems = (object[])config.GetCutListItems();

             SwDMCutListItem3 Cutlist = default(SwDMCutListItem3);
             int I = 0;
             SwDmCustomInfoType nType = 0;
             string nLink = null;
             int J = 0;
             object[] vPropNames = null;

             Debug.Print("GET CUT-LIST ITEM");

             for (I = 0; I <= vCutListItems.GetUpperBound(0); I++)
             {
                 Cutlist = (SwDMCutListItem3)vCutListItems[I];
                 Debug.Print("Name : " + Cutlist.Name);
                 Debug.Print(" Quantity : " + Cutlist.Quantity);
                 vPropNames = (object[])Cutlist.GetCustomPropertyNames();

                 if (!((vPropNames == null)))
                 {
                     Debug.Print(" GET CUSTOM PROPERTIES");
                     for (J = 0; J <= vPropNames.GetUpperBound(0); J++)
                     {
                         Debug.Print(" Property Name : " + vPropNames[J]);
                         Debug.Print(" Property Value : " + Cutlist.GetCustomPropertyValue2((string)vPropNames[J], out nType, out nLink));
                         Debug.Print(" Type : " + nType);
                         Debug.Print(" Link : " + nLink);
                     }
                 }

                 Debug.Print("_________________________");
             }

             Cutlist = (SwDMCutListItem3)vCutListItems[0];
             Debug.Print("ADD CUSTOM PROPERTY CALLED Testing1");
             Debug.Print(" Custom Property added? " + Cutlist.AddCustomProperty("Testing1", SwDmCustomInfoType.swDmCustomInfoText, "Verify1"));
             Debug.Print(" GET CUSTOM PROPERTIES");

             vPropNames = (object[])Cutlist.GetCustomPropertyNames();

             for (J = 0; J <= vPropNames.GetUpperBound(0); J++)
             {
                 Debug.Print(" Property Name : " + vPropNames[J]);
                 Debug.Print(" Property Value : " + Cutlist.GetCustomPropertyValue2((string)vPropNames[J], out nType, out nLink));
                 Debug.Print(" Type : " + nType);
                 Debug.Print(" Link : " + nLink);
             }

             Debug.Print("_________________________");
             Debug.Print("SET NEW CUSTOM PROPERTY VALUE FOR Testing1");
             Debug.Print(" Property Value Before Setting: " + Cutlist.GetCustomPropertyValue2("Testing1", out nType, out nLink));
             Debug.Print(" New Value Set? " + Cutlist.SetCustomProperty("Testing1", "Verify3"));
             Debug.Print(" Property Value After Setting : " + Cutlist.GetCustomPropertyValue2("Testing1", out nType, out nLink));
             Debug.Print(" GET CUSTOM PROPERTIES");

             vPropNames = (object[])Cutlist.GetCustomPropertyNames();

             for (J = 0; J <= vPropNames.GetUpperBound(0); J++)
             {
                 Debug.Print(" Property Name : " + vPropNames[J]);
                 Debug.Print(" Property Value : " + Cutlist.GetCustomPropertyValue2((string)vPropNames[J], out nType, out nLink));
                 Debug.Print(" Type : " + nType);
                 Debug.Print(" Link : " + nLink);
             }

             Debug.Print("_________________________");
             Debug.Print("DELETE CUSTOM PROPERTY Testing1");
             Debug.Print(" Delete Property Value? " + Cutlist.DeleteCustomProperty("Testing1"));

             vPropNames = (object[])Cutlist.GetCustomPropertyNames();
             if (!((vPropNames == null)))
             {
                 Debug.Print(" GET CUSTOM PROPERTIES");
                 for (J = 0; J <= vPropNames.GetUpperBound(0); J++)
                 {
                     Debug.Print(" Property Name : " + vPropNames[J]);
                     Debug.Print(" Property Value : " + Cutlist.GetCustomPropertyValue2((string)vPropNames[J], out nType, out nLink));
                     Debug.Print(" Type : " + nType);
                     Debug.Print(" Link : " + nLink);
                 }
             }

             Debug.Print("_________________________");

             //swDocument10.Save()

             swDocument10.CloseDoc();
         }
     }
```
