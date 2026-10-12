---
title: "TotalInstances2 Property (ILocalCircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCircularPatternFeatureData"
member: "TotalInstances2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~TotalInstances2.html"
---

# TotalInstances2 Property (ILocalCircularPatternFeatureData)

Gets or sets the total number of pattern instances in Direction 2 of this bidirectional circular component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property TotalInstances2 As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCircularPatternFeatureData
Dim value As System.Integer

instance.TotalInstances2 = value

value = instance.TotalInstances2
```

### C#

```csharp
System.int TotalInstances2 {get; set;}
```

### C++/CLI

```cpp
property System.int TotalInstances2 {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Total number of pattern instances in Direction 2

## VBA Syntax

See [LocalCircularPatternFeatureData::TotalInstances2](ms-its:sldworksapivb6.chm::/sldworks~LocalCircularPatternFeatureData~TotalInstances2.html).

## Remarks

This property is only available when:

- [ILocalCircularPatternFeatureData::Direction2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Direction2.html) is true, and
- [ILocalCircularPatternFeatureData::Symmetric](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Symmetric.html) is false.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html)
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.html)
[ILocalCircularPatternFeatureData::TotalInstances Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~TotalInstances.html)
[ILocalCircularPatternFeatureData::EqualSpacing2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~EqualSpacing2.html)
[ILocalCircularPatternFeatureData::Spacing2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~Spacing2.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
