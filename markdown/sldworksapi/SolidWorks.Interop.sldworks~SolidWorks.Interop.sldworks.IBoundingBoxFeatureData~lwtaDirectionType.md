---
title: "lwtaDirectionType Property (IBoundingBoxFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundingBoxFeatureData"
member: "lwtaDirectionType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~lwtaDirectionType.html"
---

# lwtaDirectionType Property (IBoundingBoxFeatureData)

Gets or sets the length, width, or thickness direction with respect to a specified coordinate system of the rectangular bounding box feature. Gets or sets the axis direction with respect to a specified coordinate system of the cylindrical bounding box feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property lwtaDirectionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundingBoxFeatureData
Dim value As System.Integer

instance.lwtaDirectionType = value

value = instance.lwtaDirectionType
```

### C#

```csharp
System.int lwtaDirectionType {get; set;}
```

### C++/CLI

```cpp
property System.int lwtaDirectionType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Direction mapping as defined by [swGlobalBBoxLWTADirectionType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGlobalBBoxLWTADirectionType_e.html)

## VBA Syntax

See [BoundingBoxFeatureData::lwtaDirectionType](ms-its:sldworksapivb6.chm::/sldworks~BoundingBoxFeatureData~lwtaDirectionType.html).

## Remarks

This property is valid only if [IBoundingBoxFeatureData::ReferenceFaceOrPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~ReferenceFaceOrPlane.html) is set to [swGlobalBoundingBoxFitOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGlobalBoundingBoxFitOptions_e.html).swBoundingBoxType_CustomCoordSys.

Set this property and [IBoundingBoxFeatureData::CoordinateSystem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~CoordinateSystem.html) to define a custom coordinate system for this rectangular or cylindrical bounding box feature.

## See Also

[IBoundingBoxFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.html)
[IBoundingBoxFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData_members.html)

## Availability

SOLIDWORKS 2026 SP01, Revision Number 34.1
