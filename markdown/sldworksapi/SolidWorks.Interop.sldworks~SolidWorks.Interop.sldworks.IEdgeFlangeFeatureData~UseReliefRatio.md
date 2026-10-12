---
title: "UseReliefRatio Property (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "UseReliefRatio"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UseReliefRatio.html"
---

# UseReliefRatio Property (IEdgeFlangeFeatureData)

Gets or sets whether to use the relief ratio for this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseReliefRatio As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As System.Boolean

instance.UseReliefRatio = value

value = instance.UseReliefRatio
```

### C#

```csharp
System.bool UseReliefRatio {get; set;}
```

### C++/CLI

```cpp
property System.bool UseReliefRatio {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True uses the relief ratio (default), false does not

## VBA Syntax

See [EdgeFlangeFeatureData::UseReliefRatio](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~UseReliefRatio.html).

## Examples

See the [IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html) examples.

## Remarks

This property is valid only if

- [IEdgeFlangeFeatureData::UseDefaultBendRelief](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UseDefaultBendRelief.html) is false

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
[IEdgeFlangeFeatureData::ReliefDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~ReliefDepth.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
