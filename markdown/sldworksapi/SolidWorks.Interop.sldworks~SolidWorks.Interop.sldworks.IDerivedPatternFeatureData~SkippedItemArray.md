---
title: "SkippedItemArray Property (IDerivedPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPatternFeatureData"
member: "SkippedItemArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~SkippedItemArray.html"
---

# SkippedItemArray Property (IDerivedPatternFeatureData)

Gets or sets the list of skipped items for this derived pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SkippedItemArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPatternFeatureData
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

Array of the skipped items

## VBA Syntax

See [DerivedPatternFeatureData::SkippedItemArray](ms-its:sldworksapivb6.chm::/sldworks~DerivedPatternFeatureData~SkippedItemArray.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IDerivedPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.html)
[IDerivedPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData_members.html)
[IDerivedPatternFeatureData::GetSkippedItemCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~GetSkippedItemCount.html)
[IDerivedPatternFeatureData::IGetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~IGetSkippedItemArray.html)
[IDerivedPatternFeatureData::ISetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~ISetSkippedItemArray.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
