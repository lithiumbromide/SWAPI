---
title: "PatternBodyArray Property (ISketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchPatternFeatureData"
member: "PatternBodyArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~PatternBodyArray.html"
---

# PatternBodyArray Property (ISketchPatternFeatureData)

Gets and sets the bodies to pattern for this sketch pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternBodyArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPatternFeatureData
Dim value As System.Object

instance.PatternBodyArray = value

value = instance.PatternBodyArray
```

### C#

```csharp
System.object PatternBodyArray {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PatternBodyArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of bodies to pattern

## VBA Syntax

See [SketchPatternFeatureData::PatternBodyArray](ms-its:sldworksapivb6.chm::/sldworks~SketchPatternFeatureData~PatternBodyArray.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html)
[ISketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.html)
[ISketchPatternFeatureData::GetPatternBodyCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GetPatternBodyCount.html)
[ISketchPatternFeatureData::IGetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~IGetPatternBodyArray.html)
[ISketchPatternFeatureData::ISetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~ISetPatternBodyArray.html)
[ISketchPatternFeatureData::BodyPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~BodyPattern.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
