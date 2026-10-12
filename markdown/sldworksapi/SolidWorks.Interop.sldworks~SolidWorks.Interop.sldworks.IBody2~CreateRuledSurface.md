---
title: "CreateRuledSurface Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "CreateRuledSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateRuledSurface.html"
---

# CreateRuledSurface Method (IBody2)

Creates a ruled surface from the specified curves and apex point.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateRuledSurface( _
   ByVal Curve1 As System.Object, _
   ByVal Curve2 As System.Object, _
   ByVal ApexPoint As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Curve1 As System.Object
Dim Curve2 As System.Object
Dim ApexPoint As System.Object
Dim value As System.Object

value = instance.CreateRuledSurface(Curve1, Curve2, ApexPoint)
```

### C#

```csharp
System.object CreateRuledSurface(
   System.object Curve1,
   System.object Curve2,
   System.object ApexPoint
)
```

### C++/CLI

```cpp
System.Object^ CreateRuledSurface(
   System.Object^ Curve1,
   System.Object^ Curve2,
   System.Object^ ApexPoint
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Curve1`: First curve
- `Curve2`: Second curve
- `ApexPoint`: Array of 3 doubles (x, y, z), the apex point

### Return Value

Pointer to ruled [surface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html)

## VBA Syntax

See [Body2::CreateRuledSurface](ms-its:sldworksapivb6.chm::/sldworks~Body2~CreateRuledSurface.html).

## Remarks

Any existing object created by this method is destroyed if you call this method again.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::ICreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateRuledSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
