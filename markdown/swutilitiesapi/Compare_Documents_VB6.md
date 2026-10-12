---
title: "Compare Documents Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swutilitiesapi/Compare_Documents_VB6.htm"
---

# Compare Documents Example (VBA)

This example shows how to compare the volumes of two parts and save the results of the comparison using the SOLIDWORKS Utilities API.

```
'------------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Utilities as an add-in
'    (in SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Utilities).
' 2. Add the SOLIDWORKS Utilities type library as a reference
'    (in the SOLIDWORKS Microsoft Visual Basic for Applications IDE, click
'    Tools > References > SolidWorks Utilities <version> Type Library).
' 3. Verify that the specified parts exist.
' 4. Verify that C:\test\ exists.
'
' Postconditions:
' 1. Creates the document comparison report, C:\test\Report\gtReportIndex.htm.
' 2. Gets document comparison statuses.
' 3. Examine C:\test\Report\gtReportIndex.htm.
'
' NOTE: Because the parts are used elsewhere, do not save changes.
'------------------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swapp As SldWorks.SldWorks
    Dim swUtil As SWUtilities.gtcocswUtilities
    Dim swUtilCompdoc As SWUtilities.gtcocswCompareDocument
    Dim longStatus As Long
    Dim bAddToBinder As Boolean
    Dim bOverwrite As Boolean
    Dim file1 As String
    Dim file2 As String
```

```
    ' Connect to SOLIDWORKS
    Set swapp = Application.SldWorks
```

```
   ' Get the SOLIDWORKS Utilities interface
    Set swUtil = swapp.GetAddInObject("Utilities.UtilitiesApp")
```

```
   ' Set the SOLIDWORKS Utilities tool to compare documents
    Set swUtilCompdoc = swUtil.GetToolInterface(gtSwToolCompDocs, 0)
```

```
    ' Compare the volumes of the specified part documents; do not show the Results
    ' dialog box, but do save the results to a file in the specified path
    file1 = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_a.sldprt"
    file2 = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_b.sldprt"
    bAddToBinder = False
    bOverwrite = True
    longStatus = swUtilCompdoc.CompareDocument2(file1, "", file2, "", gtCodVolumeCompare, gtResultSaveReport, "C:\test\Report", bAddToBinder, bOverwrite)
```

```
    ' Perform any necessary clean up
    longStatus = swUtilCompdoc.Close()
```

```
End Sub
```
