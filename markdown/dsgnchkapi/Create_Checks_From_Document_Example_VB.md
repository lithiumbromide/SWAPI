---
title: "Create Checks from Document Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "dsgnchkapi/Create_Checks_From_Document_Example_VB.htm"
---

# Create Checks from Document Example (VBA)

This example shows how to build Design Checker checks from existing SOLIDWORKS documents, templates, and drafting standards.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
' 1. Load the SOLIDWORKS Design Checker add-in
 '    (click Tools > Add-ins > SOLIDWORKS Design Checker).
 ' 2. Ensure that the specified document exists.
 ' 3. Reference the SOLIDWORKS Design Checker type library
 '    (in the IDE, click Tools > References > SOLIDWORKS Design
 '    Checker  <version> Type Library).
 ' 4. Open an Immediate window.
 '
 ' Postconditions: SOLIDWORKS Design Checker launches and displays 27 checks
 ' that were added from the specified document.
 '
 ' NOTE: Because this drawing document is used by a SOLIDWORKS
 ' tutorial, do not save any changes when closing the document.
 '----------------------------------------------------------------------------
Option Explicit

Sub main()
    Dim swApp As SldWorks.SldWorks
     Dim retValue As Long

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

    ' Build Design Checker checks from a SOLIDWORKS drawing document
     retValue = swDCAddIn.CreateChecksFromSWFile("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\FoodProcessor.slddrw")
    Select Case retValue
         Case 0
             Debug.Print "No errors running this report."
         Case 1
             Debug.Print "Report already exists."
         Case 2
             Debug.Print "Could not create report directory."
         Case 3
             Debug.Print "No active document."
         Case 4
             Debug.Print "Standards file does not exist."
     End Select

End Sub
```
