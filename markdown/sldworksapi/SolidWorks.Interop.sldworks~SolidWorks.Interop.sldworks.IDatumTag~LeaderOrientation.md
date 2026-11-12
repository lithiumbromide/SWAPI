---
title: "LeaderOrientation Property (IDatumTag)"
project: "SOLIDWORKS API Help"
interface: "IDatumTag"
member: "LeaderOrientation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~LeaderOrientation.html"
---

# LeaderOrientation Property (IDatumTag)

Gets or sets the orientation of the leader for a round datum tag.

## Syntax

### Visual Basic (Declaration)

```vb
Property LeaderOrientation As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTag
Dim value As System.Integer

instance.LeaderOrientation = value

value = instance.LeaderOrientation
```

### C#

```csharp
System.int LeaderOrientation {get; set;}
```

### C++/CLI

```cpp
property System.int LeaderOrientation {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Orientation as defined in [swDatumGbLeaderStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDatumGbLeaderStyle_e.html)

## VBA Syntax

See [DatumTag::LeaderOrientation](ms-its:sldworksapivb6.chm::/sldworks~DatumTag~LeaderOrientation.html).

## Remarks

Although you get or set this property at any time, this property only applies to round datum tags. If you use it when a square datum tag is shown, you will not see a value for the current display.

## See Also

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.html)
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html)

## Availability

SOLIDWORKS 2006 SP4, Revision Number 14.4
