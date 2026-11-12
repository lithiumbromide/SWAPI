---
title: "Create Checks from Document Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "dsgnchkapi/Create_Checks_From_Document_Example_VBNET.htm"
---

# Create Checks from Document Example (VB.NET)

This example shows how to build Design Checker checks from existing SOLIDWORKS documents, templates, and drafting standards.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Load the SOLIDWORKS Design Checker add-in
 '    (click Tools > Add-ins > SOLIDWORKS Design Checker).
 ' 2. Ensure that the specified document exists.
  ' 3. Reference the SOLIDWORKS Design Checker primary interop assembly
 '   (in Project Explorer, right-click the project name, select
 '    Add Reference, click the Browse tab, navigate to the
 '    install_dir\api\redist folder and
 '    select SolidWorks.Interop.dsgnchk.dll).
 ' 4. Open an Immediate window.
 '
 ' Postconditions: SOLIDWORKS Design Checker launches and displays 27 checks
 ' that were added from the specified document.
 '
 ' NOTE: Because this drawing document is used by a SOLIDWORKS
 ' tutorial, do not save any changes when closing the document.
 '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.dsgnchk
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swDCAddIn As SWDesignCheck
         Dim retValue As Long

         ' Get the SOLIDWORKS Design Checker add-in
         ' Recommended to use the version-specific ProgID for your version of Design Checker
         ' e.g., "SWDesignChecker.SWDesignCheck.yyyy"; See the Remarks section in ISWDesignCheck help
         swDCAddIn = swApp.GetAddInObject("SWDesignChecker.SWDesignCheck")

         If swDCAddIn Is Nothing Then
             Debug.Print("No SOLIDWORKS Design Checker add-in.")
             Exit Sub
         End If

         ' Build Design Checker checks from a SOLIDWORKS drawing document
         retValue = swDCAddIn.CreateChecksFromSWFile("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\FoodProcessor.slddrw")

         Select Case retValue
             Case 0
                 Debug.Print("No errors running this report.")
             Case 1
                 Debug.Print("Report already exists.")
             Case 2
                 Debug.Print("Could not create report directory.")
             Case 3
                 Debug.Print("No active document.")
             Case 4
                 Debug.Print("Standards file does not exist.")
         End Select

     End Sub

     Public swApp As SldWorks

 End  Class
```
