---
title: "GetUVBounds Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetUVBounds"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetUVBounds.html"
---

# GetUVBounds Method (IFace2)

Gets the values that describe the U, V bounds of this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUVBounds() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Object

value = instance.GetUVBounds()
```

### C#

```csharp
System.object GetUVBounds()
```

### C++/CLI

```cpp
System.Object^ GetUVBounds();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [Face2::GetUVBounds](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetUVBounds.html).

## Examples

[Create Trimmed Curve (VBA)](Return_Untrimmed_Curve_Example_VB.htm)
[Create Trimmed Curve (VB.NET)](Return_Untrimmed_Curve_Example_VBNET.htm)
[Create Trimmed Curve (C#)](Return_Untrimmed_Curve_Example_CSharp.htm)

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
[IFace2::IGetUVBounds Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetUVBounds.html)
[IBody2::GetProcessedBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBody2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
