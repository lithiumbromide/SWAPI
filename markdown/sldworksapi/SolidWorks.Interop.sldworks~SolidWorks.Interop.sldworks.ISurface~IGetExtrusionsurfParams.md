---
title: "IGetExtrusionsurfParams Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IGetExtrusionsurfParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetExtrusionsurfParams.html"
---

# IGetExtrusionsurfParams Method (ISurface)

Gets the parameters for the extrusion surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetExtrusionsurfParams() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Double

value = instance.IGetExtrusionsurfParams()
```

### C#

```csharp
System.double IGetExtrusionsurfParams()
```

### C++/CLI

```cpp
System.double IGetExtrusionsurfParams();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles giving extrusion surface parameters

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [Surface::IGetExtrusionsurfParams](ms-its:sldworksapivb6.chm::/sldworks~Surface~IGetExtrusionsurfParams.html).

## Remarks

An extrusion surface is constructed by extruding a profile curve (line or arc or b-spline) along a direction vector. You can retrieve the profile curve for the extrusion using [ISurface::GetProfileCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~GetProfileCurve.html) or [ISurface::IGetProfileCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IGetProfileCurve.html).

Three doubles of parameters returned, `DirectionVector[3]`, which is the direction vector along which the profile curve is extruded.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::GetExtrusionsurfParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetExtrusionsurfParams.html)
