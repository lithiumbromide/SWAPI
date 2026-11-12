---
title: "SetPlotDisplayOptions Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "SetPlotDisplayOptions"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotDisplayOptions.html"
---

# SetPlotDisplayOptions Method (ICWResults)

Sets the display options for the specified plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPlotDisplayOptions( _
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

value = instance.SetPlotDisplayOptions(SPlotName, ArrayInput)
```

### C#

```csharp
System.int SetPlotDisplayOptions(
   System.string SPlotName,
   System.object ArrayInput
)
```

### C++/CLI

```cpp
System.int SetPlotDisplayOptions(
   System.String^ SPlotName,
   System.Object^ ArrayInput
)
```

### Parameters

- `SPlotName`: Plot name (see **Remarks**)
- `ArrayInput`: Array of plot display options (see **Remarks**)

### Return Value

Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

## VBA Syntax

See [CWResults::SetPlotDisplayOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~SetPlotDisplayOptions.html).

## Remarks

Call [ICWResults::GetPlotNames](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotNames.html) to populate SPlotName.

The 0-based array contains eight elements:

| Array element... | Contains... |
| --- | --- |
| 0 | Boolean; whether to display minimum value |
| 1 | Boolean; whether to display maximum value |
| 2 | Boolean; whether to display plot details |
| 3 | Boolean; whether to display plot legend |
| 4 | Boolean; whether to display minimum/maximum ranges only for parts |
| 5 | Boolean; whether to allow user-defined minimum/maximum values |
| 6 | Double; user-defined minimum value; valid only if array element 5 is true |
| 7 | Double; user-defined maximum value; valid only if array element 5 is true |

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetPlotDisplayOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotDisplayOptions.html)
[ICWResults::SetPlotColorOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotColorOptions.html)
[ICWResults::SetPlotPositionFormatOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotPositionFormatOptions.html)
[ICWResults::SetPlotSettings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotSettings.html)
[ICWResults::AddIsoClippingToPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~AddIsoClippingToPlot.html)
[ICWResults::CreatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreatePlot.html)
[ICWResults::SetPlotSettingsOptionForHiddenAndExcludedBody Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotSettingsOptionForHiddenAndExcludedBody.html)
[ICWResults::CreateResultsEquationPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateResultsEquationPlot.html)
[ICWResults::GetPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlot.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
