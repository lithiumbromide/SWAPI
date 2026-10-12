---
title: "Copy Document and Its Dependencies Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Copy_Document_and_Its_Dependencies_Example_CSharp.htm"
---

# Copy Document and Its Dependencies Example (C#)

This example shows how to copy a document and its dependencies to this macro's folder.

```vb
 //---------------------------------------------------------------------------
 // Preconditions: Open an assembly document.
 //
 // Postconditions:
 // 1. Closes the assembly document.
 // 2. Copies the assembly document and its dependencies to the macro folder.
 // 3. Examine the macro folder.
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
 namespace GetCurrentMacroPathName_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             string source = null;
             string target = null;
             string sourcefile = null;
             string tempfile = null;
             bool traverse = false;
             bool search = false;
             bool addreadonlyinfo = false;
             object[] depends = null;
             string[] sourcefiles = null;
             string[] targetfiles = null;
             int idx = 0;
             int sourcecount = 0;
             int copyopt = 0;
             int errors = 0;
             int lind = 0;
             ModelDoc2 doc = default(ModelDoc2);

             doc = (ModelDoc2)swApp.ActiveDoc;

             source = swApp.GetCurrentWorkingDirectory();
             sourcefile = doc.GetPathName();

             tempfile = swApp.GetCurrentMacroPathName();
             lind = tempfile.LastIndexOf("\\");
             target = tempfile.Substring(0, lind);

             traverse = true;
             search = true;
             addreadonlyinfo = false;

             depends = (object[])swApp.GetDocumentDependencies2(sourcefile, traverse, search, addreadonlyinfo);

             if ((depends == null))
                 return;

             idx = 1;

             while (idx <= depends.GetUpperBound(0))
             {
                 Array.Resize(ref sourcefiles, sourcecount + 1);
                 Array.Resize(ref targetfiles, sourcecount + 1);

                 sourcefiles[sourcecount] = (string)depends[idx];
                 lind = sourcefiles[sourcecount].LastIndexOf("\\");
                 targetfiles[sourcecount] = target + sourcefiles[sourcecount].Substring(lind, sourcefiles[sourcecount].Length - lind);

                 sourcecount = sourcecount + 1;
                 idx = idx + 2;
             }

             swApp.CloseAllDocuments(true);

             copyopt = (int)swMoveCopyOptions_e.swMoveCopyOptionsOverwriteExistingDocs;
             errors = swApp.CopyDocument(source + sourcefile, target + sourcefile, (sourcefiles), (targetfiles), (int)copyopt);

         }

         public SldWorks swApp;

     }
 }
```
