---
title: "CreateImportedResultsPlot Method (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "CreateImportedResultsPlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~CreateImportedResultsPlot.html"
---

# CreateImportedResultsPlot Method (ICWStudy)

Creates a plot for this study using the specified external results file.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateImportedResultsPlot( _
   ByVal SExternalResultFile As System.String, _
   ByVal SLegendTitle As System.String, _
   ByVal BValueByElem As System.Boolean, _
   ByRef ErrorCode As System.Integer _
) As CWPlot
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim SExternalResultFile As System.String
Dim SLegendTitle As System.String
Dim BValueByElem As System.Boolean
Dim ErrorCode As System.Integer
Dim value As CWPlot

value = instance.CreateImportedResultsPlot(SExternalResultFile, SLegendTitle, BValueByElem, ErrorCode)
```

### C#

```csharp
CWPlot CreateImportedResultsPlot(
   System.string SExternalResultFile,
   System.string SLegendTitle,
   System.bool BValueByElem,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWPlot^ CreateImportedResultsPlot(
   System.String^ SExternalResultFile,
   System.String^ SLegendTitle,
   System.bool BValueByElem,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SExternalResultFile`: Full pathname of the ***.csv** results file
- `SLegendTitle`: Legend title of the plot
- `BValueByElem`: True if SExternalResultFile contains element data, false if it contains nodal data
- `ErrorCode`: Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

### Return Value

[ICWPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)

## VBA Syntax

See [CWStudy::CreateImportedResultsPlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~CreateImportedResultsPlot.html).

## Examples

```
'VBA
```

```
...
```

```
Set aPlot = Study.CreateImportedResultsPlot("D:\tmp\22297\Parts\Element_data.csv", "Element Data", True, errCode)
If aPlot Is Nothing Then
    Select Case errCode
        Case cwResultPlot_InvalidStudy
            ErrorMsg SwApp, "Study is missing important internal components"
        Case cwResultPlot_FailedPlotCreation
            ErrorMsg SwApp, "Plot not created"
        Case cwResultPlot_InvalidResultType
            ErrorMsg SwApp, "Invalid result type"
        Case cwResultPlot_CosworksViewNotPresent
            ErrorMsg SwApp, "CosmosWorks view is not present"
        Case cwResultPlot_InvalidExternalResultsFile
            ErrorMsg SwApp, "External results file is not in the prescribed format"
        Case cwResultPlot_InvalidIsoValueRange
            ErrorMsg SwApp, "Iso value is out of range, Range is [0,1]"
        Case cwResultPlot_InvalidSmoothingCycleRange
            ErrorMsg SwApp, "Smoothing cycle value is out of range, range is [0,10]"
        Case cwResultPlot_MeshInformationNotFound
            ErrorMsg SwApp, "Mesh is not current, remesh and rerun the macro"
      End Select
```

```
End If
```

```
...
```

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
