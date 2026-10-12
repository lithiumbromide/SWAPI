---
title: "PositionOffsetReference Property (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "PositionOffsetReference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionOffsetReference.html"
---

# PositionOffsetReference Property (IEdgeFlangeFeatureData)

Gets or sets the flange position offset reference for this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property PositionOffsetReference As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As System.Object

instance.PositionOffsetReference = value

value = instance.PositionOffsetReference
```

### C#

```csharp
System.object PositionOffsetReference {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PositionOffsetReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Flange position offset reference for this edge flange

## VBA Syntax

See [EdgeFlangeFeatureData::PositionOffsetReference](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~PositionOffsetReference.html).

## Remarks

This property is valid only if:

- [IEdgeFlangeFeatureData::UsePositionOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UsePositionOffset.html) is set to true,

- and -

- [IEdgeFlangeFeatureData::PositionOffsetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionOffsetType.html) is set to [swFlangeOffsetTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangeOffsetTypes_e.html).:

  - swFlangeOffsetUpToVertex
  - swFlangeOffsetUpToSurface
  - swFlangeOffsetFromSurface

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)
[IEdgeFlangeFeatureData::PositionOffsetDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionOffsetDistance.html)
[IEdgeFlangeFeatureData::ReversePositionOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReversePositionOffset.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
