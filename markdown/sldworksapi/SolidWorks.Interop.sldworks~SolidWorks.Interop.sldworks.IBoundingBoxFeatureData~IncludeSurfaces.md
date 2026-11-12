---
title: "IncludeSurfaces Property (IBoundingBoxFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundingBoxFeatureData"
member: "IncludeSurfaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~IncludeSurfaces.html"
---

# IncludeSurfaces Property (IBoundingBoxFeatureData)

Gets or sets whether to include surfaces in this bounding box feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeSurfaces As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundingBoxFeatureData
Dim value As System.Boolean

instance.IncludeSurfaces = value

value = instance.IncludeSurfaces
```

### C#

```csharp
System.bool IncludeSurfaces {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeSurfaces {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to include surfaces, false to not

## VBA Syntax

See [BoundingBoxFeatureData::IncludeSurfaces](ms-its:sldworksapivb6.chm::/sldworks~BoundingBoxFeatureData~IncludeSurfaces.html).

## Examples

See the [IBoundingBoxFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.html) example.

## See Also

[IBoundingBoxFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.html)
[IBoundingBoxFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
