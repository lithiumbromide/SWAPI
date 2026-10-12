---
title: "PatternFeature Property (IDerivedPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPatternFeatureData"
member: "PatternFeature"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~PatternFeature.html"
---

# PatternFeature Property (IDerivedPatternFeatureData)

Gets or sets the pattern feature for this derived pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternFeature As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPatternFeatureData
Dim value As System.Object

instance.PatternFeature = value

value = instance.PatternFeature
```

### C#

```csharp
System.object PatternFeature {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PatternFeature {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pattern [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html) on which to base this derived pattern feature

## VBA Syntax

See [DerivedPatternFeatureData::PatternFeature](ms-its:sldworksapivb6.chm::/sldworks~DerivedPatternFeatureData~PatternFeature.html).

## Examples

[Create Derived Pattern Feature (C#)](Create_Derived_Pattern_Feature_Example_CSharp.htm)
[Create Derived Pattern Feature (VB.NET)](Create_Derived_Pattern_Feature_Example_VBNET.htm)
[Create Derived Pattern Feature (VBA)](Create_Derived_Pattern_Feature_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IDerivedPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.html)
[IDerivedPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData_members.html)
[IDerivedPatternFeatureData::DrivingFeatureSkippedItemArray Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~DrivingFeatureSkippedItemArray.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
