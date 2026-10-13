---
title: "ICreateExtrusionSurface Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "ICreateExtrusionSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateExtrusionSurface.html"
---

# ICreateExtrusionSurface Method (IBody2)

Creates a new surface of extrusion (infinitely long tabulated cylinder).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateExtrusionSurface( _
   ByVal ProfileCurve As Curve, _
   ByVal AxisDirection As System.Object _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim ProfileCurve As Curve
Dim AxisDirection As System.Object
Dim value As Surface

value = instance.ICreateExtrusionSurface(ProfileCurve, AxisDirection)
```

### C#

```csharp
Surface ICreateExtrusionSurface(
   Curve ProfileCurve,
   System.object AxisDirection
)
```

### C++/CLI

```cpp
Surface^ ICreateExtrusionSurface(
   Curve^ ProfileCurve,
   System.Object^ AxisDirection
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ProfileCurve`: [ICurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html) object
- `AxisDirection`: Array of 3 doubles (x,y,z)

### Return Value

[ISurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html) object

## VBA Syntax

See [Body2::ICreateExtrusionSurface](ms-its:sldworksapivb6.chm::/sldworks~Body2~ICreateExtrusionSurface.html).

## Examples

[Create Imported Surface Body from Sketch (C#)](Create_Imported_Surface_Body_from_Sketch_Example_CSharp.htm)

## Remarks

You can use this method with:

- A set of related functions that construct a body from trimmed surfaces. The profile curve is extruded along the direction vector of axis direction, the new surface being the envelope of the curve. The profile curve must be of type line, circle, or B-spline curve.
- Trimming curve creation routines (for example [ISurface::IAddTrimmingLoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IAddTrimmingLoop2.html)) to construct a trimmed tabulated cylinder.

Any existing object created by this method is destroyed if you call this method again.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::CreateExtrusionSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateExtrusionSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
