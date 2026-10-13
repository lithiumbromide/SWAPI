---
title: "OffsetPlanarWireBody Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "OffsetPlanarWireBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~OffsetPlanarWireBody.html"
---

# OffsetPlanarWireBody Method (IBody2)

Offsets a planar wire body in the normal plane by the specified distance.

## Syntax

### Visual Basic (Declaration)

```vb
Function OffsetPlanarWireBody( _
   ByVal Distance As System.Double, _
   ByVal Normal As MathVector, _
   ByVal Option As System.Integer _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Distance As System.Double
Dim Normal As MathVector
Dim Option As System.Integer
Dim value As Body2

value = instance.OffsetPlanarWireBody(Distance, Normal, Option)
```

### C#

```csharp
Body2 OffsetPlanarWireBody(
   System.double Distance,
   MathVector Normal,
   System.int Option
)
```

### C++/CLI

```cpp
Body2^ OffsetPlanarWireBody(
   System.double Distance,
   MathVector^ Normal,
   System.int Option
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Distance`: Distance by which to offset the planar wire body
- `Normal`: Plane normal
- `Option`: How to fill the gap between edges as defined in [swOffsetPlanarWireBodyOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swOffsetPlanarWireBodyOptions_e.html)

### Return Value

Pointer to the [IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) object

## VBA Syntax

See [Body2::OffsetPlanarWireBody](ms-its:sldworksapivb6.chm::/sldworks~Body2~OffsetPlanarWireBody.html).

## Remarks

The offset direction is determined by the direction of the first edge and the normal. For example, imagine that you are standing on the plane with normal pointing upwards and you are looking along the first edge, then the offset is to your right.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
