---
title: "Get Hyperlinks Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Hyperlinks_Example_CSharp.htm"
---

# Get Hyperlinks Example (C#)

This example shows how to get the hyperlinks for a SOLIDWORKS document using the SOLIDWORKS Document Manager API.

//---------------------------------------------------------------------------
// Preconditions:
// 1. Read the SOLIDWORKS Document Manager API
// **Getting Started** topic and ensure that
// the required DLLs have been registered.
// 2. Copy and paste this module into a C#
// console application in Microsoft Visual Studio.
// 3. Add the **SolidWorks.Interop.swdocumentmgr.dll** reference to the project:
// a. Right-click the solution in Solution Explorer.
// b. Click **Add Reference**.
// c. Click **Browse**.
// d. Click:
// `install_dir`**\api\redist\SolidWorks.Interop.swdocumentmgr.dll**
// 4. Substitute `your_license_code` with your
// SOLIDWORKS Document Manager license key.
// 5. Substitute `model_with_hyperlinks` with the path to a model that
// contains one or more hyperlinks.
// 6. Compile and run this program in Debug mode.
//
// Postconditions: Inspect the Output window and the
// code to see how the API is used.
//--------------------------------------------------------------------------

using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Text;
using SolidWorks.Interop.swdocumentmgr;

class Program
{

```vb
     public static void ProcessDocHyperlinks(SwDMDocument swDoc)
     {
         int i;
         int count = swDoc.GetHyperLinksCount();
         Debug.Print(" Hyperlinks: " + count);

         for (i = 0; i < count; i++)
         {
             Debug.Print(" " + swDoc.GetHyperLinkAt(i));
         }

         Debug.Print("");
     }
```

static void Main(string[] args)
{

const string sLicenseKey = "`your_license_code`";
const string sDocFileName = "`model_with_hyperlinks`";

SwDMClassFactory swClassFact = default(SwDMClassFactory);
SwDMApplication swDocMgr = default(SwDMApplication);
SwDMDocument swDoc = default(SwDMDocument);
SwDMConfigurationMgr swCfgMgr = default(SwDMConfigurationMgr);
SwDmDocumentType nDocType = 0;
SwDmDocumentOpenError nRetVal = 0;

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
// Not a SOLIDWORKS file
nDocType = SwDmDocumentType.swDmDocumentUnknown;

// So cannot open
return;
}

swClassFact = new SwDMClassFactory();
swDocMgr = swClassFact.GetApplication(sLicenseKey);
swDoc = (SwDMDocument)swDocMgr.GetDocument(sDocFileName, nDocType, false, out nRetVal);
swCfgMgr = swDoc.ConfigurationManager;

Debug.Print("File = " + swDoc.FullName);

ProcessDocHyperlinks(swDoc);
}
}
