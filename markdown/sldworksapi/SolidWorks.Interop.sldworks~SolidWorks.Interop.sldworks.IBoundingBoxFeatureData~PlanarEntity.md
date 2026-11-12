---
title: "PlanarEntity Property (IBoundingBoxFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundingBoxFeatureData"
member: "PlanarEntity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~PlanarEntity.html"
---

# PlanarEntity Property (IBoundingBoxFeatureData)

Gets or sets the reference face or plane for this bounding box feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PlanarEntity As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundingBoxFeatureData
Dim value As System.Object

instance.PlanarEntity = value

value = instance.PlanarEntity
```

### C#

```csharp
System.object PlanarEntity {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PlanarEntity {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) or [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)

## VBA Syntax

See [BoundingBoxFeatureData::PlanarEntity](ms-its:sldworksapivb6.chm::/sldworks~BoundingBoxFeatureData~PlanarEntity.html).

## Examples

See the [IBoundingBoxFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.html) example.

## Remarks

This property is valid only if [IBoundingBoxFeatureData::ReferenceFaceOrPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~ReferenceFaceOrPlane.html) is set to [swGlobalBoundingBoxFitOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGlobalBoundingBoxFitOptions_e.html).swBoundingBoxType_CustomPlane.

## See Also

[IBoundingBoxFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.html)
[IBoundingBoxFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
