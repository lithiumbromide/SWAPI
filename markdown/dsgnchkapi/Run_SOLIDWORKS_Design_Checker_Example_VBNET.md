---
title: "Run SOLIDWORKS Design Checker Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "dsgnchkapi/Run_SOLIDWORKS_Design_Checker_Example_VBNET.htm"
---

# Run SOLIDWORKS Design Checker Example (VB.NET)

This example shows how to check the active document using the SOLIDWORKS Design Checker API.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Load the SOLIDWORKS Design Checker add-in
 '    (in SOLIDWORKS click Tools > Add-ins > SOLIDWORKS Design Checker).
 ' 2. Create c:\test if needed.
 ' 3. Ensure that the specified standards file and drawing document exist.
 ' 4. Reference the SOLIDWORKS Design Checker primary interop assembly
 '   (in Project Explorer, right-click the project name, select
 '    Add Reference, click the Browse tab, navigate to the
 '    install_dir\api\redist folder and
 '    select SolidWorks.Interop.dsgnchk.dll).
 ' 5. In the IDE menu bar select Debug > Windows > Immediate.
 ' 6. Run this macro.
 '
 ' Postconditions:
 ' 1. Design Binder displays in the FeatureManager design tree.
 ' 2. SOLIDWORKS Design Checker checks the active model document
 '     against the specified standards file and creates a report as follows:
 '    a. If lReportFormat is 1 and Microsoft Word is installed,
 '        then c:\test\Food Processor\SWDCReport.doc is created,
 '       and lReportformat = 1 is returned.
 '    b. If lReportFormat is 1 or 0 and Microsoft Word is not installed,
 '       then c:\test\Food processor\SWDCReport.xml is created.
 '       and lReportFormat = 0 is returned.
 ' 3. Inspect the Immediate Window.
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
 ' NOTE: Because the drawing document is used elsewhere, do not save changes.
 '-----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.dsgnchk
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub Main()

         Dim swDCAddIn As SWDesignCheck
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

         ' Get the SOLIDWORKS Design Checker add-in
         ' Recommended to use the version-specific ProgID for your version of Design Checker
         ' e.g., "SWDesignChecker.SWDesignCheck.yyyy"; See the Remarks section in ISWDesignCheck help
         swDCAddIn = swApp.GetAddInObject("SWDesignChecker.SWDesignCheck")

         If swDCAddIn Is Nothing Then
             Debug.Print("No SOLIDWORKS Design Checker add-in.")
             Exit Sub
         End If

         ' Show the Design Binder in the FeatureManager design tree
         swApp.SetUserPreferenceIntegerValue(swUserPreferenceIntegerValue_e.swFeatureManagerDesignBinderVisibility, swAutoHideShowResponse_e.swAutoHideShowResponse_Show)

         ' Open the drawing document to check
         swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\FoodProcessor.slddrw", swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent,  "", errors, warnings)

         ' Requirements file
         StandardFileName =  "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\dsgnchk\data\ansi.swstd"

         ' Filename for report
         ReportFolderName =  "c:\test\Food Processor"

         ' Add report to Design Binder
         AddtoDesignBinder =  True

         ' Overwrite any existing report
         OverWriteReport =  True

         ' Do not autocorrect all failures
         AutoCorrect =  False

         ' Create report in MS Word format
         lReportFormat = 1

         resultSummary = ""

         ' Run SOLIDWORKS Design Checker on the active drawing document
         retValue = swDCAddIn.RunDesignCheck5(StandardFileName, ReportFolderName, AddtoDesignBinder, OverWriteReport, AutoCorrect, lReportFormat, resultSummary)

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

         Debug.Print("")
         Debug.Print("SOLIDWORKS Design Checker result summary:")
         Debug.Print("")
         Debug.Print(resultSummary)

         Debug.Print("")
         Debug.Print("SOLIDWORKS Design Checker created report in this format (0=XML, 1=MSWord): " & lReportFormat)

     End Sub

     Public swApp As SldWorks

 End Class
```
