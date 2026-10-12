---
title: "GetMinMaxResultValues Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "GetMinMaxResultValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~GetMinMaxResultValues.html"
---

# GetMinMaxResultValues Method (ICWPlot)

Gets the minimum and maximum values in this plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMinMaxResultValues( _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetMinMaxResultValues(ErrorCode)
```

### C#

```csharp
System.object GetMinMaxResultValues(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetMinMaxResultValues(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

### Return Value

Array of minimum and maximum values (see **Remarks**)

## VBA Syntax

See [CWPlot::GetMinMaxResultValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~GetMinMaxResultValues.html).

## Examples

See the [ICWPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html) examples.

## Remarks

This method returns the following array:

{`node_with_minimum_value`, `minimum_value`, `node_with_maximum_value`, `maximum_value`},

where the nodes are integers, and the values are in scientific notation.

## See Also

[ICWPlot Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
[ICWPlot Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
