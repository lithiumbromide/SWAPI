---
title: "ForcedShoulder Property (IDatumTag)"
project: "SOLIDWORKS API Help"
interface: "IDatumTag"
member: "ForcedShoulder"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~ForcedShoulder.html"
---

# ForcedShoulder Property (IDatumTag)

Gets whether this datum tag has a forced shoulder on its leader.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ForcedShoulder As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTag
Dim value As System.Boolean

value = instance.ForcedShoulder
```

### C#

```csharp
System.bool ForcedShoulder {get;}
```

### C++/CLI

```cpp
property System.bool ForcedShoulder {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the datum tag has a forced shoulder on its leader, false if not

## VBA Syntax

See [DatumTag::ForcedShoulder](ms-its:sldworksapivb6.chm::/sldworks~DatumTag~ForcedShoulder.html).

## Remarks

If a square tag is attached to an edge that is not at a 0 or 90 angle, then the leader will always have a shoulder (bent leader). The user cannot remove the shoulder.

## See Also

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.html)
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html)
[IDatumTag::Shoulder Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~Shoulder.html)

## Availability

SOLIDWORKS 2006 SP4, Revision Number 14.4
