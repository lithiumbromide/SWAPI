---
title: "OffsetDistance Property (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "OffsetDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~OffsetDistance.html"
---

# OffsetDistance Property (IEdgeFlangeFeatureData)

Gets or sets the flange length for this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As System.Double

instance.OffsetDistance = value

value = instance.OffsetDistance
```

### C#

```csharp
System.double OffsetDistance {get; set;}
```

### C++/CLI

```cpp
property System.double OffsetDistance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value of the flange length; default is 0.0022098 m

## VBA Syntax

See [EdgeFlangeFeatureData::OffsetDistance](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~OffsetDistance.html).

## Examples

See the [IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html) examples.

## Remarks

This property is valid for all settings of [IEdgeFlangeFeatureData::OffsetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~OffsetType.html) except [swFlangeOffsetTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangeOffsetTypes_e.html).swFlangeOffsetUpToVertex.

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)
[IEdgeFlangeFeatureData::OffsetDimType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~OffsetDimType.html)
[IEdgeFlangeFeatureData::OffsetReference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~OffsetReference.html)
[IEdgeFlangeFeatureData::ReverseOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReverseOffset.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
