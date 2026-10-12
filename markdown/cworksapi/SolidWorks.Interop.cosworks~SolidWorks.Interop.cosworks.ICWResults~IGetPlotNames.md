---
title: "IGetPlotNames Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "IGetPlotNames"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~IGetPlotNames.html"
---

# IGetPlotNames Method (ICWResults)

Gets the names of the plots in this study.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPlotNames( _
   ByVal Count As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim Count As System.Integer
Dim value As System.String

value = instance.IGetPlotNames(Count)
```

### C#

```csharp
System.string IGetPlotNames(
   System.int Count
)
```

### C++/CLI

```cpp
System.String^ IGetPlotNames(
   System.int Count
)
```

### Parameters

- `Count`: Number of plots in this study

### Return Value

Array of the names of the plots in this study

## VBA Syntax

See [CWResults::IGetPlotNames](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~IGetPlotNames.html).

## Remarks

Before calling this method, call [ICWResults::GetPlotCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWResults~GetPlotCount.html) to determine the size of the array.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetPlotNames Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotNames.html)
[ICWResults::ActivatePlot Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~ActivatePlot.html)
[ICWResults::DeletePlot Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~DeletePlot.html)
[ICWResults::SavePlotsAseDrawings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SavePlotsAseDrawings.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
