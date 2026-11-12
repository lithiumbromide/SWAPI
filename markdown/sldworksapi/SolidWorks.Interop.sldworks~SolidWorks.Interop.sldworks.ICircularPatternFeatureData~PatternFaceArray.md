---
title: "PatternFaceArray Property (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "PatternFaceArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~PatternFaceArray.html"
---

# PatternFaceArray Property (ICircularPatternFeatureData)

Gets or sets the list of faces to pattern for this circular pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternFaceArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
Dim value As System.Object

instance.PatternFaceArray = value

value = instance.PatternFaceArray
```

### C#

```csharp
System.object PatternFaceArray {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PatternFaceArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to pattern

## VBA Syntax

See [CircularPatternFeatureData::PatternFaceArray](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~PatternFaceArray.html).

## Remarks

This property is valid only if [ICircularPatternFeatureData::BodyPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~BodyPattern.html) is false.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)
[ICircularPatternFeatureData::GetPatternFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetPatternFaceCount.html)
[ICircularPatternFeatureData::IGetPatternFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~IGetPatternFaceArray.html)
[ICircularPatternFeatureData::ISetPatternFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~ISetPatternFaceArray.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
