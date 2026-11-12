---
title: "CanBeFlipped Property (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "CanBeFlipped"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~CanBeFlipped.html"
---

# CanBeFlipped Property (IMate2)

Gets whether this distance or angle mate can be flipped.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CanBeFlipped As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim value As System.Boolean

value = instance.CanBeFlipped
```

### C#

```csharp
System.bool CanBeFlipped {get;}
```

### C++/CLI

```cpp
property System.bool CanBeFlipped {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if mate can be flipped, false if not

## VBA Syntax

See [Mate2::CanBeFlipped](ms-its:sldworksapivb6.chm::/sldworks~Mate2~CanBeFlipped.html).

## Examples

[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)
[Get Mate Definition (VBA)](Get_Mate_Definition_Example_VB.htm)
[Get Mates and Mate Entities (C#)](Get_Mates_and_Mate_Entities_Example_CSharp.htm)
[Get Mates and Mate Entities (VB.NET)](Get_Mates_and_Mate_Entities_Example_VBNET.htm)
[Get Mates and Mate Entities (VBA)](Get_Mates_and_Mate_Entities_Example_VB.htm)

## Remarks

Use [IMate2::Type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMate2~Type.html) to determine the type of mate.

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::Flipped Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~Flipped.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
