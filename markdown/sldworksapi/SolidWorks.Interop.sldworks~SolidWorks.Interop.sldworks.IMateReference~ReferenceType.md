---
title: "ReferenceType Property (IMateReference)"
project: "SOLIDWORKS API Help"
interface: "IMateReference"
member: "ReferenceType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~ReferenceType.html"
---

# ReferenceType Property (IMateReference)

Gets the mate type for the specified entity in this mate reference.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferenceType( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMateReference
Dim Index As System.Integer
Dim value As System.Integer

value = instance.ReferenceType(Index)
```

### C#

```csharp
System.int ReferenceType(
   System.int Index
) {get;}
```

### C++/CLI

```cpp
property System.int ReferenceType {
   System.int get(System.int Index);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Mate reference entity as defined by [swMateReferenceIndex_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceIndex_e.html)

### Property Value

Mate reference type as defined by [swMateReferenceType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceType_e.html)

## VBA Syntax

See [MateReference::ReferenceType](ms-its:sldworksapivb6.chm::/sldworks~MateReference~ReferenceType.html).

## Examples

[Get Mate Reference Properties (VBA)](Get_Mate_Reference_Properties_Example_VB.htm)
[Get Mate Reference Properties (VB.NET)](Get_Mate_Reference_Properties_Example_VBNET.htm)
[Get Mate Reference Properties (C#)](Get_Mate_Reference_Properties_Example_CSharp.htm)

## Remarks

Before calling this property, call [IMateReference::ReferenceEntityCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateReference~ReferenceEntityCount.html) to determine the number of mate reference entities for the mate reference.

This method returns -1 if there is no reference entity. See [IMateReference::ReferenceEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateReference~ReferenceEntity.html) for details.

## See Also

[IMateReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference.html)
[IMateReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
