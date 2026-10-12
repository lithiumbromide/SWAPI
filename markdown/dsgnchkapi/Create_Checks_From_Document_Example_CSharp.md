---
title: "Create Checks from Document Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "dsgnchkapi/Create_Checks_From_Document_Example_CSharp.htm"
---

# Create Checks from Document Example (C#)

This example shows how to build Design Checker checks from existing SOLIDWORKS documents, templates, and drafting standards.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Load the SOLIDWORKS Design Checker add-in
 //    (click Tools > Add-ins > SOLIDWORKS Design Checker).
 // 2. Ensure that the specified document exists.
 // 3.  Reference the SOLIDWORKS Design Checker primary interop assembly
 //    (in Project Explorer, right-click the project name, select
 //    Add Reference, click the Browse tab, navigate to the
 //    install_dir\api\redist folder and
 //     select SolidWorks.Interop.dsgnchk.dll).
 // 4. Rename the namespace of this macro to match the name of your C# project.
 // 5. Open an Immediate window.
 //
 // Postconditions: SOLIDWORKS Design Checker launches and displays 27 checks
 //   that were added from the specified document.
 //
 // NOTE: Because this drawing document is used by a SOLIDWORKS
 // tutorial, do not save any changes when closing the document.
 //---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using SolidWorks.Interop.dsgnchk;
 using System;
 using System.Diagnostics;
 namespace CreateChecksFromFile_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {

             SWDesignCheck swDCAddIn = default(SWDesignCheck);
             int retValue = 0;

             // Get the SOLIDWORKS Design Checker add-in
             // Recommended to use the version-specific ProgID for your version of Design Checker
             // e.g., "SWDesignChecker.SWDesignCheck.yyyy"; See the Remarks section in ISWDesignCheck help
             swDCAddIn = (SWDesignCheck)swApp.GetAddInObject("SWDesignChecker.SWDesignCheck");

             if (swDCAddIn == null)
             {
                 Debug.Print("No SOLIDWORKS Design Checker add-in.");
                 return;
             }

             // Build Design Checker checks from a SOLIDWORKS drawing document
             retValue = swDCAddIn.CreateChecksFromSWFile("C:\\Users\\Public\\Documents\\SOLIDWORKS\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\FoodProcessor.slddrw");

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
         }

         public SldWorks swApp;

     }
 }
```
