---
title: "ShowTensorOrVector Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "ShowTensorOrVector"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~ShowTensorOrVector.html"
---

# ShowTensorOrVector Method (ICWPlot)

Sets whether to render a vector or tensor plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowTensorOrVector( _
   ByVal BShowTensorOrVector As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim BShowTensorOrVector As System.Boolean
Dim value As System.Integer

value = instance.ShowTensorOrVector(BShowTensorOrVector)
```

### C#

```csharp
System.int ShowTensorOrVector(
   System.bool BShowTensorOrVector
)
```

### C++/CLI

```cpp
System.int ShowTensorOrVector(
   System.bool BShowTensorOrVector
)
```

### Parameters

- `BShowTensorOrVector`: True to render a tensor or vector plot, false to not

### Return Value

Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

## VBA Syntax

See [CWPlot::ShowTensorOrVector](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~ShowTensorOrVector.html).

## Examples

See the [ICWPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html) examples.

## Remarks

| If the results plot is for component... | And BShowTensorOrVector is... | Then the plot renders a... |
| --- | --- | --- |
| von Mises stress | True | Tensor of the three principal stresses at each node or element center |
| Directional stress, displacement, acceleration, or velocity | True | Vector of the magnitude and direction of the component at each node |
| Thermal resultant temperature gradient or resultant heat flux | True | Vector of the magnitude and direction of the component at each node |

## See Also

[ICWPlot Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
[ICWPlot Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
