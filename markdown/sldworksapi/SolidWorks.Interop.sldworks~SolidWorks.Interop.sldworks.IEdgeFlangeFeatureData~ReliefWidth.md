---
title: "ReliefWidth Property (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "ReliefWidth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReliefWidth.html"
---

# ReliefWidth Property (IEdgeFlangeFeatureData)

Gets or sets the width of the relief for this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReliefWidth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As System.Double

instance.ReliefWidth = value

value = instance.ReliefWidth
```

### C#

```csharp
System.double ReliefWidth {get; set;}
```

### C++/CLI

```cpp
property System.double ReliefWidth {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Relief width; default value is 0.0003683 m

## VBA Syntax

See [EdgeFlangeFeatureData::ReliefWidth](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~ReliefWidth.html).

## Remarks

This property is valid only if:

- [IEdgeFlangeFeatureData::UseDefaultBendRelief](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UseDefaultBendRelief.html) is set to false,

- and -

- [IEdgeFlangeFeatureData::UseReliefRatio](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UseReliefRatio.html) is true.

- and -

- [IEdgeFlangeFeatureData::AutoReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~AutoReliefType.html) is set to [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html).:

  - swSheetMetalReliefObround

- or -

- swSheetMetalReliefRectangle.

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)
[IEdgeFlangeFeatureData::PositionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionType.html)
[IEdgeFlangeFeatureData::ReliefDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReliefDepth.html)
[IEdgeFlangeFeatureData::ReliefRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReliefRatio.html)
[IEdgeFlangeFeatureData::ReliefTearType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReliefTearType.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
