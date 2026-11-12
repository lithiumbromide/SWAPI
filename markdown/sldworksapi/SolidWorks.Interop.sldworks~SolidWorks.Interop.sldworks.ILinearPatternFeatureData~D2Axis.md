---
title: "D2Axis Property (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "D2Axis"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2Axis.html"
---

# D2Axis Property (ILinearPatternFeatureData)

Gets or sets Direction 2 for this bidirectional linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2Axis As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
Dim value As System.Object

instance.D2Axis = value

value = instance.D2Axis
```

### C#

```csharp
System.object D2Axis {get; set;}
```

### C++/CLI

```cpp
property System.Object^ D2Axis {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Direction 2 entity: linear [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html), [line](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html), [axis](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefAxis.html), [dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html), planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), planar [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html), conical face, conical surface, circular edge, or reference [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)

## VBA Syntax

See [LinearPatternFeatureData::D2Axis](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~D2Axis.html).

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::GetD2AxisType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetD2AxisType.html)
[ILinearPatternFeatureData::IsDirection2Specified Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~IsDirection2Specified.html)
[ILinearPatternFeatureData::D2PatternSeedOnly Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2PatternSeedOnly.html)
[ILinearPatternFeatureData::D2ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2ReverseDirection.html)
[ILinearPatternFeatureData::D2Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2Spacing.html)
[ILinearPatternFeatureData::D2TotalInstances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D2TotalInstances.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
