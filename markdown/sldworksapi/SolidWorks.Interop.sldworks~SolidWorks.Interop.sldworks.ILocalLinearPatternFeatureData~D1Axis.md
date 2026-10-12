---
title: "D1Axis Property (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "D1Axis"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1Axis.html"
---

# D1Axis Property (ILocalLinearPatternFeatureData)

Gets or sets Direction 1 for this linear component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1Axis As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
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

See [LocalLinearPatternFeatureData::D1Axis](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~D1Axis.html).

## Remarks

Use [ILocalLinearPatternFeatureData::GetD1AxisType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalLinearPatternFeatureData~GetD1AxisType.html) to determine the type of object to pass to this property.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)
[ILocalLinearPatternFeatureData::D1ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1ReverseDirection.html)
[ILocalLinearPatternFeatureData::D1Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1Spacing.html)
[ILocalLinearPatternFeatureData::D1TotalInstances Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1TotalInstances.html)
[ILocalLinearPatternFeatureData::GetD1AxisType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~GetD1AxisType.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
