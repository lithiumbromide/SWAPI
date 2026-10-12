---
title: "SetPlotColorOptions Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "SetPlotColorOptions"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotColorOptions.html"
---

# SetPlotColorOptions Method (ICWResults)

Sets the color options for the specified plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPlotColorOptions( _
   ByVal SPlotName As System.String, _
   ByVal NType As System.Integer, _
   ByVal NContour As System.Integer, _
   ByVal NBaseColor As System.Integer, _
   ByVal BFlip As System.Boolean, _
   ByVal BSpecifyColorLimit As System.Boolean, _
   ByVal VarColor As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim SPlotName As System.String
Dim NType As System.Integer
Dim NContour As System.Integer
Dim NBaseColor As System.Integer
Dim BFlip As System.Boolean
Dim BSpecifyColorLimit As System.Boolean
Dim VarColor As System.Object
Dim value As System.Integer

value = instance.SetPlotColorOptions(SPlotName, NType, NContour, NBaseColor, BFlip, BSpecifyColorLimit, VarColor)
```

### C#

```csharp
System.int SetPlotColorOptions(
   System.string SPlotName,
   System.int NType,
   System.int NContour,
   System.int NBaseColor,
   System.bool BFlip,
   System.bool BSpecifyColorLimit,
   System.object VarColor
)
```

### C++/CLI

```cpp
System.int SetPlotColorOptions(
   System.String^ SPlotName,
   System.int NType,
   System.int NContour,
   System.int NBaseColor,
   System.bool BFlip,
   System.bool BSpecifyColorLimit,
   System.Object^ VarColor
)
```

### Parameters

- `SPlotName`: Plot name (see **Remarks**)
- `NType`: Color map as defined in [swsColorChartOptionLegendTypeValue_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsColorChartOptionLegendTypeValue_e.html) (see **Remarks**)
- `NContour`: 2 <= Number of gradient colors <= 24
- `NBaseColor`: Number of base colors for NType; valid only if NType is swsColorChartOptionLegendTypeValue_e.swsColorChartOptionLegendUserDefined (see **Remarks**)
- `BFlip`: True to reverse the color mapping, false to not
- `BSpecifyColorLimit`: True to specify a color for values above the yield limit, false to not; valid only for von Mises stress plots of single body parts where the yield strength is defined
- `VarColor`: Array of RGB triplets:

  - RGB color for values above the yield limit; valid only if BSpecifyColorLimit is true
  - One or more RGB triplets of user-defined colors

### Return Value

Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

## VBA Syntax

See [CWResults::SetPlotColorOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~SetPlotColorOptions.html).

## Remarks

Call [ICWResults::GetPlotNames](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotNames.html) to populate SPlotName.

| If NType is swsColorChartOptionLegendTypeValue_e... | Then NBaseColor is... |
| --- | --- |
| swsColorChartOptionLegendDefault | 5 |
| swsColorChartOptionLegendRainbow | 7 |
| swsColorChartOptionLegendGrayScale | 2 |
| swsColorChartOptionLegendUserDefined | 2-9 |

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetPlotColorOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotColorOptions.html)
[ICWResults::SetPlotDisplayOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotDisplayOptions.html)
[ICWResults::SetPlotPositionFormatOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotPositionFormatOptions.html)
[ICWResults::SetPlotSettings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotSettings.html)
[ICWResults::AddIsoClippingToPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~AddIsoClippingToPlot.html)
[ICWResults::CreatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreatePlot.html)
[ICWResults::SetPlotSettingsOptionForHiddenAndExcludedBody Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotSettingsOptionForHiddenAndExcludedBody.html)
[ICWResults::CreateResultsEquationPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateResultsEquationPlot.html)
[ICWResults::GetPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlot.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
