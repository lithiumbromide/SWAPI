---
title: "FlipOffsetDirection Property (IGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IGussetFeatureData"
member: "FlipOffsetDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~FlipOffsetDirection.html"
---

# FlipOffsetDirection Property (IGussetFeatureData)

Gets or sets whether the offset direction is flipped for this gusset feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlipOffsetDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IGussetFeatureData
Dim value As System.Boolean

instance.FlipOffsetDirection = value

value = instance.FlipOffsetDirection
```

### C#

```csharp
System.bool FlipOffsetDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool FlipOffsetDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip the offset direction, false to not

## VBA Syntax

See [GussetFeatureData::FlipOffsetDirection](ms-its:sldworksapivb6.chm::/sldworks~GussetFeatureData~FlipOffsetDirection.html).

## See Also

[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.html)
[IGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
