---
title: "ReferenceEntity Property (IMateReference)"
project: "SOLIDWORKS API Help"
interface: "IMateReference"
member: "ReferenceEntity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~ReferenceEntity.html"
---

# ReferenceEntity Property (IMateReference)

Obsolete. Superseded by [IMateReference::ReferenceEntity2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateReference~ReferenceEntity2.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferenceEntity( _
   ByVal Index As System.Integer _
) As Entity
```

### Visual Basic (Usage)

```vb
Dim instance As IMateReference
Dim Index As System.Integer
Dim value As Entity

value = instance.ReferenceEntity(Index)
```

### C#

```csharp
Entity ReferenceEntity(
   System.int Index
) {get;}
```

### C++/CLI

```cpp
property Entity^ ReferenceEntity {
   Entity^ get(System.int Index);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Mate reference entity as define by [swMateReferenceIndex_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceIndex_e.html)

### Property Value

[Entity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html)

## VBA Syntax

See [MateReference::ReferenceEntity](ms-its:sldworksapivb6.chm::/sldworks~MateReference~ReferenceEntity.html).

## Examples

[Get Mate Reference Properties (VBA)](Get_Mate_Reference_Properties_Example_VB.htm)

## Remarks

Before calling this property, call [IMateReference::ReferenceEntityCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateReference~ReferenceEntityCount.html) to determine the number of mate reference entities for the mate reference.

## See Also

[IMateReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference.html)
[IMateReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
