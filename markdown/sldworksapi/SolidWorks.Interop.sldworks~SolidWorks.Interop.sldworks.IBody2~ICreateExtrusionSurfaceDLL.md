---
title: "ICreateExtrusionSurfaceDLL Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "ICreateExtrusionSurfaceDLL"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateExtrusionSurfaceDLL.html"
---

# ICreateExtrusionSurfaceDLL Method (IBody2)

Creates an extruded surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateExtrusionSurfaceDLL( _
   ByVal ProfileCurve As Curve, _
   ByRef AxisDirection As System.Double _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim ProfileCurve As Curve
Dim AxisDirection As System.Double
Dim value As Surface

value = instance.ICreateExtrusionSurfaceDLL(ProfileCurve, AxisDirection)
```

### C#

```csharp
Surface ICreateExtrusionSurfaceDLL(
   Curve ProfileCurve,
   ref System.double AxisDirection
)
```

### C++/CLI

```cpp
Surface^ ICreateExtrusionSurfaceDLL(
   Curve^ ProfileCurve,
   System.double% AxisDirection
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ProfileCurve`: Pointer to the profile [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)
- `AxisDirection`: Array of 3 doubles (x,y,z)

### Return Value

Pointer to the new [surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html) of extrusion (tabulated cylinder)

## VBA Syntax

See [Body2::ICreateExtrusionSurfaceDLL](ms-its:sldworksapivb6.chm::/sldworks~Body2~ICreateExtrusionSurfaceDLL.html).

## Remarks

Any existing object created by this method is destroyed if you call this method again.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
