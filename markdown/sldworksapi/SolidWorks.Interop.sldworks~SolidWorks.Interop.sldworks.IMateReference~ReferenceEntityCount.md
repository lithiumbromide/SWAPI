---
title: "ReferenceEntityCount Property (IMateReference)"
project: "SOLIDWORKS API Help"
interface: "IMateReference"
member: "ReferenceEntityCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~ReferenceEntityCount.html"
---

# ReferenceEntityCount Property (IMateReference)

Gets the number of mate reference entities for the selected mate reference.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferenceEntityCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMateReference
Dim value As System.Integer

value = instance.ReferenceEntityCount
```

### C#

```csharp
System.int ReferenceEntityCount {get;}
```

### C++/CLI

```cpp
property System.int ReferenceEntityCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of mate reference entities

## VBA Syntax

See [MateReference::ReferenceEntityCount](ms-its:sldworksapivb6.chm::/sldworks~MateReference~ReferenceEntityCount.html).

## Examples

[Get Mate Reference Properties (VBA)](Get_Mate_Reference_Properties_Example_VB.htm)
[Get Mate Reference Properties (VB.NET)](Get_Mate_Reference_Properties_Example_VBNET.htm)
[Get Mate Reference Properties (C#)](Get_Mate_Reference_Properties_Example_CSharp.htm)

## Remarks

This method returns a value 3 (primary, secondary, and tertiary).

Call this property before calling [IMateReference::ReferenceAlignment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateReference~ReferenceAlignment.html), [IMateReference::ReferenceEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateReference~ReferenceEntity.html), or [IMateReference::ReferenceType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateReference~ReferenceType.html).

## See Also

[IMateReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference.html)
[IMateReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
