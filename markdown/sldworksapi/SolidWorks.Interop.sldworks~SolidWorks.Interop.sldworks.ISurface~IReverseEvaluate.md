---
title: "IReverseEvaluate Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IReverseEvaluate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IReverseEvaluate.html"
---

# IReverseEvaluate Method (ISurface)

Gets the UV parameters at the specified location, which must be on the surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function IReverseEvaluate( _
   ByVal PositionX As System.Double, _
   ByVal PositionY As System.Double, _
   ByVal PositionZ As System.Double _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim PositionX As System.Double
Dim PositionY As System.Double
Dim PositionZ As System.Double
Dim value As System.Double

value = instance.IReverseEvaluate(PositionX, PositionY, PositionZ)
```

### C#

```csharp
System.double IReverseEvaluate(
   System.double PositionX,
   System.double PositionY,
   System.double PositionZ
)
```

### C++/CLI

```cpp
System.double IReverseEvaluate(
   System.double PositionX,
   System.double PositionY,
   System.double PositionZ
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PositionX`: X position on the surface
- `PositionY`: Y position on the surface
- `PositionZ`: Z position on the surface

### Return Value

Array of doubles describing the UV parameters

## VBA Syntax

See [Surface::IReverseEvaluate](ms-its:sldworksapivb6.chm::/sldworks~Surface~IReverseEvaluate.html).

## Remarks

At parametric singularities, such as sphere poles, the non-degenerate parameter is returned as the lowest value in its range. To determine the UV range, call [ISurface::Parameterization](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~Parameterization.html) or [ISurface::IParameterization](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IParameterization.html).

[IFace2::ReverseEvaluate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~ReverseEvaluate.html) and [IFace2::IReverseEvaluate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IReverseEvaluate.html) return corrected UV parameters for periodic surfaces; thus, you should use either of these methods when dealing with periodic surfaces.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::ReverseEvaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ReverseEvaluate.html)
[ISurface::Evaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~Evaluate.html)
[ISurface::IEvaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IEvaluate.html)
[ISurface::IEvaluateAtPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IEvaluateAtPoint.html)
[ISurface::EvaluateAtPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~EvaluateAtPoint.html)
