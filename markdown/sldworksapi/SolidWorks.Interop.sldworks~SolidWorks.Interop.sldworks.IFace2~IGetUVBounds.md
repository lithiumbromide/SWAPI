---
title: "IGetUVBounds Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IGetUVBounds"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetUVBounds.html"
---

# IGetUVBounds Method (IFace2)

Gets the values that describe the U, V bounds of this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetUVBounds() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Double

value = instance.IGetUVBounds()
```

### C#

```csharp
System.double IGetUVBounds()
```

### C++/CLI

```cpp
System.double IGetUVBounds();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The return values bound an area of the surface in which the face is defined. You can determine the surface U, V bounds using [ISurface::Parameterization](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~Parameterization.html) or [ISurface::IParameterization](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IParameterization.html).

The returned data is an array of 4 doubles arranged in the following order:

retval[0] - Minimum U parameter of this face

retval[1] - Maximum U parameter of this face

retval[2] - Minimum V parameter of this face

retval[3] - Maximum V parameter of this face

The minimum parameters are always less than the maximum parameters, and the range (for example, retval[1] - retval[0] and retval[3]-retval[2]) is always less than or equal to the U and V range of the underlying surface.

For surfaces with periodic parameters, the face parameter box can never be larger than the period of the corresponding surface parameter.

uRange[0] <= retval[0] < uRange[1]

vRange[0] <= retval[2] < vRange[1]

where uRange and vRange describe the UV range of the surface

Therefore, a face that straddles the boundary of a periodic parameter has an upper parameter value for the face that is greater than the upper parameter range of the surface.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IBody2::GetProcessedBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBody2.html)
[IFace2::GetUVBounds Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetUVBounds.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
