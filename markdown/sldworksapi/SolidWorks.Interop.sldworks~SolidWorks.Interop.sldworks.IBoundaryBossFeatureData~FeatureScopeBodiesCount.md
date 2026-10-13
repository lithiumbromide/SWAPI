---
title: "FeatureScopeBodiesCount Property (IBoundaryBossFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData"
member: "FeatureScopeBodiesCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~FeatureScopeBodiesCount.html"
---

# FeatureScopeBodiesCount Property (IBoundaryBossFeatureData)

Gets the number of bodies that this boundary feature affects in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FeatureScopeBodiesCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundaryBossFeatureData
Dim value As System.Integer

value = instance.FeatureScopeBodiesCount
```

### C#

```csharp
System.int FeatureScopeBodiesCount {get;}
```

### C++/CLI

```cpp
property System.int FeatureScopeBodiesCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of bodies

## VBA Syntax

See [BoundaryBossFeatureData::FeatureScopeBodiesCount](ms-its:sldworksapivb6.chm::/sldworks~BoundaryBossFeatureData~FeatureScopeBodiesCount.html).

## Remarks

This property is only available when [IBoundaryBossFeatureData::FeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~FeatureScope.html) is true.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html)
[IBoundaryBossFeatureData::FeatureScopeBodies Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~FeatureScopeBodies.html)
[IBoundaryBossFeatureData::AutoSelect Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~AutoSelect.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
