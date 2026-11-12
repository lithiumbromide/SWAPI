---
title: "ShowAs3DPlot Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "ShowAs3DPlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~ShowAs3DPlot.html"
---

# ShowAs3DPlot Method (ICWPlot)

Sets whether to render the 2D Simplification results in 3D.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowAs3DPlot( _
   ByVal BShowAs3D As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim BShowAs3D As System.Boolean
Dim value As System.Integer

value = instance.ShowAs3DPlot(BShowAs3D)
```

### C#

```csharp
System.int ShowAs3DPlot(
   System.bool BShowAs3D
)
```

### C++/CLI

```cpp
System.int ShowAs3DPlot(
   System.bool BShowAs3D
)
```

### Parameters

- `BShowAs3D`: True to render the results in 3D, false to not

### Return Value

Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

## VBA Syntax

See [CWPlot::ShowAs3DPlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~ShowAs3DPlot.html).

## Examples

See the [ICWPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html) examples.

## Remarks

This method is valid only for 2D Simplification studies.

Also call [ICWPlot::Set2DPlanarRevolveAngle](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~Set2DPlanarRevolveAngle.html) to set the angle of revolution to generate the 3D plot.

## See Also

[ICWPlot Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
[ICWPlot Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
