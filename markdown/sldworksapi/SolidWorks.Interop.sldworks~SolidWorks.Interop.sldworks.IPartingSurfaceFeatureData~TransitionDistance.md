---
title: "TransitionDistance Property (IPartingSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingSurfaceFeatureData"
member: "TransitionDistance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~TransitionDistance.html"
---

# TransitionDistance Property (IPartingSurfaceFeatureData)

Gets or sets the distance to set between adjacent edges for this parting surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property TransitionDistance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingSurfaceFeatureData
Dim value As System.Double

instance.TransitionDistance = value

value = instance.TransitionDistance
```

### C#

```csharp
System.double TransitionDistance {get; set;}
```

### C++/CLI

```cpp
property System.double TransitionDistance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance

## VBA Syntax

See [PartingSurfaceFeatureData::TransitionDistance](ms-its:sldworksapivb6.chm::/sldworks~PartingSurfaceFeatureData~TransitionDistance.html).

## Remarks

This property is only available when [IPartingSurfaceFeatureData::TransitionType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartingSurfaceFeatureData~TransitionType.html) is set to swPartingSurfaceSmoothngType_e.swPartingSurfaceSmooth.

## See Also

[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.html)
[IPartingSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
