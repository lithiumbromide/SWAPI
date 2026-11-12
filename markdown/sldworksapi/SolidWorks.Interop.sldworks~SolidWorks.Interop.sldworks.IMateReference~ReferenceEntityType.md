---
title: "ReferenceEntityType Property (IMateReference)"
project: "SOLIDWORKS API Help"
interface: "IMateReference"
member: "ReferenceEntityType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~ReferenceEntityType.html"
---

# ReferenceEntityType Property (IMateReference)

Gets the exact entity type returned by [IMateReference::ReferenceEntity2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateReference~ReferenceEntity2.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferenceEntityType( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMateReference
Dim Index As System.Integer
Dim value As System.Integer

value = instance.ReferenceEntityType(Index)
```

### C#

```csharp
System.int ReferenceEntityType(
   System.int Index
) {get;}
```

### C++/CLI

```cpp
property System.int ReferenceEntityType {
   System.int get(System.int Index);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Mate reference entity as defined in [swMateReferenceIndex_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceIndex_e.html)

### Property Value

Value as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [MateReference::ReferenceEntityType](ms-its:sldworksapivb6.chm::/sldworks~MateReference~ReferenceEntityType.html).

## Examples

[Get Mate Reference Properties (VBA)](Get_Mate_Reference_Properties_Example_VB.htm)
[Get Mate Reference Properties (VB.NET)](Get_Mate_Reference_Properties_Example_VBNET.htm)
[Get Mate Reference Properties (C#)](Get_Mate_Reference_Properties_Example_CSharp.htm)

## Remarks

Call this property to determine the type returned by [IMateReference::ReferenceEntity2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateReference~ReferenceEntity2.html). Then cast the object returned by IMateReference::ReferenceEntity2 into the appropriate type.

## See Also

[IMateReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference.html)
[IMateReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
