---
title: "Run SOLIDWORKS Design Checker Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "dsgnchkapi/Run_SOLIDWORKS_Design_Checker_Example_VB.htm"
---

# Run SOLIDWORKS Design Checker Example (VBA)

This example shows how to check the active document using the SOLIDWORKS Design Checker API.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
'  1. Load the SOLIDWORKS Design Checker add-in
 '     (click Tools > Add-ins > SOLIDWORKS Design Checker).
 '  2. Create c:\test if needed.
 '  3. Ensure that the specified standards file and drawing document exist.
 '  4. Reference the SOLIDWORKS Design Checker type library
 '     (in the IDE, click Tools > References > SOLIDWORKS Design
 '     Checker <version> Type Library).
 '  5. Open an Immediate window.
 '  6. Run this macro.
 '
 ' Postconditions:
'  1. Design Binder displays in the FeatureManager design tree.
 '  2. SOLIDWORKS Design Checker checks the active model document against
 '     the specified standards file and creates a report as follows:
 '     a. If lReportFormat is 1 and Microsoft Word is installed,
 '        then c:\test\Food Processor\SWDCReport.doc is created,
 '        and lReportFormat = 1 is returned.
 '     b. If lReportFormat is 1 or 0 and Microsoft Word is not installed,
 '        then c:\test\Food processor\SWDCReport.xml is created.
 '        and lReportFormat = 0 is returned.
 '  3. Inspect the Immediate Window.
 '
 ' Because AutoCorrect is false, ResultSummary contains failure counts delimited by '@':
 '
 ' Critical@High@Medium@Low
 '
 ' If AutoCorrect is true, then ResultSummary contains both pre- and post-
 ' correction failure counts delimited by '@':
 '
 ' Critical(pre)@High(pre)@Medium(pre)@Low(pre)@Critical(post)@High(post)@Medium(post)@Low(post)
 '
 ' NOTE: Because the drawing document is elsewhere, do not save changes.
 '---------------------------------------------------------------------------
Option Explicit

Sub main()
    Dim swApp As SldWorks.SldWorks
     Dim swDCAddIn  As DesignCheckerLib.SWDesignCheck
     Dim StandardFileName As String
     Dim ReportFolderName As String
     Dim retValue As Long
     Dim AddtoDesignBinder As Boolean
     Dim OverWriteReport As Boolean
     Dim warnings As Long
     Dim errors As Long
     Dim AutoCorrect As Boolean
     Dim resultSummary As String
     Dim lReportFormat As Long
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

    ' Show the Design Binder in the FeatureManager design tree
     swApp.SetUserPreferenceIntegerValue swFeatureManagerDesignBinderVisibility, swAutoHideShowResponse_Show
    ' Open the drawing document to check
     swApp.OpenDoc6 "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\FoodProcessor.slddrw", swDocDRAWING, swOpenDocOptions_Silent, "", errors, warnings
    ' Requirements file
     StandardFileName = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\dsgnchk\data\iso.swstd"
    ' Filename for report
     ReportFolderName = "c:\test\Food Processor"
    ' Add report to Design Binder
     AddtoDesignBinder = True
    ' Overwrite any existing report
     OverWriteReport = True
    ' Do not autocorrect all failures
     AutoCorrect = False

    ' Create the report in MS Word format, if supported
     lReportFormat = 1
    ' Run SOLIDWORKS Design Checker on the active drawing document
     retValue = swDCAddIn.RunDesignCheck5(StandardFileName, ReportFolderName, AddtoDesignBinder, OverWriteReport, AutoCorrect, lReportFormat, resultSummary)
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
 Debug.Print ""
  Debug.Print "Design Check result summary:"
  Debug.Print ""
  Debug.Print resultSummary

 Debug.Print "Design Check report created in format (0 for XML, 1 for MS Word):"
  Debug.Print ""
  Debug.Print lReportFormat
End Sub
```
