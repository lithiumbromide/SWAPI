---
title: "ShowShellin3D Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "ShowShellin3D"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~ShowShellin3D.html"
---

# ShowShellin3D Method (ICWPlot)

Sets whether to render the results on 3D shell bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowShellin3D( _
   ByVal BShowShellin3D As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim BShowShellin3D As System.Boolean
Dim value As System.Integer

value = instance.ShowShellin3D(BShowShellin3D)
```

### C#

```csharp
System.int ShowShellin3D(
   System.bool BShowShellin3D
)
```

### C++/CLI

```cpp
System.int ShowShellin3D(
   System.bool BShowShellin3D
)
```

### Parameters

- `BShowShellin3D`: True to render results on 3D shell bodies, false to not

### Return Value

Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

## VBA Syntax

See [CWPlot::ShowShellin3D](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~ShowShellin3D.html).

## Examples

See the [ICWPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html) examples.

## Remarks

This method is valid for the following plots only if [ICWPlot::ShowTensorOrVector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~ShowTensorOrVector.html) and [ICWPlot::ShowPlotOnSelEntities](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~ShowPlotOnSelEntities.html) are both false:

- Acceleration
- Displacement
- Mode shape/amplitude
- Strain
- Stress
- Velocity

## See Also

[ICWPlot Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
[ICWPlot Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
