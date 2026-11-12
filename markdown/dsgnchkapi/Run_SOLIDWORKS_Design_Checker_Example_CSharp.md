---
title: "Run SOLIDWORKS Design Checker Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "dsgnchkapi/Run_SOLIDWORKS_Design_Checker_Example_CSharp.htm"
---

# Run SOLIDWORKS Design Checker Example (C#)

This example shows how to check the active document using the SOLIDWORKS Design Checker API.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 //
 // 1. Load the SOLIDWORKS Design Checker add-in
 //   (in SOLIDWORKS click Tools > Add-ins > SOLIDWORKS Design Checker).
 // 2. Create c:\test if needed.
 // 3. Ensure that the specified standards file and drawing document exist.
 // 4. Reference the SOLIDWORKS Design Checker primary interop assembly
 //    (in Project Explorer, right-click the project name, select
 //    Add Reference, click the Browse tab, navigate to the
 //    install_dir\api\redist folder and
 //    select SolidWorks.Interop.dsgnchk.dll).
 // 5. Rename the namespace of this macro to match the name of your C# project.
 // 6. Open an Immediate Window.
 //
 // Postconditions:
 //
 // 1. Design Binder displays in the FeatureManager design tree.
 // 2. SOLIDWORKS Design Checker checks the active model document against the
 //    specified standards file and creates a report as follows:
 //    a. If lReportFormat is 1 and Microsoft Word is installed,
 //       then c:\test\Food Processor\SWDCReport.doc is created,
 //       and lReportFormat = 1 is returned.
 //    b. If lReportFormat is 1 or 0 and Microsoft Word is not installed,
 //       then c:\test\Food processor\SWDCReport.xml is created.
 //       and lReportFormat = 0 is returned.
 // 3. Inspect the Immediate Window.
 //
 // Because AutoCorrect is false, ResultSummary contains failure counts delimited by '@':
 // Critical@High@Medium@Low
 //
 // If AutoCorrect is true, then ResultSummary contains both pre- and post-
 // correction failure counts delimited by '@':
 // Critical(pre)@High(pre)@Medium(pre)@Low(pre)@Critical(post)@High(post)@Medium(post)@Low(post)
 //
 // NOTE: Because the drawing document is used elsewhere, do not save changes.
 //---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.dsgnchk;
 using System;
 using System.Diagnostics;
 namespace RunDesignCheck5.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {

             SWDesignCheck swDCAddIn = default(SWDesignCheck);
             string StandardFileName = null;
             string ReportFolderName = null;
             long retValue = 0;
             bool AddtoDesignBinder = false;
             bool OverWriteReport = false;
             int warnings = 0;
             int errors = 0;
             bool AutoCorrect = false;
             string resultSummary = null;
             int lReportFormat = 0;

             // Get the SOLIDWORKS Design Checker add-in
             // Recommended to use the version-specific ProgID for your version of Design Checker
             // e.g., "SWDesignChecker.SWDesignCheck.yyyy"; See the Remarks section in ISWDesignCheck help
             swDCAddIn = (SWDesignCheck)swApp.GetAddInObject("SWDesignChecker.SWDesignCheck");

             if (swDCAddIn == null)
             {
                 Debug.Print("No SOLIDWORKS Design Checker add-in.");
                 return;
             }

             // Show the Design Binder in the FeatureManager design tree
             swApp.SetUserPreferenceIntegerValue((int)swUserPreferenceIntegerValue_e.swFeatureManagerDesignBinderVisibility, (int)swAutoHideShowResponse_e.swAutoHideShowResponse_Show);

             // Open the drawing document to check
             swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\FoodProcessor.slddrw", (int)swDocumentTypes_e.swDocDRAWING, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

             // Requirements file
             StandardFileName = "C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\dsgnchk\\data\\ansi.swstd";

             // Filename for report
             ReportFolderName = "c:\\test\\Food Processor";

             // Add report to Design Binder
             AddtoDesignBinder = true;

             // Overwrite any existing report
             OverWriteReport = true;

             // Do not autocorrect all failures
             AutoCorrect =  false;

             // Create report in MS Word format
             lReportFormat = 1;

             resultSummary = "";

             // Run SOLIDWORKS Design Checker on the active drawing document
             retValue = swDCAddIn.RunDesignCheck5(StandardFileName, ReportFolderName, AddtoDesignBinder, OverWriteReport, AutoCorrect, ref lReportFormat, out resultSummary);

             switch (retValue)
             {
                 case 0:
                     Debug.Print("No errors running this report.");
                     break;
                 case 1:
                     Debug.Print("Report already exists.");
                     break;
                 case 2:
                     Debug.Print("Could not create report directory.");
                     break;
                 case 3:
                     Debug.Print("No active document.");
                     break;
                 case 4:
                     Debug.Print("Standards file does not exist.");
                     break;
             }

             Debug.Print("SOLIDWORKS Design Checker result summary: " + resultSummary);
             Debug.Print("SOLIDWORKS Design Checker created report in format (0=XML, 1=MSWord): " + lReportFormat);

         }

         public SldWorks swApp;

     }
 }
```
