---
title: "ICreateRevolutionSurface Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "ICreateRevolutionSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateRevolutionSurface.html"
---

# ICreateRevolutionSurface Method (IBody2)

Creates a new surface of revolution.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateRevolutionSurface( _
   ByVal ProfileCurve As Curve, _
   ByVal AxisPoint As System.Object, _
   ByVal AxisDirection As System.Object, _
   ByVal ProfileEndPtParams As System.Object _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim ProfileCurve As Curve
Dim AxisPoint As System.Object
Dim AxisDirection As System.Object
Dim ProfileEndPtParams As System.Object
Dim value As Surface

value = instance.ICreateRevolutionSurface(ProfileCurve, AxisPoint, AxisDirection, ProfileEndPtParams)
```

### C#

```csharp
Surface ICreateRevolutionSurface(
   Curve ProfileCurve,
   System.object AxisPoint,
   System.object AxisDirection,
   System.object ProfileEndPtParams
)
```

### C++/CLI

```cpp
Surface^ ICreateRevolutionSurface(
   Curve^ ProfileCurve,
   System.Object^ AxisPoint,
   System.Object^ AxisDirection,
   System.Object^ ProfileEndPtParams
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ProfileCurve`: Profile curve (generatrix)
- `AxisPoint`: Array of 3 doubles (x,y,z)
- `AxisDirection`: Array of 3 doubles (x,y,z)
- `ProfileEndPtParams`: Array of 2 doubles (uStart,uEnd) (see **Remarks**)

### Return Value

Pointer to a new [surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html) of revolution

## VBA Syntax

See [Body2::ICreateRevolutionSurface](ms-its:sldworksapivb6.chm::/sldworks~Body2~ICreateRevolutionSurface.html).

## Remarks

You can use this method with:

- A set of related functions that construct a body from trimmed surfaces.
- Trimming curve creation routines (for example, [ISurface::IAddTrimmingLoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IAddTrimmingLoop2.html)) to construct a trimmed surface of revolution.

If you pass ProfileEndPtParams to this method, the surface is trimmed in the axial direction; otherwise, it is infinite. SOLIDWORKS closes the surface periodic ( period [0,2PI]) in the direction of revolution. The ProfileEndPtParams parameters indicate to SOLIDWORKS which part of the curve to spin. These parameters are used only when the profile curve intersects the revolve axis. You must pass the parameters in ascending order. SOLIDWORKS extends the curve from the given parameter range to meet the revolve axis and spins this portion of curve.

You can also pass an empty VARIANT object to ProfileEndPtParams; it cannot be NULL. You must define a variable of type VARIANT.

Any existing object created by this method is destroyed if you call this method again.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::CreateRevolutionSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateRevolutionSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
