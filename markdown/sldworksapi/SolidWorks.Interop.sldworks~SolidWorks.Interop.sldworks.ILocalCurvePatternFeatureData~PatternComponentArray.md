---
title: "PatternComponentArray Property (ILocalCurvePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCurvePatternFeatureData"
member: "PatternComponentArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~PatternComponentArray.html"
---

# PatternComponentArray Property (ILocalCurvePatternFeatureData)

Gets or sets the components in this curve-driven component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternComponentArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCurvePatternFeatureData
Dim value As System.Object

instance.PatternComponentArray = value

value = instance.PatternComponentArray
```

### C#

```csharp
System.object PatternComponentArray {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PatternComponentArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) in this local curve-driven pattern feature

## VBA Syntax

See [LocalCurvePatternFeatureData::PatternComponentArray](ms-its:sldworksapivb6.chm::/sldworks~LocalCurvePatternFeatureData~PatternComponentArray.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILocalCurvePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.html)
[ILocalCurvePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData_members.html)
[ILocalCurvePatternFeatureData::GetPatternComponentCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~GetPatternComponentCount.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
