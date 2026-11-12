---
title: "VarySketch Property (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "VarySketch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~VarySketch.html"
---

# VarySketch Property (ILinearPatternFeatureData)

Gets or sets whether to allow the pattern instances of a seed sketch to vary in relation to enclosing geometry in this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property VarySketch As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
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

True to allow the pattern instances of a seed sketch to vary in relation to enclosing geomtry, false to not

## VBA Syntax

See [LinearPatternFeatureData::VarySketch](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~VarySketch.html).

## Examples

See the [ILinearPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html) example.

## Remarks

This property is valid only when creating a pattern from a seed sketch.

The seed sketch has:

- An enclosing boundary of base geometry.
- Fully defined relations.
- Dimensions only for measurements that will not vary in the pattern instances.
- A driving dimension that is used to specify the direction of the linear pattern.

If this property is true:

- Specify [ILinearPatternFeatureData::D1Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1Axis.html) with a driving dimension of the seed sketch.
- Pattern instances vary with and are constrained by the enclosing geometry.

See the **SOLIDWORKS Help > Parts and Features > Features > Patterns and Mirroring > Control and Modify Patterns >** **Vary Sketch** topic.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
