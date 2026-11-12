---
title: "D1Axis Property (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "D1Axis"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1Axis.html"
---

# D1Axis Property (ILinearPatternFeatureData)

Gets or sets Direction 1 for this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1Axis As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
Dim value As System.Object

instance.D1Axis = value

value = instance.D1Axis
```

### C#

```csharp
System.object D1Axis {get; set;}
```

### C++/CLI

```cpp
property System.Object^ D1Axis {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Direction 1 entity: linear [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), [line](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html), [axis](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefAxis.html), [dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html), planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), planar [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html), conical face, conical surface, circular edge, or reference [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)

## VBA Syntax

See [LinearPatternFeatureData::D1Axis](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~D1Axis.html).

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::GetD1AxisType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetD1AxisType.html)
[ILinearPatternFeatureData::D1ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1ReverseDirection.html)
[ILinearPatternFeatureData::D1Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1Spacing.html)
[ILinearPatternFeatureData::D1TotalInstances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1TotalInstances.html)
[ILinearPatternFeatureData::VarySketch Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~VarySketch.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
