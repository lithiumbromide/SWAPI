---
title: "DeletePlot Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "DeletePlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~DeletePlot.html"
---

# DeletePlot Method (ICWResults)

Deletes the specified plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeletePlot( _
   ByVal PlotName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim PlotName As System.String
Dim value As System.Boolean

value = instance.DeletePlot(PlotName)
```

### C#

```csharp
System.bool DeletePlot(
   System.string PlotName
)
```

### C++/CLI

```cpp
System.bool DeletePlot(
   System.String^ PlotName
)
```

### Parameters

- `PlotName`: Name of the plot to delete (see **Remarks**)

### Return Value

True if the plot is deleted, false if not

## VBA Syntax

See [CWResults::DeletePlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~DeletePlot.html).

## Remarks

Call [ICWResults::GetPlotNames](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWResults~GetPlotNames.html) to populate PlotName.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::ActivatePlot Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~ActivatePlot.html)
[ICWResults::GetPlotCount Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotCount.html)
[ICWResults::AddIsoClippingToPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~AddIsoClippingToPlot.html)
[ICWResults::SavePlotsAseDrawings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SavePlotsAseDrawings.html)
[ICWResults::CreatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreatePlot.html)
[ICWResults::CreateResultsEquationPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateResultsEquationPlot.html)
[ICWResults::GetPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlot.html)

## Availability

SolidWork Simulation API 2009 SP0
