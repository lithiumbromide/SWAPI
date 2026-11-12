---
title: "BodyPattern Property (ISketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchPatternFeatureData"
member: "BodyPattern"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~BodyPattern.html"
---

# BodyPattern Property (ISketchPatternFeatureData)

Gets or sets whether to base this sketch pattern feature on bodies or features and faces.

## Syntax

### Visual Basic (Declaration)

```vb
Property BodyPattern As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPatternFeatureData
Dim value As System.Boolean

instance.BodyPattern = value

value = instance.BodyPattern
```

### C#

```csharp
System.bool BodyPattern {get; set;}
```

### C++/CLI

```cpp
property System.bool BodyPattern {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True for bodies, false for features and faces

## VBA Syntax

See [SketchPatternFeatureData::BodyPattern](ms-its:sldworksapivb6.chm::/sldworks~SketchPatternFeatureData~BodyPattern.html).

## See Also

[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html)
[ISketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.html)
[ISketchPatternFeatureData::PatternElement Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~PatternElement.html)
[ISketchPatternFeatureData::PatternBodyArray Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~PatternBodyArray.html)
[ISketchPatternFeatureData::PatternFaceArray Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~PatternFaceArray.html)
[ISketchPatternFeatureData::PatternFeatureArray Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~PatternFeatureArray.html)
[ISketchPatternFeatureData::IGetPatternBodyArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~IGetPatternBodyArray.html)
[ISketchPatternFeatureData::IGetPatternFaceArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~IGetPatternFaceArray.html)
[ISketchPatternFeatureData::IGetPatternFeatureArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~IGetPatternFeatureArray.html)
[ISketchPatternFeatureData::ISetPatternBodyArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~ISetPatternBodyArray.html)
[ISketchPatternFeatureData::ISetPatternFaceArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~ISetPatternFaceArray.html)
[ISketchPatternFeatureData::ISetPatternFeatureArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~ISetPatternFeatureArray.html)
[ISketchPatternFeatureData::GeometryPattern Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GeometryPattern.html)

## Availability

SOLIDWORKS 2015 SP4, Revision Number 23.4
