---
title: "Get XML Stream Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_XML_Stream_Example_CSharp.htm"
---

# Get XML Stream Example (C#)

This example shows how to get an embedded XML stream in a SOLIDWORKS document using the SOLIDWORKS Document Manager API.

//---------------------------------------------------------------------------
// Preconditions:
// 1. Read the SOLIDWORKS Document Manager API
// **Getting Started** topic and ensure that the required
// DLLs have been registered.
// 2. Copy and paste this module into a C# console
// application in Microsoft Visual Studio.
// 3. Ensure that the specified document exists
// (or point to another document).
// 4. Add the **SolidWorks.Interop.swdocumentmgr.dll**
// reference to the project:
// a. Right-click the solution in Solution Explorer.
// b. Click **Add Reference**.
// c. Click **Browse**.
// d. Click:
// `install_dir`**\api\redist\SolidWorks.Interop.swdocumentmgr.dll**.
// 5. Substitute `your_license_code` with your
// SOLIDWORKS Document Manager license key.
//
// Postconditions: Locate the XML stream in the current directory.
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
const string sLicenseKey = "`your_license_code`";
//Specify your license key
const string sDocFileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\EDraw\\claw\\claw-mechanism.sldasm";

SwDMClassFactory swClassFact = default(SwDMClassFactory);
SwDMApplication swDocMgr = default(SwDMApplication);
SwDMDocument swDoc = default(SwDMDocument);
SwDmDocumentType nDocType = 0;
string sPathName = null;
SwDmDocumentOpenError nRetVal = 0;
SwDmXmlDataError nRetVal2 = 0;

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

// Strip off SOLIDWORKS file extension (sldxxx)
// and add XML extension (xml)

sPathName = sDocFileName.Substring(0, sDocFileName.Length - 6);
sPathName = sPathName + "xml";

swClassFact = new SwDMClassFactory();
swDocMgr = (SwDMApplication)swClassFact.GetApplication(sLicenseKey);
swDoc = (SwDMDocument)swDocMgr.GetDocument(sDocFileName, nDocType, false, out nRetVal);

swDoc.**GetXmlStream**(sPathName, ref nRetVal2);

}

}
