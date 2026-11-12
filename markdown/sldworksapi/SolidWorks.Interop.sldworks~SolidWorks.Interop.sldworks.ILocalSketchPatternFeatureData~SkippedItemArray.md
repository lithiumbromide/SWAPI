---
title: "SkippedItemArray Property (ILocalSketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalSketchPatternFeatureData"
member: "SkippedItemArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~SkippedItemArray.html"
---

# SkippedItemArray Property (ILocalSketchPatternFeatureData)

Gets or sets the array of skipped components in this sketch-driven component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property SkippedItemArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalSketchPatternFeatureData
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

Array of integers representing skipped components

## VBA Syntax

See [LocalSketchPatternFeatureData::SkippedItemArray](ms-its:sldworksapivb6.chm::/sldworks~LocalSketchPatternFeatureData~SkippedItemArray.html).

## Remarks

This array is 0-based. If you skip the third and fifth components, then the array looks like ArrayOut[0]=3 and ArrayOut[1]=5.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILocalSketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData.html)
[ILocalSketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData_members.html)
[ILocalSketchPatternFeatureData::GetSkippedItemCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~GetSkippedItemCount.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
