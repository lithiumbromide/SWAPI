---
title: "SkippedItemArray Property (ILocalCircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCircularPatternFeatureData"
member: "SkippedItemArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~SkippedItemArray.html"
---

# SkippedItemArray Property (ILocalCircularPatternFeatureData)

Gets or sets the skipped components in this circular component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SkippedItemArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCircularPatternFeatureData
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

Array of integers representing the skipped components

## VBA Syntax

See [LocalCircularPatternFeatureData::SkippedItemArray](ms-its:sldworksapivb6.chm::/sldworks~LocalCircularPatternFeatureData~SkippedItemArray.html).

## Remarks

This array is 0-based. If you skip the third and fifth components, then the array looks like ArrayOut[0]=3 and ArrayOut[1]=5.

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

## See Also

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.html)
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.html)
[ILocalCircularPatternFeatureData::GetSkippedItemCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~GetSkippedItemCount.html)
[ILocalCircularPatternFeatureData::IGetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~IGetSkippedItemArray.html)
[ILocalCircularPatternFeatureData::ISetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~ISetSkippedItemArray.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
