---
title: "Get 3D Content Central Stream Files Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_3D_Content_Central_Stream_Files_Example_CSharp.htm"
---

# Get 3D Content Central Stream Files Example (C#)

This example builds a design table and configuration rules into a SOLIDWORKS document and then demonstrates how to get the configuration rules out in two XML formats:

* original (3DCC) format

* generic (multi-use) format

//-------------------------------------------------------------------------

// Preconditions:

// 1. Read the SOLIDWORKS Document Manager API G**etting Started**

// topic and ensure that the required DLLs have been registered.

// 2. Ensure that the latest SolidWorks.Interop.swdocumentmgr.dll

// interop assembly is loaded in the project.

// (Right-click the project in Project Explorer, click **Add Reference**,

// click the interop assembly on the .NET tab, or browse for the DLL

// in install_dir\api\redist.)

// 3. Open the specified document and add a design table

// (**Insert > Tables > Design Table**).

// 4. Click the green check mark to accept the design table defaults.

// 5. Multi-select the dimensions or parameters in the document

// to use in the design table.

// 6. Click the **ConfigurationManager** tab and right-click the

// configuration name at the top.

// 7. Select **Configuration Publisher** on the shortcut menu.

// 8. Create rules that are functions of design table parameters,

// setting values as appropriate.

// (To learn how to create rules, read the 3D Content Central

// online help: **http://www.3dcontentcentral.com**.)

// 9. Click **Apply** and **Close**.

// 10. Save the document to another name.

// NOTE: Because the specified document is used in SOLIDWORKS tutorials,

// do not save changes to the original file name.

// 11. Update the sDocFileName in the code below to reference the new

// document.

// 12. Update sLicenseKey in the code below with your license key.

//

// Postconditions:

// 1. Inspect the Immediate window error codes.

// 2. If error codes are swDmXmlDataErrorNone for both format types,

// inspect the directory where the part is located to find

// **motor casing_generic.xml** and **motor casing.xml**.

//-------------------------------------------------------------------

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

using SolidWorks.Interop.swdocumentmgr;

using System;

using System.Diagnostics;

partial class SolidWorksMacro

{

public void Main()

{

const string sLicenseKey = "`your_license_key`";

//Specify your license key

const string sDocFileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\motor casing.sldasm";

SwDMClassFactory swClassFact = default(SwDMClassFactory);

SwDMApplication swDocMgr = default(SwDMApplication);

SwDMDocument14 swDoc = default(SwDMDocument14);

SwDmDocumentType nDocType = default(SwDmDocumentType);

string sPathName = null;

string gPathName = null;

SwDmDocumentOpenError nRetVal = 0;

// Determine type of SOLIDWORKS file based on file extension

if (String.Equals(sDocFileName.Substring((sDocFileName.Length - 6)), "sldprt"))

{

nDocType = SwDmDocumentType.swDmDocumentPart;

}

else if (String.Equals(sDocFileName.Substring((sDocFileName.Length - 6)), "sldasm"))

{

nDocType = SwDmDocumentType.swDmDocumentAssembly;

}

else if (String.Equals(sDocFileName.Substring((sDocFileName.Length - 6)), "slddrw"))

{

nDocType = SwDmDocumentType.swDmDocumentDrawing;

}

else

{

// Probably not a SW file

nDocType = SwDmDocumentType.swDmDocumentUnknown;

// So cannot open

return;

}

// Strip off SOLIDWORKS file extension (sldxxx)

// and add XML extension (xml)

sPathName = sDocFileName.Substring(0, (sDocFileName.Length - 7));

sPathName = sPathName + ".xml";

gPathName = sDocFileName.Substring(0, (sDocFileName.Length - 7));

gPathName = gPathName + "_generic.xml";

swClassFact = new SwDMClassFactory();

swDocMgr = swClassFact.GetApplication(sLicenseKey);

swDoc = (SwDMDocument14)swDocMgr.GetDocument(sDocFileName, nDocType, false, out nRetVal);

SwDmXmlDataError Err = default(SwDmXmlDataError);

Err = swDoc.Get3DCCStreamFile(sPathName);

Debug.Print("Original (3DCC) format SwDmXmlDataError: " + Err);

Err = swDoc.Get3DCCGenericStreamFile(gPathName);

Debug.Print("Generic format SwDmXmlDataError: " + Err);

swDoc.CloseDoc();

}

public SldWorks swApp;

}
