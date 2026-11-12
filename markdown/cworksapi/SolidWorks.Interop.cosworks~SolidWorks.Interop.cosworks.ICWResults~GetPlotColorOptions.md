---
title: "GetPlotColorOptions Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetPlotColorOptions"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotColorOptions.html"
---

# GetPlotColorOptions Method (ICWResults)

Gets the color options for the specified plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPlotColorOptions( _
   ByVal SPlotName As System.String, _
   ByRef NType As System.Integer, _
   ByRef NBaseColor As System.Integer, _
   ByRef NContour As System.Integer, _
   ByRef BFlip As System.Boolean, _
   ByRef BSpecifyColorLimit As System.Boolean, _
   ByRef VarColor As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim SPlotName As System.String
Dim NType As System.Integer
Dim NBaseColor As System.Integer
Dim NContour As System.Integer
Dim BFlip As System.Boolean
Dim BSpecifyColorLimit As System.Boolean
Dim VarColor As System.Object
Dim value As System.Integer

value = instance.GetPlotColorOptions(SPlotName, NType, NBaseColor, NContour, BFlip, BSpecifyColorLimit, VarColor)
```

### C#

```csharp
System.int GetPlotColorOptions(
   System.string SPlotName,
   out System.int NType,
   out System.int NBaseColor,
   out System.int NContour,
   out System.bool BFlip,
   out System.bool BSpecifyColorLimit,
   out System.object VarColor
)
```

### C++/CLI

```cpp
System.int GetPlotColorOptions(
   System.String^ SPlotName,
   [Out] System.int NType,
   [Out] System.int NBaseColor,
   [Out] System.int NContour,
   [Out] System.bool BFlip,
   [Out] System.bool BSpecifyColorLimit,
   [Out] System.Object^ VarColor
)
```

### Parameters

- `SPlotName`: Plot name (see **Remarks**)
- `NType`: Color map as defined in [swsColorChartOptionLegendTypeValue_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsColorChartOptionLegendTypeValue_e.html) (see **Remarks**)
- `NBaseColor`: Number of base colors in color map specified by NType (see **Remarks**)
- `NContour`: Number of gradient colors
- `BFlip`: True to reverse the color mapping, false to not
- `BSpecifyColorLimit`: True to specify a color for values above the yield limit, false to not; valid only for von Mises stress plots of single body parts where the yield strength is defined
- `VarColor`: Array of RGB triplets:

  - RGB color for values above the yield limit; valid only if BSpecifyColorLimit is true
  - One or more RGB triplets of user-defined colors

### Return Value

Error as defined in [swsResultsError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultsError_e.html)

## VBA Syntax

See [CWResults::GetPlotColorOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetPlotColorOptions.html).

## Examples

[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)

## Remarks

Call [ICWResults::GetPlotNames](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotNames.html) to populate SPlotName.

| If NType is swsColorChartOptionLegendTypeValue_e... | Then NBaseColor is... |
| --- | --- |
| swsColorChartOptionLegendDefault | 5 |
| swsColorChartOptionLegendRainbow | 7 |
| swsColorChartOptionLegendGrayScale | 2 |
| swsColorChartOptionLegendUserDefined | 2 - 9 |

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::SetPlotColorOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotColorOptions.html)
[ICWResults::GetPlotCount Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotCount.html)
[ICWResults::GetPlotDisplayOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotDisplayOptions.html)
[ICWResults::GetPlotPositionFormatOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotPositionFormatOptions.html)
[ICWResults::GetPlotSettings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotSettings.html)
[ICWResults::CreatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreatePlot.html)
[ICWResults::GetLegendContourColors Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetLegendContourColors.html)
[ICWResults::GetPlotSettingsOptionForHiddenAndExcludedBody Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotSettingsOptionForHiddenAndExcludedBody.html)
[ICWResults::CreateResultsEquationPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateResultsEquationPlot.html)
[ICWResults::GetPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlot.html)
[ICWResults::GetPlotDefinition Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotDefinition.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
