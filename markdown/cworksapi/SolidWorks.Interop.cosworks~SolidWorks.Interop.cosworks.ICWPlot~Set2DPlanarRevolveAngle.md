---
title: "Set2DPlanarRevolveAngle Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "Set2DPlanarRevolveAngle"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~Set2DPlanarRevolveAngle.html"
---

# Set2DPlanarRevolveAngle Method (ICWPlot)

Sets the revolve angle of the 3D plot of a 2D Simplification study.

## Syntax

### Visual Basic (Declaration)

```vb
Function Set2DPlanarRevolveAngle( _
   ByVal D2DPlanarRevolveAngle As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim D2DPlanarRevolveAngle As System.Double
Dim value As System.Integer

value = instance.Set2DPlanarRevolveAngle(D2DPlanarRevolveAngle)
```

### C#

```csharp
System.int Set2DPlanarRevolveAngle(
   System.double D2DPlanarRevolveAngle
)
```

### C++/CLI

```cpp
System.int Set2DPlanarRevolveAngle(
   System.double D2DPlanarRevolveAngle
)
```

### Parameters

- `D2DPlanarRevolveAngle`: Angle of revolution about a selected axis to create the 3D plot

### Return Value

Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

## VBA Syntax

See [CWPlot::Set2DPlanarRevolveAngle](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~Set2DPlanarRevolveAngle.html).

## Examples

See the [ICWPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html) examples.

## Remarks

This method is valid only:

- for 2D Simplification axi-symmetric studies where the geometry, loads, and restraints are symmetric (360 degrees) about an axis.
- if [ICWPlot::ShowAs3DPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~ShowAs3DPlot.html) is set to true.

## See Also

[ICWPlot Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
[ICWPlot Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
