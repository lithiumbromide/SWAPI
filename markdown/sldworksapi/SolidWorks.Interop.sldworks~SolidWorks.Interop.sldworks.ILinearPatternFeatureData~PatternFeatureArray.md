---
title: "PatternFeatureArray Property (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "PatternFeatureArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~PatternFeatureArray.html"
---

# PatternFeatureArray Property (ILinearPatternFeatureData)

Gets or sets the seed features in this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternFeatureArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
Dim value As System.Object

instance.PatternFeatureArray = value

value = instance.PatternFeatureArray
```

### C#

```csharp
System.object PatternFeatureArray {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PatternFeatureArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html) for this pattern

## VBA Syntax

See [LinearPatternFeatureData::PatternFeatureArray](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~PatternFeatureArray.html).

## Examples

[Change Linear Pattern (C#)](Change_Linear_Pattern_Example_CSharp.htm)
[Change Linear Pattern (VB.NET)](Change_Linear_Pattern_Example_VBNET.htm)
[Change Linear Pattern (VBA)](Change_Linear_Pattern_Example_VB.htm)

## Remarks

This property is valid only if [ILinearPatternFeatureData::BodyPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~BodyPattern.html) is false.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::GetPatternFeatureCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetPatternFeatureCount.html)
[ILinearPatternFeatureData::IGetPatternFeatureArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~IGetPatternFeatureArray.html)
[ILinearPatternFeatureData::ISetPatternFeatureArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~ISetPatternFeatureArray.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
