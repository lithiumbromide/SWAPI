---
title: "CreateExtrusionSurface Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "CreateExtrusionSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateExtrusionSurface.html"
---

# CreateExtrusionSurface Method (IBody2)

Creates a new surface of extrusion (infinitely long tabulated cylinder).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateExtrusionSurface( _
   ByVal ProfileCurve As System.Object, _
   ByVal AxisDirection As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim ProfileCurve As System.Object
Dim AxisDirection As System.Object
Dim value As System.Object

value = instance.CreateExtrusionSurface(ProfileCurve, AxisDirection)
```

### C#

```csharp
System.object CreateExtrusionSurface(
   System.object ProfileCurve,
   System.object AxisDirection
)
```

### C++/CLI

```cpp
System.Object^ CreateExtrusionSurface(
   System.Object^ ProfileCurve,
   System.Object^ AxisDirection
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ProfileCurve`: Profile curve
- `AxisDirection`: Array of 3 doubles (x,y,z)

### Return Value

New surface of extrusion (tabulated cylinder)

## VBA Syntax

See [Body2::CreateExtrusionSurface](ms-its:sldworksapivb6.chm::/sldworks~Body2~CreateExtrusionSurface.html).

## Remarks

You can use this method with:

- A set of related functions that construct a body from trimmed surfaces. The profile curve is extruded along the direction vector of axis direction, the new surface being the envelope of the curve. The profile curve must be of type line, circle, or B-spline curve.
- Trimming curve creation routines (for example [ISurface::AddTrimmingLoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~AddTrimmingLoop2.html)) to construct a trimmed tabulated cylinder.

Any existing object created by this method is destroyed if you call this method again.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::ICreateExtrusionSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateExtrusionSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
