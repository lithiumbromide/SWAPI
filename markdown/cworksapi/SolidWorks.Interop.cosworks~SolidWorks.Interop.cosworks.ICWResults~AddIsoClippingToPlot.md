---
title: "AddIsoClippingToPlot Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "AddIsoClippingToPlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~AddIsoClippingToPlot.html"
---

# AddIsoClippingToPlot Method (ICWResults)

Adds iso clipping to the specified result plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddIsoClippingToPlot( _
   ByVal PlotName As System.String, _
   ByVal NIsoPlanes As System.Integer, _
   ByVal IsoValues As System.Object, _
   ByVal BShowClipSurface As System.Boolean, _
   ByVal BShowCutUncut As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim PlotName As System.String
Dim NIsoPlanes As System.Integer
Dim IsoValues As System.Object
Dim BShowClipSurface As System.Boolean
Dim BShowCutUncut As System.Boolean
Dim value As System.Integer

value = instance.AddIsoClippingToPlot(PlotName, NIsoPlanes, IsoValues, BShowClipSurface, BShowCutUncut)
```

### C#

```csharp
System.int AddIsoClippingToPlot(
   System.string PlotName,
   System.int NIsoPlanes,
   System.object IsoValues,
   System.bool BShowClipSurface,
   System.bool BShowCutUncut
)
```

### C++/CLI

```cpp
System.int AddIsoClippingToPlot(
   System.String^ PlotName,
   System.int NIsoPlanes,
   System.Object^ IsoValues,
   System.bool BShowClipSurface,
   System.bool BShowCutUncut
)
```

### Parameters

- `PlotName`: Name of result plot to which to add iso clipping (see **Remarks**)
- `NIsoPlanes`: Number of values in IsoValues
- `IsoValues`: Array of values; each value corresponds to an iso surface to be plotted
- `BShowClipSurface`: True to plot on iso surface only, false to not
- `BShowCutUncut`: True to display result contours on the uncut portion of the model, false to display the uncut portion of the model in shaded view mode

### Return Value

Error as defined by [swsIsoClippingErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsIsoClippingErrorCode_e.html)

## VBA Syntax

See [CWResults::AddIsoClippingToPlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~AddIsoClippingToPlot.html).

## Remarks

Call [ICWResults::GetPlotNames](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotNames.html) or [ICWResults::IGetPlotNames](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~IGetPlotNames.html) to populate PlotName.

For stress plots, iso clipping is available for nodal values only.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::SavePlotsAseDrawings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SavePlotsAseDrawings.html)
[ICWResults::GetPlotCount Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotCount.html)
[ICWResults::CreatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreatePlot.html)
[ICWResults::SetPlotColorOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotColorOptions.html)
[ICWResults::SetPlotDisplayOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotDisplayOptions.html)
[ICWResults::SetPlotPositionFormatOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotPositionFormatOptions.html)
[ICWResults::SetPlotSettings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotSettings.html)
[ICWResults::SetPlotSettingsOptionForHiddenAndExcludedBody Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotSettingsOptionForHiddenAndExcludedBody.html)
[ICWResults::CreateResultsEquationPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateResultsEquationPlot.html)
[ICWResults::GetPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlot.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
