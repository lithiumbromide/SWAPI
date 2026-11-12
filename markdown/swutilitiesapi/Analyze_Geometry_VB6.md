---
title: "Analyze Geometry Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swutilitiesapi/Analyze_Geometry_VB6.htm"
---

# Analyze Geometry Example (VBA)

This example shows how to analyze the geometry of a part using the SOLIDWORKS Utilities API.

```
'------------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Utilities as an add-in
'    (in SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Utilities).
' 2. Add the SOLIDWORKS Utilities type library as a reference
'    (in the SOLIDWORKS Microsoft Visual Basic for Applications IDE, click
'    Tools > References > SolidWorks Utilities <version> Type Library).
' 3. Verify that C:\test\ exists.
' 4. Open a part.
'
' Postconditions:
' 1. Analyzes the geometry and creates a report,
'    C:\test\AnalyzeGeometry\gtReportIndex.htm.
' 2. Examine C:\test\AnalyzeGeometry\gtReportIndex.htm.
'------------------------------------------------------------------------------
Option Explicit
```

```
Dim swapp As SldWorks.SldWorks
Dim swUtil As SWUtilities.gtcocswUtilities
Dim swUtilGeometryAnalysis As SWUtilities.gtcocswGeometryAnalysis
Dim longStatus As gtError_e
```

```
Sub main()
```

```
    ' Connect to SOLIDWORKS
    Set swapp = Application.SldWorks
```

```
    ' Get the SOLIDWORKS Utilities interface
    Set swUtil = swapp.GetAddInObject("Utilities.UtilitiesApp")
    Set swUtilGeometryAnalysis = swUtil.GetToolInterface(gtSwToolGeomCheck, longStatus)
```

```
    ' Initiate the analysis
    longStatus = swUtilGeometryAnalysis.Init()
```

```
    ' Get the number of short edges
    Dim lShortEdgeCount As Long
    lShortEdgeCount = swUtilGeometryAnalysis.GetShortEdgesCount(0.0001, longStatus)
```

```
    ' Get the number of small faces
    Dim lSmallFaceCount As Long
    lSmallFaceCount = swUtilGeometryAnalysis.GetSmallFacesCount(0.0001, longStatus)
```

```
    ' Get the number of sliver faces
    Dim lSliverFaceCount As Long
    lSliverFaceCount = swUtilGeometryAnalysis.GetSliverFacesCount(0.0001, longStatus)
```

```
    ' Get the number of knife edges
    Dim lKnifeEdgecount As Long
    lKnifeEdgecount = swUtilGeometryAnalysis.GetKnifeEdgesCount(5#, longStatus)
```

```
    ' Get the number of knife vertices
    Dim lKnifeVertexCount As Long
    lKnifeVertexCount = swUtilGeometryAnalysis.GetKnifeVerticesCount(5#, longStatus)
```

```
    ' Get the number of discontinuous edges
    Dim lDiscontinuousEdgeCount As Long
    lDiscontinuousEdgeCount = swUtilGeometryAnalysis.GetDiscontinuousEdgesCount(longStatus)
```

```
    ' Get the number of discontinuous faces
    Dim lDiscontinuousFaceCount As Long
    lDiscontinuousFaceCount = swUtilGeometryAnalysis.GetDiscontinuousFacesCount(longStatus)
```

```
    ' Save the results to a file in the specified path
    longStatus = swUtilGeometryAnalysis.SaveReport2("C:\test\AnalyzeGeometry", False, True)
```

```
    ' Perform any necessary cleanup
    longStatus = swUtilGeometryAnalysis.Close()
```

```
End Sub
```
