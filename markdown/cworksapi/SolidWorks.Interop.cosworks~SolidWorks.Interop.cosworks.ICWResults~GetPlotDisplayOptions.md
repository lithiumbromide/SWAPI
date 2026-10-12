---
title: "GetPlotDisplayOptions Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetPlotDisplayOptions"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotDisplayOptions.html"
---

# GetPlotDisplayOptions Method (ICWResults)

Gets the display options for the specified plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPlotDisplayOptions( _
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

value = instance.GetPlotDisplayOptions(SPlotName, ErrorCode)
```

### C#

```csharp
System.object GetPlotDisplayOptions(
   System.string SPlotName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetPlotDisplayOptions(
   System.String^ SPlotName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SPlotName`: Plot name (see **Remarks**)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of display options (see **Remarks**)

## VBA Syntax

See [CWResults::GetPlotDisplayOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetPlotDisplayOptions.html).

## Examples

[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)

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
[ICWResults::SetPlotDisplayOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotDisplayOptions.html)
[ICWResults::GetPlotColorOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotColorOptions.html)
[ICWResults::GetPlotCount Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotCount.html)
[ICWResults::GetPlotPositionFormatOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotPositionFormatOptions.html)
[ICWResults::GetPlotSettings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotSettings.html)
[ICWResults::CreatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreatePlot.html)
[ICWResults::GetPlotSettingsOptionForHiddenAndExcludedBody Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotSettingsOptionForHiddenAndExcludedBody.html)
[ICWResults::CreateResultsEquationPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateResultsEquationPlot.html)
[ICWResults::GetPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlot.html)
[ICWResults::GetPlotDefinition Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotDefinition.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
