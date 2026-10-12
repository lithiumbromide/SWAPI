---
title: "ReverseOffset Property (ISimpleHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleHoleFeatureData2"
member: "ReverseOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~ReverseOffset.html"
---

# ReverseOffset Property (ISimpleHoleFeatureData2)

Gets or sets whether to reverse the offset from the surface.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseOffset As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleHoleFeatureData2
Dim value As System.Boolean

instance.ReverseOffset = value

value = instance.ReverseOffset
```

### C#

```csharp
System.bool ReverseOffset {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseOffset {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True reverses the offset from the surface, false does not

## VBA Syntax

See [SimpleHoleFeatureData2::ReverseOffset](ms-its:sldworksapivb6.chm::/sldworks~SimpleHoleFeatureData2~ReverseOffset.html).

## See Also

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.html)
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.html)
[ISimpleHoleFeature2::SurfaceOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~SurfaceOffset.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
