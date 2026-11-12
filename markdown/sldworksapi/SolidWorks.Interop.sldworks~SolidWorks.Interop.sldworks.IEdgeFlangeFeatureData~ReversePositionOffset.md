---
title: "ReversePositionOffset Property (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "ReversePositionOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReversePositionOffset.html"
---

# ReversePositionOffset Property (IEdgeFlangeFeatureData)

Gets or sets whether to reverse the flange position offset for this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReversePositionOffset As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As System.Boolean

instance.ReversePositionOffset = value

value = instance.ReversePositionOffset
```

### C#

```csharp
System.bool ReversePositionOffset {get; set;}
```

### C++/CLI

```cpp
property System.bool ReversePositionOffset {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True reverses the flange position offset, false does not (default)

## VBA Syntax

See [EdgeFlangeFeatureData::ReversePositionOffset](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~ReversePositionOffset.html).

## Remarks

This property is valid only if [IEdgeFlangeFeatureData::UsePositionOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UsePositionOffset.html) is set to true.

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)
[IEdgeFlangeFeatureData::PositionOffsetDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionOffsetDistance.html)
[IEdgeFlangeFeatureData::PositionOffsetReference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionOffsetReference.html)
[IEdgeFlangeFeatureData::PositionOffsetType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionOffsetType.html)
[IEdgeFlangeFeatureData::UsePositionOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UsePositionOffset.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
