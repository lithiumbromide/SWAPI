---
title: "PatternBodyArray Property (ITablePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData"
member: "PatternBodyArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PatternBodyArray.html"
---

# PatternBodyArray Property (ITablePatternFeatureData)

Gets or sets the seed bodies to pattern for this table-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PatternBodyArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITablePatternFeatureData
Dim value As System.Object

instance.PatternBodyArray = value

value = instance.PatternBodyArray
```

### C#

```csharp
System.object PatternBodyArray {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PatternBodyArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) to pattern

## VBA Syntax

See [TablePatternFeatureData::PatternBodyArray](ms-its:sldworksapivb6.chm::/sldworks~TablePatternFeatureData~PatternBodyArray.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html)
[ITablePatternFeatureData::GetPatternBodyCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetPatternBodyCount.html)
[ITablePatternFeatureData::IGetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetPatternBodyArray.html)
[ITablePatternFeatureData::ISetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetPatternBodyArray.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
