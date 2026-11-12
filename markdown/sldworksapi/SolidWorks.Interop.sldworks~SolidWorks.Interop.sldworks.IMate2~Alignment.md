---
title: "Alignment Property (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "Alignment"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~Alignment.html"
---

# Alignment Property (IMate2)

Gets the type of alignment for this mate.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Alignment As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim value As System.Integer

value = instance.Alignment
```

### C#

```csharp
System.int Alignment {get;}
```

### C++/CLI

```cpp
property System.int Alignment {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of alignment as defined in [swMateAlign_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateAlign_e.html)

## VBA Syntax

See [Mate2::Alignment](ms-its:sldworksapivb6.chm::/sldworks~Mate2~Alignment.html).

## Examples

[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)
[Get Mate Definition (VBA)](Get_Mate_Definition_Example_VB.htm)
[Get Mates and Mate Entities (C#)](Get_Mates_and_Mate_Entities_Example_CSharp.htm)
[Get Mates and Mate Entities (VB.NET)](Get_Mates_and_Mate_Entities_Example_VBNET.htm)
[Get Mates and Mate Entities (VBA)](Get_Mates_and_Mate_Entities_Example_VB.htm)

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
