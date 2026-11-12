---
title: "Run Thickness Analysis Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swutilitiesapi/Run_Thickness_Analysis_VB6.htm"
---

# Run Thickness Analysis Example (VBA)

This example shows how to run a thickness analysis and generate reports using the SOLIDWORKS Utilities API.

```
'-----------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Utilities as an add-in
'    (in SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Utilities).
' 2. Add the SOLIDWORKS Utilities type library as a reference
'    (in the SOLIDWORKS Microsoft Visual Basic for Applications IDE, click
'    Tools > References > SolidWorks Utilities <version> Type Library).
' 3. Verify that the specified part exists.
' 4. Verify that c:\test exists.
'
' Postconditions:
' 1. Opens the part and runs a thin thickness analysis.
' 2. Adds the thickness analysis report to the Design Binder.
' 3. Saves the thickness analysis report to c:\test\report.
' 4. Examine the Immediate window, Design Binder, and c:\test\report\gtReportIndex.htm.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'------------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
```

```
Sub main()
```

```
    Dim swModel As SldWorks.ModelDoc2
    Dim utAddIn As SWUtilities.gtcocswUtilities
    Dim utThicknessAnalysis As SWUtilities.gtcocswThicknessAnalysis
    Dim nOption As SWUtilities.gtResultOptions_e
    Dim nResolution As SWUtilities.gttckResolutionOptions_e
    Dim strReportName As String
    Dim lStatus As Long
    Dim bAddToBinder As Boolean
    Dim bSaveToEdwg As Boolean
    Dim bOverWrite As Boolean
    Dim vCriticalFeatureNames As Variant
    Dim lIdx As Long
    Dim dRangeMin As Double
    Dim dRangeMax As Double
    Dim lNumFaces As Long
    Dim dSurfArea As Double
    Dim dPerAnalysisArea As Double
    Dim lNumRanges As Long
    Dim dThicknessLimit As Double
    Dim lErrors As Long
    Dim lWarnings As Long
    Dim sPart As String
```

```
    ' Connect to SOLIDWORKS
    Set swApp = Application.SldWorks
```

```
    ' Load the document for analysis
    sPart = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\introtosw\pressure_plate.sldprt"
    Set swModel = swApp.OpenDoc6(sPart, swDocPART, swOpenDocOptions_Silent, "", lErrors, lWarnings)
```

```
    ' Load the SOLIDWORKS Utilities add-in
    Set utAddIn = swApp.GetAddInObject("Utilities.UtilitiesApp")
```

```
    ' Get the thickness analysis tool
    Set utThicknessAnalysis = utAddIn.ThicknessAnalysis
```

```
    ' Initialize the thickness analysis tool
    lStatus = utThicknessAnalysis.Init()
    If lStatus <> gtNOErr Then
        Debug.Print "Thickness analysis tool could not be initialized: " & CStr(lStatus)
        Exit Sub
    End If
```

```
    ' Set the options
    ' Save the report
    nOption = gtResultSaveReport
```

```
    ' Use high resolution
    nResolution = gttckHighResolution
```

```
    ' Save the report to this folder
    strReportName = "c:\test\report"
```

```
    ' Add the report to the Design Binder
    bAddToBinder = True
```

```
    ' Do not save the report to eDrawings
    bSaveToEdwg = False
```

```
    ' Allow the report to be overwritten, both in Design Binder and
    ' on disk, so that you can rerun the analysis
    bOverWrite = True
```

```
    ' Set the thickness threshold
    dThicknessLimit = 0.025
```

```
    ' Run the analysis
    lStatus = utThicknessAnalysis.RunThinAnalysis2(dThicknessLimit, nResolution, nOption, strReportName, bAddToBinder, bSaveToEdwg, bOverWrite)
```

```
    ' Check the result
    If lStatus <> gtNOErr Then
        Debug.Print "Thickness analysis completed an with error: " & CStr(lStatus)
        ' Close the thickness analysis tool
        lStatus = utThicknessAnalysis.Close()
        ' Release
        Set utThicknessAnalysis = Nothing
        Set utAddIn = Nothing
        Exit Sub
    End If
```

```
    ' Get results
    Debug.Print "Total surface area analyzed              = " & CStr(utThicknessAnalysis.GetTotalSurfaceAreaAnalyzed(lStatus))
    Debug.Print "Critical area                            = " & CStr(utThicknessAnalysis.GetCriticalSurfaceArea(lStatus))
    Debug.Print "Maximum deviation                        = " & CStr(utThicknessAnalysis.GetMaxDeviationfromTargetThickness(lStatus))
    Debug.Print "Average weighted thickness critical area = " & CStr(utThicknessAnalysis.GetAvgWeightedTckOnCritArea(lStatus))
    Debug.Print "Average weighted thickness analyzed area = " & CStr(utThicknessAnalysis.GetAvgWeightedTckOnAnalArea(lStatus))
    Debug.Print "Number of critical faces                 = " & CStr(utThicknessAnalysis.GetNumCriticalFaces(lStatus))
    Debug.Print "Number of critical features              = " & CStr(utThicknessAnalysis.GetNumCriticalFeatures(lStatus))
    vCriticalFeatureNames = utThicknessAnalysis.GetCriticalFeatureNames(lStatus)
    If Not IsEmpty(vCriticalFeatureNames) Then
        Debug.Print "Critical features:"
        For lIdx = LBound(vCriticalFeatureNames) To UBound(vCriticalFeatureNames)
            Debug.Print "  " & vCriticalFeatureNames(lIdx)
        Next lIdx
    End If
```

```
    Debug.Print "Minimum thickness analyzed area          = " & CStr(utThicknessAnalysis.GetMinTckOnAnalArea(lStatus))
    Debug.Print "Maximum thickness analyzed area          = " & CStr(utThicknessAnalysis.GetMaxTckOnAnalArea(lStatus))
    lNumRanges = utThicknessAnalysis.GetIntervalCount(lStatus)
    Debug.Print "Number of intervals                      = " & lNumRanges; CStr(utThicknessAnalysis.GetIntervalCount(lStatus))
    For lIdx = 1 To lNumRanges
        Debug.Print "  #" & CStr(lIdx)
        lStatus = utThicknessAnalysis.GetAnalysisDetails(lIdx, dRangeMin, dRangeMax, lNumFaces, dSurfArea, dPerAnalysisArea)
        If lStatus <> gtNOErr Then
            Debug.Print "Could not obtain analysis details."
        Else
            Debug.Print "     min            = " & CStr(dRangeMin)
            Debug.Print "     max            = " & CStr(dRangeMax)
            Debug.Print "     #faces         = " & CStr(lNumFaces)
            Debug.Print "     surf area      = " & CStr(dSurfArea)
            Debug.Print "     %analyzed area = " & CStr(dPerAnalysisArea)
        End If
    Next lIdx
```

```
    ' Close the thickness analysis tool
    lStatus = utThicknessAnalysis.Close()
```

```
    ' Release
    Set utThicknessAnalysis = Nothing
    Set utAddIn = Nothing
```

```
    ' Done
    Exit Sub
```

```
End Sub
```
