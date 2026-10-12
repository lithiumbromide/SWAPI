---
title: "EqualSpacing2 Property (ILocalCircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCircularPatternFeatureData"
member: "EqualSpacing2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~EqualSpacing2.html"
---

# EqualSpacing2 Property (ILocalCircularPatternFeatureData)

Gets or sets whether the pattern instances in Direction 2 are equally spaced in this bidirectional circular component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property EqualSpacing2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCircularPatternFeatureData
Dim value As System.Boolean

instance.EqualSpacing2 = value

value = instance.EqualSpacing2
```

### C#

```csharp
System.bool EqualSpacing2 {get; set;}
```

### C++/CLI

```cpp
property System.bool EqualSpacing2 {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use equal spacing in Direction 2, false to not

## VBA Syntax

See [LocalCircularPatternFeatureData::EqualSpacing2](ms-its:sldworksapivb6.chm::/sldworks~LocalCircularPatternFeatureData~EqualSpacing2.html).

## Remarks

This property is only available when:

- [ILocalCircularPatternFeatureData::Direction2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Direction2.html) is true, and
- [ILocalCircularPatternFeatureData::Symmetric](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Symmetric.html) is false.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html)
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.html)
[ILocalCircularPatternFeatureData::EqualSpacing Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~EqualSpacing.html)
[ILocalCircularPatternFeatureData::Spacing2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Spacing2.html)
[ILocalCircularPatternFeatureData::TotalInstances2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~TotalInstances2.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
