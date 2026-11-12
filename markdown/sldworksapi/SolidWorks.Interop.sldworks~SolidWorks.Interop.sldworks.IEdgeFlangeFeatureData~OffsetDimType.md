---
title: "OffsetDimType Property (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "OffsetDimType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~OffsetDimType.html"
---

# OffsetDimType Property (IEdgeFlangeFeatureData)

Gets or sets the flange length origin type for dimensioning this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetDimType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As System.Integer

instance.OffsetDimType = value

value = instance.OffsetDimType
```

### C#

```csharp
System.int OffsetDimType {get; set;}
```

### C++/CLI

```cpp
property System.int OffsetDimType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Dimensioning origin type as defined in [swFlangeDimTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangeDimTypes_e.html)

## VBA Syntax

See [EdgeFlangeFeatureData::OffsetDimType](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~OffsetDimType.html).

## Examples

See the [IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html) examples.

## Remarks

This property is valid only if [IEdgeFlangeFeatureData::OffsetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~OffsetType.html) is not set to [swFlangeOffsetTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangeOffsetTypes_e.html).swFlangeOffsetUpToVertex.

The default value of this property is swFlangeDimTypes_e.swFlangeDimTypeInnerVirtualSharp.

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)
[IEdgeFlangeFeatureData::OffsetDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~OffsetDistance.html)
[IEdgeFlangeFeatureData::UsePositionOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UsePositionOffset.html)
[IEdgeFlangeFeatureData::OffsetType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~OffsetType.html)
[IEdgeFlangeFeatureData::ReverseOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReverseOffset.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
