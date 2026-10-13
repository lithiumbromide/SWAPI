---
title: "Shoulder Property (IDatumTag)"
project: "SOLIDWORKS API Help"
interface: "IDatumTag"
member: "Shoulder"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~Shoulder.html"
---

# Shoulder Property (IDatumTag)

Gets whether there is a shoulder (or bend) in the leader for this datum tag.

## Syntax

### Visual Basic (Declaration)

```vb
Property Shoulder As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTag
Dim value As System.Boolean

instance.Shoulder = value

value = instance.Shoulder
```

### C#

```csharp
System.bool Shoulder {get; set;}
```

### C++/CLI

```cpp
property System.bool Shoulder {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if this datum tag has a shoulder, false if not

## VBA Syntax

See [DatumTag::Shoulder](ms-its:sldworksapivb6.chm::/sldworks~DatumTag~Shoulder.html).

## Remarks

Although you get or set this property at any time, this property only applies to square datum tags. If you use it when a round datum tag is shown, you will not see a value for the current display.

## See Also

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.html)
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html)
[IDatumTag::ForcedShoulder Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~ForcedShoulder.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
