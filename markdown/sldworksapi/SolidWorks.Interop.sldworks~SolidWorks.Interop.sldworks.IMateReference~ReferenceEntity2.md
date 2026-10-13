---
title: "ReferenceEntity2 Property (IMateReference)"
project: "SOLIDWORKS API Help"
interface: "IMateReference"
member: "ReferenceEntity2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~ReferenceEntity2.html"
---

# ReferenceEntity2 Property (IMateReference)

Gets the specified mate entity in this mate reference.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferenceEntity2( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMateReference
Dim Index As System.Integer
Dim value As System.Object

value = instance.ReferenceEntity2(Index)
```

### C#

```csharp
System.object ReferenceEntity2(
   System.int Index
) {get;}
```

### C++/CLI

```cpp
property System.Object^ ReferenceEntity2 {
   System.Object^ get(System.int Index);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Mate reference entity as defined in [swMateReferenceIndex_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceIndex_e.html)

### Property Value

[IEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) or [ISketchPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) (see **Remarks**)

## VBA Syntax

See [MateReference::ReferenceEntity2](ms-its:sldworksapivb6.chm::/sldworks~MateReference~ReferenceEntity2.html).

## Examples

[Get Mate Reference Properties (VBA)](Get_Mate_Reference_Properties_Example_VB.htm)
[Get Mate Reference Properties (VB.NET)](Get_Mate_Reference_Properties_Example_VBNET.htm)
[Get Mate Reference Properties (C#)](Get_Mate_Reference_Properties_Example_CSharp.htm)

## Remarks

Before calling this property, call [IMateReference::ReferenceEntityCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateReference~ReferenceEntityCount.html) to determine the range of values for Index.

After calling this property, call [IMateReference::ReferenceEntityType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateReference~ReferenceEntityType.html) to determine which type this property returns and then cast the returned object into the appropriate type.

## See Also

[IMateReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference.html)
[IMateReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
