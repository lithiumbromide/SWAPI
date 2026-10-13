---
title: "GetRevsurfParams Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "GetRevsurfParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetRevsurfParams.html"
---

# GetRevsurfParams Method (ISurface)

Gets the parameters for the surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRevsurfParams() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Object

value = instance.GetRevsurfParams()
```

### C#

```csharp
System.object GetRevsurfParams()
```

### C++/CLI

```cpp
System.Object^ GetRevsurfParams();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [Surface::GetRevsurfParams](ms-its:sldworksapivb6.chm::/sldworks~Surface~GetRevsurfParams.html).

## Remarks

A surface of revolution is constructed by revolving a profile curve (line or arc or b-spline) about an axis. The profile curve for the surface of revolution can be retrieved with [ISurface::GetProfileCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~GetProfileCurve.html) or [ISurface::IGetProfileCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IGetProfileCurve.html).

Eight doubles of parameters returned.

- Point [3] - X, Y, Z coordinates of the start point of the axis of rotation.
- AxisDir[3] - Vector showing the direction of the axis of rotation.
- Params[2] - Parameter range of the part of the profile curve that was used to create the surface.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::IGetRevsurfParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetRevsurfParams.html)
