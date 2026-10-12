---
title: "CoordinateSystem Property (IBoundingBoxFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundingBoxFeatureData"
member: "CoordinateSystem"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~CoordinateSystem.html"
---

# CoordinateSystem Property (IBoundingBoxFeatureData)

Gets or sets the coordinate system reference for this bounding box feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CoordinateSystem As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundingBoxFeatureData
Dim value As System.Object

instance.CoordinateSystem = value

value = instance.CoordinateSystem
```

### C#

```csharp
System.object CoordinateSystem {get; set;}
```

### C++/CLI

```cpp
property System.Object^ CoordinateSystem {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [BoundingBoxFeatureData::CoordinateSystem](ms-its:sldworksapivb6.chm::/sldworks~BoundingBoxFeatureData~CoordinateSystem.html).

## Remarks

This property is valid only if [IBoundingBoxFeatureData::ReferenceFaceOrPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~ReferenceFaceOrPlane.html) is set to [swGlobalBoundingBoxFitOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGlobalBoundingBoxFitOptions_e.html).swBoundingBoxType_CustomCoordSys.

Set this property and [IBoundingBoxFeatureData::lwtaDirectionType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~lwtaDirectionType.html) to define a custom coordinate system for this rectangular or cylindrical bounding box feature.

## See Also

[IBoundingBoxFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.html)
[IBoundingBoxFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData_members.html)
[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)

## Availability

SOLIDWORKS 2026 SP01, Revision Number 34.1
