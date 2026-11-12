---
title: "ICreateRuledSurface Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "ICreateRuledSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateRuledSurface.html"
---

# ICreateRuledSurface Method (IBody2)

Creates a ruled surface from the specified curves and apex point.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateRuledSurface( _
   ByVal Curve1 As Curve, _
   ByVal Curve2 As Curve, _
   ByRef ApexPoint As System.Double _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Curve1 As Curve
Dim Curve2 As Curve
Dim ApexPoint As System.Double
Dim value As Surface

value = instance.ICreateRuledSurface(Curve1, Curve2, ApexPoint)
```

### C#

```csharp
Surface ICreateRuledSurface(
   Curve Curve1,
   Curve Curve2,
   ref System.double ApexPoint
)
```

### C++/CLI

```cpp
Surface^ ICreateRuledSurface(
   Curve^ Curve1,
   Curve^ Curve2,
   System.double% ApexPoint
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Curve1`: Pointer to first [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)
- `Curve2`: Pointer to second [curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)
- `ApexPoint`: Array of 3 doubles (x, y, z) being the apex point

### Return Value

Pointer to ruled [surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html)

## VBA Syntax

See [Body2::ICreateRuledSurface](ms-its:sldworksapivb6.chm::/sldworks~Body2~ICreateRuledSurface.html).

## Remarks

Any existing object created by this method is destroyed if you call this method again.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::ICreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateRuledSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
