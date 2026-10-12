---
title: "SetPlotSettings Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "SetPlotSettings"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotSettings.html"
---

# SetPlotSettings Method (ICWResults)

Sets various settings for the specified plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPlotSettings( _
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

value = instance.SetPlotSettings(SPlotName, ArrayInput)
```

### C#

```csharp
System.int SetPlotSettings(
   System.string SPlotName,
   System.object ArrayInput
)
```

### C++/CLI

```cpp
System.int SetPlotSettings(
   System.String^ SPlotName,
   System.Object^ ArrayInput
)
```

### Parameters

- `SPlotName`: Plot name (see **Remarks**)
- `ArrayInput`: Array of plot settings (see **Remarks**)

### Return Value

Error code as defined in [swsPlotSettingsErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsPlotSettingsErrorCode_e.html)

## VBA Syntax

See [CWResults::SetPlotSettings](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~SetPlotSettings.html).

## Remarks

Call [ICWResults::GetPlotNames](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotNames.html) to populate SPlotName.

The 0-based array contains 11 elements:

| Array element... | Contains... |
| --- | --- |
| 0 | Display option for active fringe plot as defined in swsPlotFringeSettingsOptionValue_e |
| 1 | Display option for model boundary as defined in swsPlotBoundarySettingsOptionValue_e |
| 2 | R[0-255] value for model/mesh color; valid only if array element 1 is not swsPlotBoundarySettingsOptionValue_e.swsPlotBoundaryNone |
| 3 | G[0-255] value for model/mesh color; valid only if array element 1 is not swsPlotBoundarySettingsOptionValue_e.swsPlotBoundaryNone |
| 4 | B[0-255] value for model/mesh color; valid only if array element 1 is not swsPlotBoundarySettingsOptionValue_e.swsPlotBoundaryNone |
| 5 | Boolean; whether to superimpose the undeformed model on the deformed model |
| 6 | Deformed plot translucent color option as defined in swsPlotDeformedShapeOptionSuperImposeValue_e ; valid only if array element 5 is true |
| 7 | R[0-255] value for single translucent color; valid only if array elmeent 5 is true, and array element 6 is swsPlotDeformedShapeOptionSuperImposeValue_e.swsPlotDeformedShapeSuperImposeModel_TranslucentSingleColor |
| 8 | G[0-255] value for single translucent color; valid only if array element 5 is true, and array element 6 is swsPlotDeformedShapeOptionSuperImposeValue_e.swsPlotDeformedShapeSuperImposeModel_TranslucentSingleColor |
| 9 | B[0-255] value for single translucent color; valid only if array element 5 is true, and array element 6 is swsPlotDeformedShapeOptionSuperImposeValue_e.swsPlotDeformedShapeSuperImposeModel_TranslucentSingleColor |
| 10 | 0.0 <= Transparency or intensity of the translucent single color or part colors <= 1.0; valid only if array element 5 is true |

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetPlotSettings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotSettings.html)
[ICWResults::SetPlotColorOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotColorOptions.html)
[ICWResults::SetPlotDisplayOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotDisplayOptions.html)
[ICWResults::SetPlotPositionFormatOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotPositionFormatOptions.html)
[ICWResults::AddIsoClippingToPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~AddIsoClippingToPlot.html)
[ICWResults::CreatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreatePlot.html)
[ICWResults::SetPlotSettingsOptionForHiddenAndExcludedBody Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotSettingsOptionForHiddenAndExcludedBody.html)
[ICWResults::CreateResultsEquationPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateResultsEquationPlot.html)
[ICWResults::GetPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlot.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
