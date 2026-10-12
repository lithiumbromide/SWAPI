---
title: "IncludeHiddenBodies Property (IBoundingBoxFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundingBoxFeatureData"
member: "IncludeHiddenBodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~IncludeHiddenBodies.html"
---

# IncludeHiddenBodies Property (IBoundingBoxFeatureData)

Gets or sets whether to include hidden bodies in this bounding box feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeHiddenBodies As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundingBoxFeatureData
Dim value As System.Boolean

instance.IncludeHiddenBodies = value

value = instance.IncludeHiddenBodies
```

### C#

```csharp
System.bool IncludeHiddenBodies {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeHiddenBodies {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to include hidden bodies, false to not

## VBA Syntax

See [BoundingBoxFeatureData::IncludeHiddenBodies](ms-its:sldworksapivb6.chm::/sldworks~BoundingBoxFeatureData~IncludeHiddenBodies.html).

## Examples

See the [IBoundingBoxFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.html) example.

## See Also

[IBoundingBoxFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.html)
[IBoundingBoxFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
