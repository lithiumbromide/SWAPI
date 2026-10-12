---
title: "Get eDrawings Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_eDrawings_Data_Example_CSharp.htm"
---

# Get eDrawings Data Example (C#)

This example shows how to get eDrawings data from a SOLIDWORKS document using the SOLIDWORKS Document Manager API.

**NOTE**: ISwDMDocument::GetEDrawingsData is obsolete as of SOLIDWORKS Document Manager API 2005 FCS and has not been superseded.

//---------------------------------------------------------------------------
// Preconditions:
// 1. Read the SOLIDWORKS Document Manager API **Getting Started** topic and
// ensure that the required DLLs have been registered.
// 2. Copy and paste this module into a C# console
// application in Microsoft Visual Studio.
// 3. Ensure that the specified document exists (or point to another document
// that contains eDrawings data).
// 4. Add the **SolidWorks.Interop.swdocumentmgr.dll** reference to the project:
// a. Right-click the solution in Solution Explorer.
// b. Click **Add Reference**.
// c. Click **Browse**.
// d. Click:
// `install_dir`**\api\redist\SolidWorks.Interop.swdocumentmgr.dll**
// 5. Substitute `your_license_code` with your
// SOLIDWORKS Document Manager license key.
// 6. Compile and run this program in Debug mode.
//
// Postconditions:
// 1. Inspect the error code in the Output window.
// 2. The eDrawings data is extracted to a temp file in **C:\temp**.
//---------------------------------------------------------------------------

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
string sEdrawExt = null;
SwDmDocumentOpenError nRetVal = default(SwDmDocumentOpenError);
SwDmEDwgDataError nRetVal2 = default(SwDmEDwgDataError);

// Determine type of SOLIDWORKS file based on file extension

if (sDocFileName.EndsWith("sldprt"))
{
nDocType = SwDmDocumentType.swDmDocumentPart;
sEdrawExt = "eprt";
}
else if (sDocFileName.EndsWith("sldasm"))
{
nDocType = SwDmDocumentType.swDmDocumentAssembly;
sEdrawExt = "easm";
}
else if (sDocFileName.EndsWith("slddrw"))
{
nDocType = SwDmDocumentType.swDmDocumentDrawing;
sEdrawExt = "edrw";
}
else
{
// Not a SOLIDWORKS file
nDocType = SwDmDocumentType.swDmDocumentUnknown;
sEdrawExt = "";

// So cannot open
return;
}

swClassFact = new SwDMClassFactory();
swDocMgr = (SwDMApplication)swClassFact.GetApplication(sLicenseKey);
swDoc = (SwDMDocument)swDocMgr.GetDocument(sDocFileName, nDocType, false, out nRetVal);
Debug.Assert(SwDmDocumentOpenError.swDmDocumentOpenErrorNone == nRetVal);

// Copy eDrawings data to file with eDrawings extension
nRetVal2 = swDoc.**GetEDrawingsData**("c:\\temp\\temp." + sEdrawExt);

Debug.Print("EDrawing error code: " + nRetVal2);
}
}
