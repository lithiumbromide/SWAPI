---
title: "MakeOffset Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "MakeOffset"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MakeOffset.html"
---

# MakeOffset Method (IBody2)

Creates a new temporary body by offsetting the selected surface body by the specified distance and in the specified direction.

## Syntax

### Visual Basic (Declaration)

```vb
Function MakeOffset( _
   ByVal Distance As System.Double, _
   ByVal Direction As System.Boolean _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Distance As System.Double
Dim Direction As System.Boolean
Dim value As Body2

value = instance.MakeOffset(Distance, Direction)
```

### C#

```csharp
Body2 MakeOffset(
   System.double Distance,
   System.bool Direction
)
```

### C++/CLI

```cpp
Body2^ MakeOffset(
   System.double Distance,
   System.bool Direction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Distance`: Distance by which to offset the selected surface body
- `Direction`: True to offset the selected surface body in the opposite direction, false to offset
  the surface body along the normal

### Return Value

Pointer to the newly created [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Body2::MakeOffset](ms-its:sldworksapivb6.chm::/sldworks~Body2~MakeOffset.html).

## Examples

[Create Temporary Bodies by Offsetting Surface Body (C#)](Create_Temporary_Bodies_by_Offsetting_Surface_Body_Example_CSharp.htm)
[Create Temporary Bodies by Offsetting Surface Body (VB.NET)](Create_Temporary_Bodies_by_Offsetting_Surface_Body_Example_VBNET.htm)
[Create Temporary Bodies By Offsetting a Surface Body (VBA)](Create_Temporary_Bodies_by_Offsetting_Surface_Body_Example_VB.htm)

## Remarks

This method only supports surface bodies.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
