---
title: "Spacing2 Property (ILocalCircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCircularPatternFeatureData"
member: "Spacing2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Spacing2.html"
---

# Spacing2 Property (ILocalCircularPatternFeatureData)

Gets or sets the spacing between pattern instances in Direction 2 of this bidirectional circular component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Spacing2 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCircularPatternFeatureData
Dim value As System.Double

instance.Spacing2 = value

value = instance.Spacing2
```

### C#

```csharp
System.double Spacing2 {get; set;}
```

### C++/CLI

```cpp
property System.double Spacing2 {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance in radians between pattern instances in Direction 2

## VBA Syntax

See [LocalCircularPatternFeatureData::Spacing2](ms-its:sldworksapivb6.chm::/sldworks~LocalCircularPatternFeatureData~Spacing2.html).

## Remarks

This property is only available when:

- [ILocalCircularPatternFeatureData::Direction2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Spacing2.html) is true, and
- [ILocalCircularPatternFeatureData::Symmetric](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Symmetric.html) is false.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html)
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.html)
[ILocalCircularPatternFeatureData::Spacing Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Spacing.html)
[ILocalCircularPatternFeatureData::EqualSpacing2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~EqualSpacing2.html)
[ILocalCircularPatternFeatureData::TotalInstances2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~TotalInstances2.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
