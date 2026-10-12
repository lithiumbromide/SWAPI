---
title: "Mate Property (IMateLoadReference)"
project: "SOLIDWORKS API Help"
interface: "IMateLoadReference"
member: "Mate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~Mate.html"
---

# Mate Property (IMateLoadReference)

Gets the mate that owns this mate load reference.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Mate As Mate2
```

### Visual Basic (Usage)

```vb
Dim instance As IMateLoadReference
Dim value As Mate2

value = instance.Mate
```

### C#

```csharp
Mate2 Mate {get;}
```

### C++/CLI

```cpp
property Mate2^ Mate {
   Mate2^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Mate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMate2.html) that owns this mate load reference

## VBA Syntax

See [MateLoadReference::Mate](ms-its:sldworksapivb6.chm::/sldworks~MateLoadReference~Mate.html).

## See Also

[IMateLoadReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference.html)
[IMateLoadReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
