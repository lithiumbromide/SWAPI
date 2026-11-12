---
title: "GetExtrusionsurfParams Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "GetExtrusionsurfParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetExtrusionsurfParams.html"
---

# GetExtrusionsurfParams Method (ISurface)

Gets the parameters for the extrusion surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExtrusionsurfParams() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Object

value = instance.GetExtrusionsurfParams()
```

### C#

```csharp
System.object GetExtrusionsurfParams()
```

### C++/CLI

```cpp
System.Object^ GetExtrusionsurfParams();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles giving extrusion surface parameters

## VBA Syntax

See [Surface::GetExtrusionsurfParams](ms-its:sldworksapivb6.chm::/sldworks~Surface~GetExtrusionsurfParams.html).

## Remarks

An extrusion surface is constructed by extruding a profile curve (line or arc or b-spline) along a direction vector. You can retrieve the profile curve for the extrusion using [ISurface::GetProfileCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~GetProfileCurve.html) or [ISurface::IGetProfileCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IGetProfileCurve.html).

Three doubles of parameters returned, `DirectionVector[3]`, which is the direction vector along which the profile curve is extruded.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::IGetExtrusionsurfParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetExtrusionsurfParams.html)
