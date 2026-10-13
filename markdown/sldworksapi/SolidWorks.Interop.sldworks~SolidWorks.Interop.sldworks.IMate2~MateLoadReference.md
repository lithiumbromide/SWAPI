---
title: "MateLoadReference Property (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "MateLoadReference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~MateLoadReference.html"
---

# MateLoadReference Property (IMate2)

Gets the mate load reference associated with this mate.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MateLoadReference As MateLoadReference
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim value As MateLoadReference

value = instance.MateLoadReference
```

### C#

```csharp
MateLoadReference MateLoadReference {get;}
```

### C++/CLI

```cpp
property MateLoadReference^ MateLoadReference {
   MateLoadReference^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Mate load reference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateLoadReference.html) for this mate, or Nothing or null if none exists

## VBA Syntax

See [Mate2::MateLoadReference](ms-its:sldworksapivb6.chm::/sldworks~Mate2~MateLoadReference.html).

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
