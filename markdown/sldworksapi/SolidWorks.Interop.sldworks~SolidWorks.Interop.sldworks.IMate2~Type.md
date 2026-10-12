---
title: "Type Property (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~Type.html"
---

# Type Property (IMate2)

Gets the type of mate.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim value As System.Integer

value = instance.Type
```

### C#

```csharp
System.int Type {get;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of mate as defined by [swMateType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateType_e.html)

## VBA Syntax

See [Mate2::Type](ms-its:sldworksapivb6.chm::/sldworks~Mate2~Type.html).

## Examples

[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)
[Get Mate Definition (VBA)](Get_Mate_Definition_Example_VB.htm)
[Get Mates (C#)](Get_Mates_Example_CSharp.htm)
[Get Mates (VB.NET)](Get_Mates_Example_VBNET.htm)
[Get Mates (VBA)](Get_Mates_Example_VB.htm)
[Get Mates and Mate Entities (C#)](Get_Mates_and_Mate_Entities_Example_CSharp.htm)
[Get Mates and Mate Entities (VB.NET)](Get_Mates_and_Mate_Entities_Example_VBNET.htm)
[Get Mates and Mate Entities (VBA)](Get_Mates_and_Mate_Entities_Example_VB.htm)

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::LockMagneticMate Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~LockMagneticMate.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
