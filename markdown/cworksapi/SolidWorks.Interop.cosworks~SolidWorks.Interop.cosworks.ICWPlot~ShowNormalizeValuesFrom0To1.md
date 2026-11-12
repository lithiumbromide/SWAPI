---
title: "ShowNormalizeValuesFrom0To1 Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "ShowNormalizeValuesFrom0To1"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~ShowNormalizeValuesFrom0To1.html"
---

# ShowNormalizeValuesFrom0To1 Method (ICWPlot)

Sets whether to normalize values from 0 to 1 in this plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowNormalizeValuesFrom0To1( _
   ByVal BNormalizeValuesFrom0To1 As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim BNormalizeValuesFrom0To1 As System.Boolean
Dim value As System.Integer

value = instance.ShowNormalizeValuesFrom0To1(BNormalizeValuesFrom0To1)
```

### C#

```csharp
System.int ShowNormalizeValuesFrom0To1(
   System.bool BNormalizeValuesFrom0To1
)
```

### C++/CLI

```cpp
System.int ShowNormalizeValuesFrom0To1(
   System.bool BNormalizeValuesFrom0To1
)
```

### Parameters

- `BNormalizeValuesFrom0To1`: True to normalize values from 0 to 1, false to not

### Return Value

Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

## VBA Syntax

See [CWPlot::ShowNormalizeValuesFrom0To1](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~ShowNormalizeValuesFrom0To1.html).

## Examples

See the [ICWPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html) examples.

## See Also

[ICWPlot Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
[ICWPlot Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
