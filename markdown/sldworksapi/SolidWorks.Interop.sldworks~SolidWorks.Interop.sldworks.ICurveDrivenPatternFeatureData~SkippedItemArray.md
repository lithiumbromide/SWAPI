---
title: "SkippedItemArray Property (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "SkippedItemArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~SkippedItemArray.html"
---

# SkippedItemArray Property (ICurveDrivenPatternFeatureData)

Gets or sets the skipped items for this curve-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SkippedItemArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData
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

Array of integers representing the skipped items

## VBA Syntax

See [CurveDrivenPatternFeatureData::SkippedItemArray](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~SkippedItemArray.html).

## Remarks

This array is 0-based. If you skip the third and fifth items, then the array looks like ArrayOut[0]=3 and ArrayOut[1]=5.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)
[ICurveDrivenPatternFeatureData::GetSkippedItemCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~GetSkippedItemCount.html)
[ICurveDrivenPatternFeatureData::IGetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~IGetSkippedItemArray.html)
[ICurveDrivenPatternFeatureData::ISetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~ISetSkippedItemArray.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
