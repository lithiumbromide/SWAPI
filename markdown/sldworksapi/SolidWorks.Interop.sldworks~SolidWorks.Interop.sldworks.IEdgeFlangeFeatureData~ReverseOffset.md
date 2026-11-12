---
title: "ReverseOffset Property (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "ReverseOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReverseOffset.html"
---

# ReverseOffset Property (IEdgeFlangeFeatureData)

Gets or sets whether to flip the flange length for this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseOffset As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
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

True flips the flange length, false does not (default)

## VBA Syntax

See [EdgeFlangeFeatureData::ReverseOffset](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~ReverseOffset.html).

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)
[IEdgeFlangeFeatureData::OffsetDimType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~OffsetDimType.html)
[IEdgeFlangeFeatureData::OffsetDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~OffsetDistance.html)
[IEdgeFlangeFeatureData::OffsetReference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~OffsetReference.html)
[IEdgeFlangeFeatureData::OffsetType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~OffsetType.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
