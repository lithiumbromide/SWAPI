---
title: "DraftFromWall Property (IRibFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRibFeatureData2"
member: "DraftFromWall"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~DraftFromWall.html"
---

# DraftFromWall Property (IRibFeatureData2)

Gets or sets whether to draft the rib from the wall interface or the sketch plane.

## Syntax

### Visual Basic (Declaration)

```vb
Property DraftFromWall As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRibFeatureData2
Dim value As System.Boolean

instance.DraftFromWall = value

value = instance.DraftFromWall
```

### C#

```csharp
System.bool DraftFromWall {get; set;}
```

### C++/CLI

```cpp
property System.bool DraftFromWall {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to draft from the sketch plane, false to draft from the wall interface

## VBA Syntax

See [RibFeatureData2::DraftFromWall](ms-its:sldworksapivb6.chm::/sldworks~RibFeatureData2~DraftFromWall.html).

## Remarks

This property is valid only when [IRibFeatureData2::EnableDraft](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRibFeatureData2~EnableDraft.html) is set to true.

## See Also

[IRibFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.html)
[IRibFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
