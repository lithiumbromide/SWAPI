---
title: "SetPlotSettingsOptionForHiddenAndExcludedBody Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "SetPlotSettingsOptionForHiddenAndExcludedBody"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotSettingsOptionForHiddenAndExcludedBody.html"
---

# SetPlotSettingsOptionForHiddenAndExcludedBody Method (ICWResults)

Sets hidden and excluded body options for the specified plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPlotSettingsOptionForHiddenAndExcludedBody( _
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

value = instance.SetPlotSettingsOptionForHiddenAndExcludedBody(SPlotName, ArrayInput)
```

### C#

```csharp
System.int SetPlotSettingsOptionForHiddenAndExcludedBody(
   System.string SPlotName,
   System.object ArrayInput
)
```

### C++/CLI

```cpp
System.int SetPlotSettingsOptionForHiddenAndExcludedBody(
   System.String^ SPlotName,
   System.Object^ ArrayInput
)
```

### Parameters

- `SPlotName`: Plot name (see **Remarks**)
- `ArrayInput`: Array of hidden and excluded body options (see **Remarks**)

### Return Value

Error code as defined in [swsPlotSettingsErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsPlotSettingsErrorCode_e.html)

## VBA Syntax

See [CWResults::SetPlotSettingsOptionForHiddenAndExcludedBody](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~SetPlotSettingsOptionForHiddenAndExcludedBody.html).

## Examples

[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)

## Remarks

Call [ICWResults::GetPlotNames](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotNames.html) to populate SPlotName.

ArrayInput is a 0-based array that contains 12 elements:

| Array element... | Contains... |
| --- | --- |
| 0 | Boolean; whether to show hidden bodies |
| 1 | Hidden body translucent color option as defined in swsPlotShowHiddenBodiesOptionValue_e ; valid only if array element 0 is true |
| 2 | R[0-255] value for single translucent color; valid only if array element 0 is true, and array element 1 is swsPlotShowHiddenBodiesOptionValue_e.swsPlotHiddenBodyTranslucentSingleColor |
| 3 | G[0-255] value for single translucent color; valid only if array element 0 is true, and array element 1 is swsPlotShowHiddenBodiesOptionValue_e.swsPlotHiddenBodyTranslucentSingleColor |
| 4 | B[0-255] value for single translucent color; valid only if array element 0 is true, and array element 1 is swsPlotShowHiddenBodiesOptionValue_e.swsPlotHiddenBodyTranslucentSingleColor |
| 5 | 0.0 <= transparency or intensity of the translucent single color or part colors <= 1.0; valid only if array element 0 is true |
| 6 | Boolean; whether to show excluded bodies |
| 7 | Excluded body translucent color option as defined in swsPlotShowExcludedBodiesOptionValue_e ; valid only if array element 6 is true |
| 8 | R[0-255] value for single translucent color; valid only if array element 6 is true, and array element 7 is swsPlotShowExcludedBodiesOptionValue_e.swsPlotExcludedBodyTranslucentSingleColor |
| 9 | G[0-255] value for single translucent color; valid only if array element 6 is true, and array element 7 is swsPlotShowExcludedBodiesOptionValue_e.swsPlotExcludedBodyTranslucentSingleColor |
| 10 | B[0-255] value for single translucent color; valid only if array element 6 is true, and array element 7 is swsPlotShowExcludedBodiesOptionValue_e.swsPlotExcludedBodyTranslucentSingleColor |
| 11 | 0.0 <= transparency or intensity of the translucent single color or part colors <= 1.0; valid only if array element 6 is true |

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::SetPlotSettings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotSettings.html)
[ICWResults::GetPlotSettingsOptionForHiddenAndExcludedBody Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotSettingsOptionForHiddenAndExcludedBody.html)
[ICWResults::SavePlotsAseDrawings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SavePlotsAseDrawings.html)
[ICWResults::SetPlotColorOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotColorOptions.html)
[ICWResults::SetPlotDisplayOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotDisplayOptions.html)
[ICWResults::SetPlotPositionFormatOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotPositionFormatOptions.html)
[ICWResults::CreatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreatePlot.html)
[ICWResults::AddIsoClippingToPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~AddIsoClippingToPlot.html)
[ICWResults::CreateResultsEquationPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateResultsEquationPlot.html)
[ICWResults::GetPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlot.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
