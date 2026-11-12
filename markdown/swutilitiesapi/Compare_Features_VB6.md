---
title: "Compare Features Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swutilitiesapi/Compare_Features_VB6.htm"
---

# Compare Features Example (VBA)

This example shows how to compare the solid features between the original and modified parts using the SOLIDWORKS Utilities API.

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
'
' 1. Creates a solid feature comparison report for the two parts,
'    C:\test\Report\gtReportIndex.htm.
' 2. Examine the graphics area and C:\test\Report\gtReportIndex.htm.
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
    Dim swUtilCompFeat As SWUtilities.gtcocswCompareFeature
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
    ' Set the SOLIDWORKS Utilities tool to compare features
     Set swUtilCompFeat = swUtil.GetToolInterface(gtSwToolFeatDiff, 0)
```

```
   ' Compare the volumes of the specified part documents; do not show the Results
    ' dialog box, but do save the results to a file in the specified path
    bAddToBinder = False
    bOverwrite = True
    file1 = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_a.sldprt"
    file2 = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_b.sldprt"
    longStatus = swUtilCompFeat.CompareFeatures2(file1, "", file2, "", gtResultSaveReport, "C:\test\Report", bAddToBinder, bOverwrite)
```

```
    ' Perform any necessary clean up
    longStatus = swUtilCompFeat.Close()
```

```
End Sub
```
