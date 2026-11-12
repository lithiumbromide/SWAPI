---
title: "Flipped Property (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "Flipped"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~Flipped.html"
---

# Flipped Property (IMate2)

Gets or sets whether to flip the distance or angle mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property Flipped As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim value As System.Boolean

instance.Flipped = value

value = instance.Flipped
```

### C#

```csharp
System.bool Flipped {get; set;}
```

### C++/CLI

```cpp
property System.bool Flipped {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip the mate, false to not

## VBA Syntax

See [Mate2::Flipped](ms-its:sldworksapivb6.chm::/sldworks~Mate2~Flipped.html).

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::CanBeFlipped Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~CanBeFlipped.html)
[IMate2::Type Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~Type.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
