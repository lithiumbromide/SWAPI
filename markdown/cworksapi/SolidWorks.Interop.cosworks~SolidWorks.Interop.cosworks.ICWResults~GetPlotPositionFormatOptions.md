---
title: "GetPlotPositionFormatOptions Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetPlotPositionFormatOptions"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotPositionFormatOptions.html"
---

# GetPlotPositionFormatOptions Method (ICWResults)

Gets the position format options for the specified plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPlotPositionFormatOptions( _
   ByVal SPlotName As System.String, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim SPlotName As System.String
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetPlotPositionFormatOptions(SPlotName, ErrorCode)
```

### C#

```csharp
System.object GetPlotPositionFormatOptions(
   System.string SPlotName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetPlotPositionFormatOptions(
   System.String^ SPlotName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SPlotName`: Plot name (see **Remarks**)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of plot position/format options (see **Remarks**)

## VBA Syntax

See [CWResults::GetPlotPositionFormatOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetPlotPositionFormatOptions.html).

## Examples

[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)

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
[ICWResults::SetPlotPositionFormatOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotPositionFormatOptions.html)
[ICWResults::GetPlotColorOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotColorOptions.html)
[ICWResults::GetPlotCount Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotCount.html)
[ICWResults::GetPlotDisplayOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotDisplayOptions.html)
[ICWResults::GetPlotSettings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotSettings.html)
[ICWResults::CreatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreatePlot.html)
[ICWResults::GetPlotSettingsOptionForHiddenAndExcludedBody Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotSettingsOptionForHiddenAndExcludedBody.html)
[ICWResults::CreateResultsEquationPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateResultsEquationPlot.html)
[ICWResults::GetPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlot.html)
[ICWResults::GetPlotDefinition Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotDefinition.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
