---
title: "IncludeHiddenComponents Property (IBoundingBoxFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundingBoxFeatureData"
member: "IncludeHiddenComponents"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~IncludeHiddenComponents.html"
---

# IncludeHiddenComponents Property (IBoundingBoxFeatureData)

Gets or sets whether to include hidden components in this bounding box feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeHiddenComponents As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundingBoxFeatureData
Dim value As System.Boolean

instance.IncludeHiddenComponents = value

value = instance.IncludeHiddenComponents
```

### C#

```csharp
System.bool IncludeHiddenComponents {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeHiddenComponents {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to include hidden components, false to not

## VBA Syntax

See [BoundingBoxFeatureData::IncludeHiddenComponents](ms-its:sldworksapivb6.chm::/sldworks~BoundingBoxFeatureData~IncludeHiddenComponents.html).

## See Also

[IBoundingBoxFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.html)
[IBoundingBoxFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
