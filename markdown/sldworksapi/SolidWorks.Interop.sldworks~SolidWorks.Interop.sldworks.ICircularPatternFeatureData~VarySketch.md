---
title: "VarySketch Property (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "VarySketch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~VarySketch.html"
---

# VarySketch Property (ICircularPatternFeatureData)

Gets or sets whether to allow pattern instances of a seed sketch to vary in relation to the base part in this circular pattern.

## Syntax

### Visual Basic (Declaration)

```vb
Property VarySketch As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
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

True to allow the pattern instances of a seed sketch to vary in relation to enclosing geometry, false to not

## VBA Syntax

See [CircularPatternFeatureData::VarySketch](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~VarySketch.html).

## Remarks

This property is valid only when creating a pattern from a seed sketch.

The seed sketch has:

- An enclosing boundary of base geometry.
- Fully defined relations.
- Dimensions only for measurements that will not vary in the pattern instances.
- A driving dimension that is used to specify the direction of the circular pattern.

If this property is true:

- Specify [ICircularPatternFeatureData::Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Axis.html) with a driving dimension of the seed sketch.
- Pattern instances vary with and are constrained by the enclosing geometry.

See the **SOLIDWORKS Help > Parts and Features > Features > Patterns and Mirroring > Control and Modify Patterns >** **Vary Sketch** topic.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
