---
title: "Check Against Existing File Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "dsgnchkapi/Check_Against_Existing_File_Example_VB.htm"
---

# Check Against Existing File Example (VBA)

This example shows how to use the Design Checker API to check against an existing file.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
'  1. Load the SOLIDWORKS Design Checker add-in
 '     (click Tools > Add-ins > SOLIDWORKS Design Checker).
 '  2. Open a part document.
 '  3. Reference the SOLIDWORKS Design Checker type library
 '     (in the IDE, click Tools > References > SOLIDWORKS Design
 '     Checker  <version> Type Library).
 '  4. Open the Immediate window.
 '
 ' Postconditions:
 '  1. Select Drawing (*.drw;*.slddrw) and
 '     public_documents\samples\tutorial\advdrawings\FoodProcessor.slddrw
 '     from the pop-up file dialog.
 '  2. Check Builder launches and creates checks from the selected
 '     drawing document.
 '  3. Design Checker uses the checks to validate the active document
 '     and posts its results on a tab in the SOLIDWORKS Task Pane.
 '----------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp As SldWorks.SldWorks
     Dim swDCAddIn  As DesignCheckerLib.SWDesignCheck
    ' Get the SOLIDWORKS application
     Set swApp = Application.SldWorks
    ' Get the SOLIDWORKS Design Checker add-in
     ' Recommended to use the version-specific ProgID for your version of Design Checker
     ' e.g., "SWDesignChecker.SWDesignCheck.yyyy"; See the Remarks section in ISWDesignCheck help
     Set swDCAddIn = swApp.GetAddInObject("SWDesignChecker.SWDesignCheck")
    If swDCAddIn Is Nothing Then
           Debug.Print "No SOLIDWORKS Design Checker add-in."
           Exit Sub
     End If

    ' Select file, build checks, and validate the active document
     swDCAddIn.CheckAgainstExistingFile

End Sub
```
