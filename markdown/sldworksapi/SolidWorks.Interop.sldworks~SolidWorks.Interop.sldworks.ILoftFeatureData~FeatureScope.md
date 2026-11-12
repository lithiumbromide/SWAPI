---
title: "FeatureScope Property (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "FeatureScope"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~FeatureScope.html"
---

# FeatureScope Property (ILoftFeatureData)

Gets or sets whether to use scope for the loft feature in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Property FeatureScope As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
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

When:

- true, only the specified bodies in the multibody part are affected by the loft feature
- false, all of the bodies in the multibody part are affected by the loft feature

## VBA Syntax

See [LoftFeatureData::FeatureScope](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~FeatureScope.html).

## Remarks

The loft feature is expanded along the plane on which the feature is created and affects all or only the specified bodies it intersects.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)
[ILoftFeatureData::GetFeatureScopeBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetFeatureScopeBodiesCount.html)
[ILoftFeatureData::IGetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IGetFeatureScopeBodies.html)
[ILoftFeatureData::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ISetFeatureScopeBodies.html)
[ILoftFeatureData::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~AutoSelect.html)
[ILoftFeatureData::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~FeatureScopeBodies.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
