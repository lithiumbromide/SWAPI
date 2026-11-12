---
title: "MergeResult Property (IBoundaryBossFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData"
member: "MergeResult"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~MergeResult.html"
---

# MergeResult Property (IBoundaryBossFeatureData)

Gets or sets whether to merge all boundary feature elements.

## Syntax

### Visual Basic (Declaration)

```vb
Property MergeResult As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundaryBossFeatureData
Dim value As System.Boolean

instance.MergeResult = value

value = instance.MergeResult
```

### C#

```csharp
System.bool MergeResult {get; set;}
```

### C++/CLI

```cpp
property System.bool MergeResult {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to merge all boundary feature elements, false to not

## VBA Syntax

See [BoundaryBossFeatureData::MergeResult](ms-its:sldworksapivb6.chm::/sldworks~BoundaryBossFeatureData~MergeResult.html).

## Remarks

This property is only available when the curves are [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) or [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html)
[IBoundaryBossFeatureData::MergeTangentFaces Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~MergeTangentFaces.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
