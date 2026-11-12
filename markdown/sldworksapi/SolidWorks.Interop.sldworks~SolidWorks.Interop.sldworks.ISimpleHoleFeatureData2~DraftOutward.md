---
title: "DraftOutward Property (ISimpleHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleHoleFeatureData2"
member: "DraftOutward"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~DraftOutward.html"
---

# DraftOutward Property (ISimpleHoleFeatureData2)

Gets or sets whether to draft the simple hole feature outward.

## Syntax

### Visual Basic (Declaration)

```vb
Property DraftOutward As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleHoleFeatureData2
Dim value As System.Boolean

instance.DraftOutward = value

value = instance.DraftOutward
```

### C#

```csharp
System.bool DraftOutward {get; set;}
```

### C++/CLI

```cpp
property System.bool DraftOutward {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True drafts the simple hole feature outward, false does not

## VBA Syntax

See [SimpleHoleFeatureData2::DraftOutward](ms-its:sldworksapivb6.chm::/sldworks~SimpleHoleFeatureData2~DraftOutward.html).

## See Also

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.html)
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.html)
[ISimpleHoleFeatureData2::DraftAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~DraftAngle.html)
[ISimpleHoleFeatureData2::DraftWhileExtruding Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~DraftWhileExtruding.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
