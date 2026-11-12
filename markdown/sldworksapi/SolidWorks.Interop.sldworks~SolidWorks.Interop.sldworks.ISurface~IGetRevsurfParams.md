---
title: "IGetRevsurfParams Method (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "IGetRevsurfParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IGetRevsurfParams.html"
---

# IGetRevsurfParams Method (ISurface)

Gets the parameters for the surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetRevsurfParams() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Double

value = instance.IGetRevsurfParams()
```

### C#

```csharp
System.double IGetRevsurfParams()
```

### C++/CLI

```cpp
System.double IGetRevsurfParams();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

A surface of revolution is constructed by revolving a profile curve (line or arc or b-spline) about an axis. The profile curve for the surface of revolution can be retrieved with [ISurface::GetProfileCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~GetProfileCurve.html) or [ISurface::IGetProfileCurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IGetProfileCurve.html).

Eight doubles of parameters returned.

- Point [3] - X, Y, Z coordinates of the start point of the axis of rotation.
- AxisDir[3] - Vector showing the direction of the axis of rotation.
- Params[2] - Parameter range of the part of the profile curve that was used to create the surface.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::GetRevsurfParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~GetRevsurfParams.html)
