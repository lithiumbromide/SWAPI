---
title: "ActivatePlot Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "ActivatePlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~ActivatePlot.html"
---

# ActivatePlot Method (ICWResults)

Activates the specified plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function ActivatePlot( _
   ByVal PlotName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim PlotName As System.String
Dim value As System.Boolean

value = instance.ActivatePlot(PlotName)
```

### C#

```csharp
System.bool ActivatePlot(
   System.string PlotName
)
```

### C++/CLI

```cpp
System.bool ActivatePlot(
   System.String^ PlotName
)
```

### Parameters

- `PlotName`: Name of plot to activate (see **Remarks**)

### Return Value

True if the plot is activated, false if not

## VBA Syntax

See [CWResults::ActivatePlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~ActivatePlot.html).

## Remarks

Call [ICWResults::GetPlotNames](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWResults~GetPlotNames.html) to populate PlotName.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::DeletePlot Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~DeletePlot.html)
[ICWResults::GetPlotCount Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotCount.html)
[ICWResults::AddIsoClippingToPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~AddIsoClippingToPlot.html)
[ICWResults::SavePlotsAseDrawings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SavePlotsAseDrawings.html)
[ICWResults::CreatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreatePlot.html)
[ICWResults::CreateResultsEquationPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateResultsEquationPlot.html)
[ICWResults::GetPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlot.html)
[ICWResults::CreateStressHotSpotPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateStressHotSpotPlot.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
