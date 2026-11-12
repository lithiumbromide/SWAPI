---
title: "VarySketch Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "VarySketch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~VarySketch.html"
---

# VarySketch Property (ICurveDrivenPatternFeatureData)

Gets or sets whether to allow pattern instances of a seed sketch to vary in relation to enclosing geometry in this curve-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property VarySketch As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Boolean

instance.VarySketch = value

value = instance.VarySketch
```

### C#

```csharp
System.bool VarySketch {get; set;}
```

### C++/CLI

```cpp
property System.bool VarySketch {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to allow pattern instances of a seed sketch to vary in relation to enclosing geometry, false to not

## VBA Syntax

See [CurveDrivenPatternFeatureData::VarySketch](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~VarySketch.html).

## Remarks

This property is valid only when creating a pattern from a seed sketch.

The seed sketch has:

- An enclosing boundary of base geometry.
- Fully defined relations.
- Dimensions only for measurements that will not vary in the pattern instances.
- A driving dimension that is used to specify the direction of the curve-driven pattern.

If this property is true:

- Specify [ICurveDrivenPatternFeatureData::D1Direction](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D1Direction.html) with a driving dimension of the seed sketch.
- Pattern instances vary with and are constrained by the enclosing geometry.

See the **SOLIDWORKS Help > Parts and Features > Features > Patterns and Mirroring > Control and Modify Patterns >** **Vary Sketch** topic.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
