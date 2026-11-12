---
title: "SkippedItemArray Property (ILinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILinearPatternFeatureData"
member: "SkippedItemArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~SkippedItemArray.html"
---

# SkippedItemArray Property (ILinearPatternFeatureData)

Gets or sets the items skipped in this linear pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SkippedItemArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILinearPatternFeatureData
Dim value As System.Object

instance.SkippedItemArray = value

value = instance.SkippedItemArray
```

### C#

```csharp
System.object SkippedItemArray {get; set;}
```

### C++/CLI

```cpp
property System.Object^ SkippedItemArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of integers representing skipped items

## VBA Syntax

See [LinearPatternFeatureData::SkippedItemArray](ms-its:sldworksapivb6.chm::/sldworks~LinearPatternFeatureData~SkippedItemArray.html).

## Remarks

The array is 0-based. If you skip the third and fifth items, then the array looks like ArrayOut[0]=3 and ArrayOut[1]=5.

To calculate the pattern instance numbers to skip:

Calculate:

For a bi-directional pattern:

`I` = `n2` * (`i` - 1) + (`j` - 1)

For a uni-directional pattern:

`I` = `i` - 1

where:

- `I` = pattern instance number
- `n2` = number of instances in Direction 2
- `i` = index for Direction 1
- `j` = index for Direction 2

In the pattern's PropertyManager, find `n2` in the **Direction 2** **> Spacing and Instances > Number of instances** field and find [`i,j`] in the **Modified Instances** section.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Linear Patterns and the Linear Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.html)
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html)
[ILinearPatternFeatureData::GetSkippedItemCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetSkippedItemCount.html)
[ILinearPatternFeatureData::IGetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~IGetSkippedItemArray.html)
[ILinearPatternFeatureData::ISetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~ISetSkippedItemArray.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
