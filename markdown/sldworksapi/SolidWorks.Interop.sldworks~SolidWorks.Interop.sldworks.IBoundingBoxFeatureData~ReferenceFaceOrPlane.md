---
title: "ReferenceFaceOrPlane Property (IBoundingBoxFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundingBoxFeatureData"
member: "ReferenceFaceOrPlane"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~ReferenceFaceOrPlane.html"
---

# ReferenceFaceOrPlane Property (IBoundingBoxFeatureData)

Gets or sets how to create the bounding box.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferenceFaceOrPlane As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundingBoxFeatureData
Dim value As System.Integer

instance.ReferenceFaceOrPlane = value

value = instance.ReferenceFaceOrPlane
```

### C#

```csharp
System.int ReferenceFaceOrPlane {get; set;}
```

### C++/CLI

```cpp
property System.int ReferenceFaceOrPlane {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fit type as defined in [swGlobalBoundingBoxFitOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGlobalBoundingBoxFitOptions_e.html)

## VBA Syntax

See [BoundingBoxFeatureData::ReferenceFaceOrPlane](ms-its:sldworksapivb6.chm::/sldworks~BoundingBoxFeatureData~ReferenceFaceOrPlane.html).

## Examples

See the [IBoundingBoxFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.html) example.

## Remarks

If this property is set to:

- swGlobalBoundingBoxFitOptions_e.swBoundingBoxType_CustomPlane, then select a face or plane using [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.html) with TypeWanted set to [swSelectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html).swSelFACES before calling this method.

- swGlobalBoundingBoxFitOptions_e.swBoundingBoxType_CustomCoordSys, then use [IBoundingBoxFeatureData::CoordinateSystem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~CoordinateSystem.html) to specify the reference coordinate system and use [IBoundingBoxFeatureData::lwtaDirectionType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~lwtaDirectionType.html) to specify the length, width, thickness, or axis direction mapping with respect to the reference coordinate system.

## See Also

[IBoundingBoxFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.html)
[IBoundingBoxFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData_members.html)
[IBoundingBoxFeatureData::PlanarEntity Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~PlanarEntity.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
