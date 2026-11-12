---
title: "FeatureScopeBodies Property (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "FeatureScopeBodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~FeatureScopeBodies.html"
---

# FeatureScopeBodies Property (ISweepFeatureData)

Gets or sets the solid bodies in a multibody part affected by this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FeatureScopeBodies As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Object

instance.FeatureScopeBodies = value

value = instance.FeatureScopeBodies
```

### C#

```csharp
System.object FeatureScopeBodies {get; set;}
```

### C++/CLI

```cpp
property System.Object^ FeatureScopeBodies {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of solid [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) that the feature affects

## VBA Syntax

See [SweepFeatureData::FeatureScopeBodies](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~FeatureScopeBodies.html).

## Remarks

This property is valid only if [ISweepFeatureData::FeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~FeatureScope.html) is set to true.

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
