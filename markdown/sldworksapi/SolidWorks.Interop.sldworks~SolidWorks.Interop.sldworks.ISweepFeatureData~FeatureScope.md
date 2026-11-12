---
title: "FeatureScope Property (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "FeatureScope"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~FeatureScope.html"
---

# FeatureScope Property (ISweepFeatureData)

Gets or sets whether to use scope in a multibody part for this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FeatureScope As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
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

- true (default), only specified bodies in the multibody part are affected by the sweep feature
- false, all of the bodies in the multibody part are affected by the sweep feature

## VBA Syntax

See [SweepFeatureData::FeatureScope](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~FeatureScope.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

The sweep feature is expanded along the plane on which the feature is created and affects all or only the specified bodies it intersects. Use [ISweepFeatureData::FeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~FeatureScopeBodies.html) to specify the bodies.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::GetFeatureScopeBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetFeatureScopeBodiesCount.html)
[ISweepFeatureData::IGetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IGetFeatureScopeBodies.html)
[ISweepFeatureData::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~ISetFeatureScopeBodies.html)
[ISweepFeatureData::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~AutoSelect.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
