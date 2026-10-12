---
title: "GetPlotName Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "GetPlotName"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~GetPlotName.html"
---

# GetPlotName Method (ICWPlot)

Gets the name of this plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPlotName( _
   ByRef SPlotName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim SPlotName As System.String
Dim value As System.Integer

value = instance.GetPlotName(SPlotName)
```

### C#

```csharp
System.int GetPlotName(
   out System.string SPlotName
)
```

### C++/CLI

```cpp
System.int GetPlotName(
   [Out] System.String^ SPlotName
)
```

### Parameters

- `SPlotName`: Plot name

### Return Value

Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

## VBA Syntax

See [CWPlot::GetPlotName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~GetPlotName.html).

## Examples

See the [ICWPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html) examples.

## See Also

[ICWPlot Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
[ICWPlot Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
