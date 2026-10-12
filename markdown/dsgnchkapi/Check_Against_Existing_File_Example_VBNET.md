---
title: "Check Against Existing File Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "dsgnchkapi/Check_Against_Existing_File_Example_VBNET.htm"
---

# Check Against Existing File Example (VB.NET)

This example shows how to use the Design Checker API to check against an existing file.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Load the SOLIDWORKS Design Checker add-in
 '    (click Tools > Add-ins > SOLIDWORKS Design Checker).
 ' 2. Open a part document.
 ' 3. Reference the SOLIDWORKS Design Checker primary interop assembly
 '    (in Project Explorer, right-click the project name, select
 '    Add Reference, click the Browse tab, navigate to the
 '    install_dir\api\redist folder and
 '    select SolidWorks.Interop.dsgnchk.dll).
 ' 4. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Select Drawing (*.drw;*.slddrw) and
 '      public_documents\samples\tutorial\advdrawings\FoodProcessor.slddrw
 '     from the pop-up file dialog.
 ' 2. Check Builder launches and creates checks from the selected
 '     drawing document.
 ' 3. Design Checker uses the checks to validate the active document
 '     and posts its results on a tab in the SOLIDWORKS Task Pane.
 '---------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.dsgnchk
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swDCAddIn As SWDesignCheck

         ' Get the SOLIDWORKS Design Checker add-in
         ' Recommended to use the version-specific ProgID for your version of Design Checker
         ' e.g., "SWDesignChecker.SWDesignCheck.yyyy"; See the Remarks section in ISWDesignCheck help
         swDCAddIn = swApp.GetAddInObject("SWDesignChecker.SWDesignCheck")
         If swDCAddIn Is Nothing Then
             Debug.Print("No SOLIDWORKS Design Checker add-in.")
             Exit Sub
         End If

         ' Select file, build checks, and validate the active document
         swDCAddIn.CheckAgainstExistingFile()

     End Sub

     Public swApp As SldWorks

 End  Class
```
