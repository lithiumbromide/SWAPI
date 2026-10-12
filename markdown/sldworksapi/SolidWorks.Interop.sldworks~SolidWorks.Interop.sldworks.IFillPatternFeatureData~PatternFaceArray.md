---
title: "PatternFaceArray Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "PatternFaceArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternFaceArray.html"
---

# PatternFaceArray Property (IFillPatternFeatureData)

Gets or sets the array of faces to pattern in this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternFaceArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
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

Array of [IFace2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)s to pattern

## VBA Syntax

See [FillPatternFeatureData::PatternFaceArray](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~PatternFaceArray.html).

## Remarks

This property is valid only if [IFillPatternFeatureData::PatternElement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternElement.html) is [swPatternElementSelection_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternElementSelection_e.html).swFeatureFaces.

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
