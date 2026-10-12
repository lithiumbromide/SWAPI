---
title: "GetLegendContourColors Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetLegendContourColors"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetLegendContourColors.html"
---

# GetLegendContourColors Method (ICWResults)

Gets the contour colors based on user-input colors.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLegendContourColors( _
   ByVal SPlotName As System.String, _
   ByRef VarColor As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim SPlotName As System.String
Dim VarColor As System.Object
Dim value As System.Integer

value = instance.GetLegendContourColors(SPlotName, VarColor)
```

### C#

```csharp
System.int GetLegendContourColors(
   System.string SPlotName,
   out System.object VarColor
)
```

### C++/CLI

```cpp
System.int GetLegendContourColors(
   System.String^ SPlotName,
   [Out] System.Object^ VarColor
)
```

### Parameters

- `SPlotName`: Plot name (see **Remarks**)
- `VarColor`: Array of colors (see **Remarks**)

### Return Value

Result code as defined in [swsResultPlotColorOption_ErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotColorOption_ErrorCode_e.html)

## VBA Syntax

See [CWResults::GetLegendContourColors](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetLegendContourColors.html).

## Examples

[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)

## Remarks

Call [ICWResults::GetPlotNames](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWResults~GetPlotNames.html) to populate SPlotName.

VarColor contains an array of RGB triplets. Each triplet represents a computed legend color:

[

R[0,255] G[0,255] B[0,255]

...

]

If there are 14 colors in the legend, then the size of VarColor array is (14 * 3) = 42.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetPlotColorOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotColorOptions.html)
[ICWResults::GetPlotSettings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotSettings.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
