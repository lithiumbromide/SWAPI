---
title: "ReliefRatio Property (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "ReliefRatio"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReliefRatio.html"
---

# ReliefRatio Property (IEdgeFlangeFeatureData)

Gets or sets the relief ratio for this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReliefRatio As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As System.Double

instance.ReliefRatio = value

value = instance.ReliefRatio
```

### C#

```csharp
System.double ReliefRatio {get; set;}
```

### C++/CLI

```cpp
property System.double ReliefRatio {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Relief ratio; default value is 0.5

## VBA Syntax

See [EdgeFlangeFeatureData::ReliefRatio](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~ReliefRatio.html).

## Examples

See the [IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html) examples.

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
[IEdgeFlangeFeatureData::ReliefDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReliefDepth.html)
[IEdgeFlangeFeatureData::ReliefTearType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReliefTearType.html)
[IEdgeFlangeFeatureData::ReliefWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReliefWidth.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
