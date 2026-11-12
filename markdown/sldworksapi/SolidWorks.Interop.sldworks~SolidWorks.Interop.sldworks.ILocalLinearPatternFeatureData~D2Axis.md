---
title: "D2Axis Property (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "D2Axis"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2Axis.html"
---

# D2Axis Property (ILocalLinearPatternFeatureData)

Gets or sets Direction 2 for this bidirectional linear component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2Axis As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
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

See [LocalLinearPatternFeatureData::D2Axis](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~D2Axis.html).

## Remarks

Use [ILocalLinearPatternFeatureData::GetD2AxisType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalLinearPatternFeatureData~GetD2AxisType.html) to determine the type of object to pass to this property.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)
[ILocalLinearPatternFeatureData::D2ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2ReverseDirection.html)
[ILocalLinearPatternFeatureData::D2Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2Spacing.html)
[ILocalLinearPatternFeatureData::D2TotalInstances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2TotalInstances.html)
[ILocalLinearPatternFeatureData::GetD2AxisType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~GetD2AxisType.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Numbe 9.2
