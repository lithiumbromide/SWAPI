---
title: "PatternFeatureArray Property (ISketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchPatternFeatureData"
member: "PatternFeatureArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~PatternFeatureArray.html"
---

# PatternFeatureArray Property (ISketchPatternFeatureData)

Gets or sets the seed features for the sketch pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternFeatureArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPatternFeatureData
Dim value As System.Object

instance.PatternFeatureArray = value

value = instance.PatternFeatureArray
```

### C#

```csharp
System.object PatternFeatureArray {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PatternFeatureArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of features

## VBA Syntax

See [SketchPatternFeatureData::PatternFeatureArray](ms-its:sldworksapivb6.chm::/sldworks~SketchPatternFeatureData~PatternFeatureArray.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html)
[ISketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.html)
[ISketchPatternFeatureData::GetPatternFeatureCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GetPatternFeatureCount.html)
[ISketchPatternFeatureData::IGetPatternFeatureArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~IGetPatternFeatureArray.html)
[ISketchPatternFeatureData::ISetPatternFeatureArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~ISetPatternFeatureArray.html)
[ISketchPatternFeatureData::BodyPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~BodyPattern.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
