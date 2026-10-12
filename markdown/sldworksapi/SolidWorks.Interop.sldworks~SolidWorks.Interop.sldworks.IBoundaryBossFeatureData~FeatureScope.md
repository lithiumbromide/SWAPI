---
title: "FeatureScope Property (IBoundaryBossFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundaryBossFeatureData"
member: "FeatureScope"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~FeatureScope.html"
---

# FeatureScope Property (IBoundaryBossFeatureData)

Gets or sets whether to use scope for the boundary feature in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Property FeatureScope As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundaryBossFeatureData
Dim value As System.Boolean

instance.FeatureScope = value

value = instance.FeatureScope
```

### C#

```csharp
System.bool FeatureScope {get; set;}
```

### C++/CLI

```cpp
property System.bool FeatureScope {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if only the [specified bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~FeatureScopeBodies.html) in the multibody part are affected by the boundary feature, false if all of the bodies in the multibody part are affected by the boundary feature

## VBA Syntax

See [BoundaryBossFeatureData::FeatureScope](ms-its:sldworksapivb6.chm::/sldworks~BoundaryBossFeatureData~FeatureScope.html).

## Remarks

This property is only available when the curves are [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) or [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html).

The boundary feature is expanded along the plane on which the feature is created and selects all or only the specified bodies it intersects.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.html)
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html)
[IBoundaryBossFeatureData::AutoSelect Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~AutoSelect.html)
[IBoundaryBossFeatureData::FeatureScopeBodiesCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~FeatureScopeBodiesCount.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
