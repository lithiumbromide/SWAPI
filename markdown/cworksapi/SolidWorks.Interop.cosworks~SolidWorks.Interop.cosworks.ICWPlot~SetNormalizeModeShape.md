---
title: "SetNormalizeModeShape Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "SetNormalizeModeShape"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~SetNormalizeModeShape.html"
---

# SetNormalizeModeShape Method (ICWPlot)

Sets whether to normalize the mode shape of this plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetNormalizeModeShape( _
   ByVal BNormModeShape As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim BNormModeShape As System.Boolean
Dim value As System.Integer

value = instance.SetNormalizeModeShape(BNormModeShape)
```

### C#

```csharp
System.int SetNormalizeModeShape(
   System.bool BNormModeShape
)
```

### C++/CLI

```cpp
System.int SetNormalizeModeShape(
   System.bool BNormModeShape
)
```

### Parameters

- `BNormModeShape`: True to normalize the mode shape (maximum amplitude is 1), false to not

### Return Value

Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

## VBA Syntax

See [CWPlot::SetNormalizeModeShape](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~SetNormalizeModeShape.html).

## Examples

See the [ICWPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html) examples.

## Remarks

This method is valid only for amplitude plots.

## See Also

[ICWPlot Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
[ICWPlot Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot_members.html)
[ICWPlot::SetModeShape Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~SetModeShape.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
