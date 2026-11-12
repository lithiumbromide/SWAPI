---
title: "GetPlot Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetPlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlot.html"
---

# GetPlot Method (ICWResults)

Gets the specified results plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPlot( _
   ByVal SPlotName As System.String, _
   ByRef ErrorCode As System.Integer _
) As CWPlot
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim SPlotName As System.String
Dim ErrorCode As System.Integer
Dim value As CWPlot

value = instance.GetPlot(SPlotName, ErrorCode)
```

### C#

```csharp
CWPlot GetPlot(
   System.string SPlotName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWPlot^ GetPlot(
   System.String^ SPlotName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SPlotName`: Name of results plot (see **Remarks**)
- `ErrorCode`: Error code as defined by [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

### Return Value

[ICWPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)

## VBA Syntax

See [CWResults::GetPlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetPlot.html).

## Examples

[Create a Design Insight Plot for a Static Study (VBA)](Create_Design_Insight_Plot_for_Static_Study_Example_VB.htm)
[Create a Design Insight Plot for a Static Study (VB.NET)](Create_Design_Insight_Plot_for_Static_Study_Example_VBNET.htm)
[Create a Design Insight Plot for a Static Study (C#)](Create_Design_Insight_Plot_for_Static_Study_Example_CSharp.htm)

## Remarks

Call [ICWResults::GetPlotNames](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotNames.html) to populate SPlotName.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::CreatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreatePlot.html)
[ICWResults::CreateResultsEquationPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateResultsEquationPlot.html)
[ICWResults::DeletePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~DeletePlot.html)
[ICWResults::ActivatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~ActivatePlot.html)
[ICWResults::AddIsoClippingToPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~AddIsoClippingToPlot.html)
[ICWResults::GetPlotColorOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotColorOptions.html)
[ICWResults::GetPlotCount Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotCount.html)
[ICWResults::GetPlotDisplayOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotDisplayOptions.html)
[ICWResults::GetPlotPositionFormatOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotPositionFormatOptions.html)
[ICWResults::GetPlotSettings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotSettings.html)
[ICWResults::GetPlotSettingsOptionForHiddenAndExcludedBody Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotSettingsOptionForHiddenAndExcludedBody.html)
[ICWResults::SavePlotsAseDrawings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SavePlotsAseDrawings.html)
[ICWResults::SetPlotColorOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotColorOptions.html)
[ICWResults::SetPlotDisplayOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotDisplayOptions.html)
[ICWResults::SetPlotPositionFormatOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotPositionFormatOptions.html)
[ICWResults::SetPlotSettings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotSettings.html)
[ICWResults::SetPlotSettingsOptionForHiddenAndExcludedBody Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotSettingsOptionForHiddenAndExcludedBody.html)
[ICWResults::GetPlotDefinition Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotDefinition.html)
[ICWResults::CreateStressHotSpotPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateStressHotSpotPlot.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
