---
title: "Open Document Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_Document_Example_CSharp.htm"
---

# Open Document Example (C#)

This example shows how to programmatically open a document and set the SOLIDWORKS Design working directory.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Verify that the specified document to open exists.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Opens the specified document.
 // 2. Sets the SOLIDWORKS Design working directory to the document directory.
 // 3. Examine the Immediate window.
 //---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace SetWorkingDirectory_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 doc;
         int fileerror;
         int filewarning;

         public void Main()
         {
             swApp.Visible = true;

             // Get the current working directory before opening the document
             Debug.Print("Current working directory is " + swApp.GetCurrentWorkingDirectory());

             doc = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\chair.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref fileerror, ref filewarning);

             // Opening a document with SldWorks::OpenDoc6 does not set the working directory
             Debug.Print("Current working directory is still " + swApp.GetCurrentWorkingDirectory());

             // Set the working directory to the document directory
             swApp.SetCurrentWorkingDirectory(doc.GetPathName().Substring(0, doc.GetPathName().LastIndexOf("\\")));

             Debug.Print("Current working directory is now " + swApp.GetCurrentWorkingDirectory());

         }

         public SldWorks swApp;

     }
 }
```
