---
title: "AddDefaultOptimizationStudyPlot Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "AddDefaultOptimizationStudyPlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~AddDefaultOptimizationStudyPlot.html"
---

# AddDefaultOptimizationStudyPlot Method (ICWModelDoc)

Specifies a default optimization study result plot for the active document.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddDefaultOptimizationStudyPlot( _
   ByVal NOptimizationResultType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWModelDoc
Dim NOptimizationResultType As System.Integer
Dim value As System.Integer

value = instance.AddDefaultOptimizationStudyPlot(NOptimizationResultType)
```

### C#

```csharp
System.int AddDefaultOptimizationStudyPlot(
   System.int NOptimizationResultType
)
```

### C++/CLI

```cpp
System.int AddDefaultOptimizationStudyPlot(
   System.int NOptimizationResultType
)
```

### Parameters

- `NOptimizationResultType`: Type of optimization study result to plot as defined by [swsOptimizationStudyResultType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsOptimizationStudyResultType_e.html)

### Return Value

Error code as defined by [swsDefaultOptimizationDesignStudyPlotResultError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsAddDefaultOptimizationDesignStudyPlotResultError_e.html)

## VBA Syntax

See [CWModelDoc::AddDefaultOptimizationStudyPlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~AddDefaultOptimizationStudyPlot.html).

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
