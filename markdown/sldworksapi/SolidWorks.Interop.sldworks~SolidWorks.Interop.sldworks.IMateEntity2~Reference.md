---
title: "Reference Property (IMateEntity2)"
project: "SOLIDWORKS API Help"
interface: "IMateEntity2"
member: "Reference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~Reference.html"
---

# Reference Property (IMateEntity2)

Gets the mate reference for this mate entity.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Reference As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMateEntity2
Dim value As System.Object

value = instance.Reference
```

### C#

```csharp
System.object Reference {get;}
```

### C++/CLI

```cpp
property System.Object^ Reference {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Mate reference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateReference.html)

## VBA Syntax

See [MateEntity2::Reference](ms-its:sldworksapivb6.chm::/sldworks~MateEntity2~Reference.html).

## Examples

[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)

## Remarks

Mate references can be one or more entities of a component used for automatic mating.

## See Also

[IMateEntity2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2.html)
[IMateEntity2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2_members.html)
[IMateEntity2::ReferenceComponent Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~ReferenceComponent.html)
[IMateEntity2::ReferenceType2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~ReferenceType2.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
