---
title: "PositionOffsetType Property (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "PositionOffsetType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionOffsetType.html"
---

# PositionOffsetType Property (IEdgeFlangeFeatureData)

Gets or sets the flange position offset end condition of this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property PositionOffsetType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As System.Integer

instance.PositionOffsetType = value

value = instance.PositionOffsetType
```

### C#

```csharp
System.int PositionOffsetType {get; set;}
```

### C++/CLI

```cpp
property System.int PositionOffsetType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Flange position offset end condition as defined in [swFlangeOffsetTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangeOffsetTypes_e.html)

## VBA Syntax

See [EdgeFlangeFeatureData::PositionOffsetType](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~PositionOffsetType.html).

## Examples

See the [IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html) examples.

## Remarks

This property is valid only if [IEdgeFlangeFeatureData::UsePositionOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UsePositionOffset.html) is set to true.

The default value of this property is swFlangeOffsetTypes_e.swFlangeOffsetBlind.

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)
[IEdgeFlangeFeatureData::PositionOffsetDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionOffsetDistance.html)
[IEdgeFlangeFeatureData::PositionOffsetReference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionOffsetReference.html)
[IEdgeFlangeFeatureData::ReversePositionOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReversePositionOffset.html)
[IEdgeFlangeFeatureData::UsePositionTrimSideBends Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UsePositionTrimSideBends.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
