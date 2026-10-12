---
title: "SetPlotPositionFormatOptions Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "SetPlotPositionFormatOptions"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotPositionFormatOptions.html"
---

# SetPlotPositionFormatOptions Method (ICWResults)

Sets the position/format options for the specified plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPlotPositionFormatOptions( _
   ByVal SPlotName As System.String, _
   ByVal ArrayInput As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim SPlotName As System.String
Dim ArrayInput As System.Object
Dim value As System.Integer

value = instance.SetPlotPositionFormatOptions(SPlotName, ArrayInput)
```

### C#

```csharp
System.int SetPlotPositionFormatOptions(
   System.string SPlotName,
   System.object ArrayInput
)
```

### C++/CLI

```cpp
System.int SetPlotPositionFormatOptions(
   System.String^ SPlotName,
   System.Object^ ArrayInput
)
```

### Parameters

- `SPlotName`: Plot name (see **Remarks**)
- `ArrayInput`: Array of position/format options (see **Remarks**)

### Return Value

Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

## VBA Syntax

See [CWResults::SetPlotPositionFormatOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~SetPlotPositionFormatOptions.html).

## Remarks

Call [ICWResults::GetPlotNames](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotNames.html) to populate SPlotName.

The 0-based array contains eight elements:

| Array element... | Contains... |
| --- | --- |
| 0 | Double[0,1]; horizontal position from the left of the graphics area; percentage of the window width |
| 1 | Double[0,1]; vertical position from the top of the graphics area; percentage of the window height |
| 2 | Chart width option as defined in swsColorChartWidthOptionValue_e |
| 3 | Chart number format as defined in swsColorChartNumberFormatOptionValue_e |
| 4 | 0 <= Number of decimal places to display <= 16 |
| 5 | Boolean; whether to display chart numbers with a 1000 comma separator; valid only if array element 3 is swsColorChartNumberFormatOptionValue_e.swsColorChartNumberFormatFloating or swsColorChartNumberFormatOptionValue_e.swsColorChartNumberFormatGeneral |
| 6 | Boolean; whether to use different number format for small numbers (0.001 < \|x\| < 1000); valid only if array element 3 is swsColorChartNumberFormatOptionValue_e.swsColorChartNumberFormatScientific |
| 7 | Number format for small numbers as defined in swsColorNumberFormatUseDiffNumberFormatOptionValue_e ; valid only if array element 6 is true |

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetPlotPositionFormatOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotPositionFormatOptions.html)
[ICWResults::SetPlotColorOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotColorOptions.html)
[ICWResults::SetPlotDisplayOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotDisplayOptions.html)
[ICWResults::SetPlotSettings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotSettings.html)
[ICWResults::AddIsoClippingToPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~AddIsoClippingToPlot.html)
[ICWResults::CreatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreatePlot.html)
[ICWResults::SetPlotSettingsOptionForHiddenAndExcludedBody Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotSettingsOptionForHiddenAndExcludedBody.html)
[ICWResults::CreateResultsEquationPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateResultsEquationPlot.html)
[ICWResults::GetPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlot.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
