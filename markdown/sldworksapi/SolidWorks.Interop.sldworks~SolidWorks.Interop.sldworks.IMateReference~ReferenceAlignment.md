---
title: "ReferenceAlignment Property (IMateReference)"
project: "SOLIDWORKS API Help"
interface: "IMateReference"
member: "ReferenceAlignment"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~ReferenceAlignment.html"
---

# ReferenceAlignment Property (IMateReference)

Gets the mate reference alignment for the specified mate reference entity in the selected mate reference.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferenceAlignment( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMateReference
Dim Index As System.Integer
Dim value As System.Integer

value = instance.ReferenceAlignment(Index)
```

### C#

```csharp
System.int ReferenceAlignment(
   System.int Index
) {get;}
```

### C++/CLI

```cpp
property System.int ReferenceAlignment {
   System.int get(System.int Index);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Mate reference entity as defined by [swMateReferenceIndex_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceIndex_e.html)

### Property Value

Type of alignment as defined by [swMateReferenceAlignment_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceAlignment_e.html)

## VBA Syntax

See [MateReference::ReferenceAlignment](ms-its:sldworksapivb6.chm::/sldworks~MateReference~ReferenceAlignment.html).

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
