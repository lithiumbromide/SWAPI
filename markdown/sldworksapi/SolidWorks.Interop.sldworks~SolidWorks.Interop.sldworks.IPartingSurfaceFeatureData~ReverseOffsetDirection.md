---
title: "ReverseOffsetDirection Property (IPartingSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingSurfaceFeatureData"
member: "ReverseOffsetDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~ReverseOffsetDirection.html"
---

# ReverseOffsetDirection Property (IPartingSurfaceFeatureData)

Gets or sets whether to reverse the direction of this parting surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseOffsetDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingSurfaceFeatureData
Dim value As System.Boolean

instance.ReverseOffsetDirection = value

value = instance.ReverseOffsetDirection
```

### C#

```csharp
System.bool ReverseOffsetDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseOffsetDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the direction, false to not

## VBA Syntax

See [PartingSurfaceFeatureData::ReverseOffsetDirection](ms-its:sldworksapivb6.chm::/sldworks~PartingSurfaceFeatureData~ReverseOffsetDirection.html).

## See Also

[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.html)
[IPartingSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
