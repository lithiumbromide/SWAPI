---
title: "MateEntity Method (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "MateEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~MateEntity.html"
---

# MateEntity Method (IMate2)

Gets an entity associated with a mate.

## Syntax

### Visual Basic (Declaration)

```vb
Function MateEntity( _
   ByVal Index As System.Integer _
) As MateEntity2
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim Index As System.Integer
Dim value As MateEntity2

value = instance.MateEntity(Index)
```

### C#

```csharp
MateEntity2 MateEntity(
   System.int Index
)
```

### C++/CLI

```cpp
MateEntity2^ MateEntity(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of the entity associated with the mate

### Return Value

[Mate entity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateEntity2.html)

## VBA Syntax

See [Mate2::MateEntity](ms-its:sldworksapivb6.chm::/sldworks~Mate2~MateEntity.html).

## Examples

[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)
[Get Mates and Mate Entities (C#)](Get_Mates_and_Mate_Entities_Example_CSharp.htm)
[Get Mates and Mate Entities (VB.NET)](Get_Mates_and_Mate_Entities_Example_VBNET.htm)
[Get Mates and Mate Entities (VBA)](Get_Mates_and_Mate_Entities_Example_VB.htm)

## Remarks

To get the number of entities for this mate, call [IMate2::GetMateEntityCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMate2~GetMateEntityCount.html).

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
