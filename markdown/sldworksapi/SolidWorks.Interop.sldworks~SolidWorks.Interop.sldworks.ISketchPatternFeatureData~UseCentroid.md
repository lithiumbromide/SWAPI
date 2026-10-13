---
title: "UseCentroid Property (ISketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchPatternFeatureData"
member: "UseCentroid"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~UseCentroid.html"
---

# UseCentroid Property (ISketchPatternFeatureData)

Gets or sets whether to use a centroid for this sketch pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseCentroid As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPatternFeatureData
Dim value As System.Boolean

instance.UseCentroid = value

value = instance.UseCentroid
```

### C#

```csharp
System.bool UseCentroid {get; set;}
```

### C++/CLI

```cpp
property System.bool UseCentroid {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to a centroid, false to use a reference point

## VBA Syntax

See [SketchPatternFeatureData::UseCentroid](ms-its:sldworksapivb6.chm::/sldworks~SketchPatternFeatureData~UseCentroid.html).

## Examples

See the [ISketchPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html) examples.

## See Also

[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html)
[ISketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.html)
[ISketchPatternFeatureData::ReferencePoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~ReferencePoint.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
