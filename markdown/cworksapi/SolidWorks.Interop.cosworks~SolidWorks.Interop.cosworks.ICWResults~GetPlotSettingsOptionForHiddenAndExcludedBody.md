---
title: "GetPlotSettingsOptionForHiddenAndExcludedBody Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetPlotSettingsOptionForHiddenAndExcludedBody"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotSettingsOptionForHiddenAndExcludedBody.html"
---

# GetPlotSettingsOptionForHiddenAndExcludedBody Method (ICWResults)

Gets hidden and excluded body options for the specified plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPlotSettingsOptionForHiddenAndExcludedBody( _
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

value = instance.GetPlotSettingsOptionForHiddenAndExcludedBody(SPlotName, ErrorCode)
```

### C#

```csharp
System.object GetPlotSettingsOptionForHiddenAndExcludedBody(
   System.string SPlotName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetPlotSettingsOptionForHiddenAndExcludedBody(
   System.String^ SPlotName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SPlotName`: Plot name (see **Remarks**)
- `ErrorCode`: Error code as defined in [swsPlotSettingsErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsPlotSettingsErrorCode_e.html)

### Return Value

Array of hidden and excluded body options (see **Remarks**)

## VBA Syntax

See [CWResults::GetPlotSettingsOptionForHiddenAndExcludedBody](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetPlotSettingsOptionForHiddenAndExcludedBody.html).

## Examples

[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)

## Remarks

Call [ICWResults::GetPlotNames](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotNames.html) to populate SPlotName.

The 0-based array contains 12 elements:

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
[ICWResults::GetPlotSettings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotSettings.html)
[ICWResults::SetPlotSettingsOptionForHiddenAndExcludedBody Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotSettingsOptionForHiddenAndExcludedBody.html)
[ICWResults::GetPlotColorOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotColorOptions.html)
[ICWResults::GetPlotCount Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotCount.html)
[ICWResults::GetPlotDisplayOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotDisplayOptions.html)
[ICWResults::GetPlotPositionFormatOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotPositionFormatOptions.html)
[ICWResults::CreatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreatePlot.html)
[ICWResults::CreateResultsEquationPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateResultsEquationPlot.html)
[ICWResults::GetPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlot.html)
[ICWResults::GetPlotDefinition Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotDefinition.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
