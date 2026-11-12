---
title: "Parameterization2 Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "Parameterization2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~Parameterization2.html"
---

# Parameterization2 Method (ISurface)

Gets the parameterization of the surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function Parameterization2() As SurfaceParameterizationData
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As SurfaceParameterizationData

value = instance.Parameterization2()
```

### C#

```csharp
SurfaceParameterizationData Parameterization2()
```

### C++/CLI

```cpp
SurfaceParameterizationData^ Parameterization2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

An [ISurfaceParameterizationData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceParameterizationData.html) object

## VBA Syntax

See [Surface::Parameterization2](ms-its:sldworksapivb6.chm::/sldworks~Surface~Parameterization2.html).

## Examples

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::IParameterization Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IParameterization.html)
[ISurface::Evaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~Evaluate.html)
[ISurface::EvaluateAtPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~EvaluateAtPoint.html)
[IEvaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IEvaluate.html)
[ISurface::IEvaluateAtPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IEvaluateAtPoint.html)
[ISurface::GetBSurfParams3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetBSurfParams3.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
