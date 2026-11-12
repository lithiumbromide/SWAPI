---
title: "ReferenceType2 Property (IMateEntity2)"
project: "SOLIDWORKS API Help"
interface: "IMateEntity2"
member: "ReferenceType2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~ReferenceType2.html"
---

# ReferenceType2 Property (IMateEntity2)

Gets the mate entity reference type for this mate entity.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferenceType2 As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMateEntity2
Dim value As System.Integer

value = instance.ReferenceType2
```

### C#

```csharp
System.int ReferenceType2 {get;}
```

### C++/CLI

```cpp
property System.int ReferenceType2 {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of mate reference as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [MateEntity2::ReferenceType2](ms-its:sldworksapivb6.chm::/sldworks~MateEntity2~ReferenceType2.html).

## See Also

[IMateEntity2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2.html)
[IMateEntity2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2_members.html)
[IMateEntity2::Reference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~Reference.html)
[IMateEntity2::ReferenceComponent Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~ReferenceComponent.html)

## Availability

SOLIDWORKS 2006 SP4, Revision Number 14.4
