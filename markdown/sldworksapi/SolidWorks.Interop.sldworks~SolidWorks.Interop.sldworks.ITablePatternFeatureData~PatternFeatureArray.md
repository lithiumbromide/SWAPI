---
title: "PatternFeatureArray Property (ITablePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData"
member: "PatternFeatureArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PatternFeatureArray.html"
---

# PatternFeatureArray Property (ITablePatternFeatureData)

Gets or sets the seed features used to create the table-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternFeatureArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITablePatternFeatureData
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

Array of the [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) used to create this table-driven pattern feature

## VBA Syntax

See [TablePatternFeatureData::PatternFeatureArray](ms-its:sldworksapivb6.chm::/sldworks~TablePatternFeatureData~PatternFeatureArray.html).

## Examples

[Get Table-driven Pattern Properties (VBA)](Get_Table-driven_Pattern_Properties_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html)
[ITablePatternFeatureData::GetPatternFeatureCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetPatternFeatureCount.html)
[ITablePatternFeatureData::IGetPatternFeatureArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetPatternFeatureArray.html)
[ITablePatternFeatureData::ISetPatternFeatureArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetPatternFeatureArray.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
