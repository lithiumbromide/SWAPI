---
title: "PositionOffsetDistance Property (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "PositionOffsetDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionOffsetDistance.html"
---

# PositionOffsetDistance Property (IEdgeFlangeFeatureData)

Gets or sets the flange position offset for this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property PositionOffsetDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As System.Double

instance.PositionOffsetDistance = value

value = instance.PositionOffsetDistance
```

### C#

```csharp
System.double PositionOffsetDistance {get; set;}
```

### C++/CLI

```cpp
property System.double PositionOffsetDistance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Flange position offset value; default value is 0.01 m

## VBA Syntax

See [EdgeFlangeFeatureData::PositionOffsetDistance](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~PositionOffsetDistance.html).

## Examples

See the [IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html) examples.

## Remarks

This property is valid only if:

- [IEdgeFlangeFeatureData::UsePositionOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UsePositionOffset.html) is set to true,

- and -

- [IEdgeflangeFeatureData::PostionOffsetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionOffsetType.html) is set to either [swFlangeOffsetTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangeOffsetTypes_e.html).swFlangeOffsetFromSurface or swFlangeOffsetTypes_e.swFlangeOffsetBlind.

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)
[IEdgeFlangeFeatureData::PositionOffsetReference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionOffsetReference.html)
[IEdgeFlangeFeatureData::ReversePositionOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReversePositionOffset.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
