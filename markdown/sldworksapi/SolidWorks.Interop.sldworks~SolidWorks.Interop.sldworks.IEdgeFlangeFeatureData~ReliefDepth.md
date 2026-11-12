---
title: "ReliefDepth Property (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "ReliefDepth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReliefDepth.html"
---

# ReliefDepth Property (IEdgeFlangeFeatureData)

Gets or sets the relief depth of the edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReliefDepth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As System.Double

instance.ReliefDepth = value

value = instance.ReliefDepth
```

### C#

```csharp
System.double ReliefDepth {get; set;}
```

### C++/CLI

```cpp
property System.double ReliefDepth {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Depth of relief; default value is 0.0003683 m

## VBA Syntax

See [EdgeFlangeFeatureData::ReliefDepth](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~ReliefDepth.html).

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
[IEdgeFlangeFeatureData::ReliefRatio Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReliefRatio.html)
[IEdgeFlangeFeatureData::ReliefTearType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReliefTearType.html)
[IEdgeFlangeFeatureData::ReliefWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReliefWidth.html)

## Availability

SOLIDWORKS 2201 SP2, Revision Number 9.2
