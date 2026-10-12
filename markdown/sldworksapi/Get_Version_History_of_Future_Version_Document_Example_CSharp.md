---
title: "Get Version History of Future Version Document Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Version_History_of_Future_Version_Document_Example_CSharp.htm"
---

# Get Version History of Future Version Document Example (C#)

This example shows how to get the version history of a future version document.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Copy a future version part document to this macro's directory.
 // 2. Replace Part1.sldprt in the macro with the name
 //    of your future version part.
 // 3. Open an Immediate window.
 //
 // Postconditions:
 // 1. Does not throw swFileLoadError_e.swFutureVersion.
 // 2. Inspect the Immediate window for the version history of the document.
 // ---------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;

 namespace IsFutureVersion_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swDocument = default(ModelDoc2);
             ModelDocExtension swExtension = default(ModelDocExtension);
             int lErrors = 0;
             int lWarnings = 0;
             int lOptions = 0;
             string strFileName = null;
             object[] vVersionHistory = null;
             string strBaseVersion = null;
             string strCurrentVersion = null;
             string strHotFixes = null;
             string strRevisionNumber = null;
             int lDateCode = 0;
             string strFormatVersion = null;

             strFormatVersion = swApp.GetLatestSupportedFileVersion().ToString();

             strRevisionNumber = swApp.RevisionNumber();
             swApp.GetBuildNumbers2(out strBaseVersion, out strCurrentVersion, out strHotFixes);
             lDateCode = swApp.DateCode();

             Debug.Print("Format version = " + strFormatVersion);
             Debug.Print("RevisionNumber = " + strRevisionNumber);
             Debug.Print("BaseVersion    = " + strBaseVersion);
             Debug.Print("CurrentVersion = " + strCurrentVersion);
             Debug.Print("HotFixes       = " + strHotFixes);
             Debug.Print("DateCode       = " + lDateCode);

             swDocument = (ModelDoc2)swApp.ActiveDoc;

             if ((swDocument == null))
             {
                 strFileName = swApp.GetCurrentMacroPathFolder() + "\\Part1.sldprt";
                 lOptions = 0;
                 lOptions = lOptions | (int)swOpenDocOptions_e.swOpenDocOptions_Silent;
                 swDocument = swApp.OpenDoc6(strFileName, (int)swDocumentTypes_e.swDocPART, lOptions, "", ref lErrors, ref lWarnings);
                 Debug.Print("lErrors = " + lErrors);

                 // Starting with SW2012 SP5, loading future file versions
                 // is supported, so the future version error no longer occurs.
                 Debug.Print("  future version error = " + ((lErrors & (int)swFileLoadError_e.swFutureVersion) == (int)swFileLoadError_e.swFutureVersion));
                 Debug.Print("lWarnings = " + lWarnings);
             }

             if ((swDocument == null))
             {
                 Debug.Print("No model");
                 return;
             }

             strFileName = swDocument.GetPathName();
             Debug.Print("File = " + strFileName);
             swExtension = swDocument.Extension;

             // The version history of a future version document is the same
             // as that of the part/assembly template that is used to load it
             // into the older version of SOLIDWORKS Design. IModelDoc2::VersionHistory
             // returns the version history of the part template,
             // not the version history of the future version document.
             // Get the version history of a future version document from
             // its file on disk using SldWorks::VersionHistory.

             Debug.Print("Is future version = " + swExtension.IsFutureVersion());

             if ((!(swExtension.IsFutureVersion() ==  false)))
             {
                 vVersionHistory = (object[])swApp.VersionHistory(strFileName);
                 if (((vVersionHistory != null)))
                 {
                     Debug.Print("Version history from file:");
                     PrintVersionHistory(vVersionHistory);
                 }
             }

             vVersionHistory = (object[])swDocument.VersionHistory();

             if (((vVersionHistory != null)))
             {
                 Debug.Print("Version history from document:");
                 PrintVersionHistory(vVersionHistory);
             }

             Debug.Print("view-only      = " + swDocument.IsOpenedViewOnly());
             Debug.Print("read-only      = " + swDocument.IsOpenedReadOnly());
             Debug.Print("blocking state = " + BlockingState2String((swBlockingStates_e)swDocument.GetBlockingState()));

         }

         private void PrintVersionHistory(object[] vVersionHistory)
         {
             object[] vSplitResults = null;
             string strFormatVersion = null;
             string strDateCodes = null;
             string vDateCode = null;
             string vHistoryEntry = null;

             foreach (string vHistoryEntry_loopVariable in vVersionHistory)
             {
                 vHistoryEntry = vHistoryEntry_loopVariable;

                 Debug.Print("  " + vHistoryEntry);
                 vSplitResults = vHistoryEntry.Split('[');
                 strFormatVersion = (string)vSplitResults[0];
                 strDateCodes = vSplitResults[1].ToString().Replace(']', ' ');
                 vSplitResults = strDateCodes.Split(',');
                 Debug.Print("    format version = " + strFormatVersion);

                 foreach (string vDateCode_loopVariable in vSplitResults)
                 {
                     vDateCode = vDateCode_loopVariable;
                     Debug.Print("       datecode = " + vDateCode);
                 }

             }

         }

         private string BlockingState2String(swBlockingStates_e nBlockingState)
         {
             string functionReturnValue = null;

             switch ((nBlockingState))
             {
                 case swBlockingStates_e.swEditorBlock:
                     functionReturnValue =  "editor block";

                     break;

                 case swBlockingStates_e.swEditSketchBlock:
                     functionReturnValue =  "edit sketch block";

                     break;

                 case swBlockingStates_e.swFullBlock:
                     functionReturnValue =  "full block";

                     break;

                 case swBlockingStates_e.swModifyBlock:
                     functionReturnValue =  "modify block";

                     break;

                 case swBlockingStates_e.swNoBlock:
                     functionReturnValue =  "no block";

                     break;

                 case swBlockingStates_e.swPartialModifyBlock:
                     functionReturnValue =  "partial modify block";

                     break;

                 case swBlockingStates_e.swSystemBlock:
                     functionReturnValue =  "system block";

                     break;

                 case swBlockingStates_e.swViewOnlyBlock:
                     functionReturnValue =  "view only block";

                     break;

                 default:
                     functionReturnValue =  "<unknown blocking state>";

                     break;

             }
             return functionReturnValue;

         }

         public SldWorks swApp;

     }
 }
```
