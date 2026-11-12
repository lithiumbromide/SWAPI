---
title: "FeatureName Property (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FeatureName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureName.html"
---

# FeatureName Property (IFeatureManager)

Gets the feature name for the specified feature ID.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FeatureName( _
   ByVal NameID As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim NameID As System.Integer
Dim value As System.String

value = instance.FeatureName(NameID)
```

### C#

```csharp
System.string FeatureName(
   System.int NameID
) {get;}
```

### C++/CLI

```cpp
property System.String^ FeatureName {
   System.String^ get(System.int NameID);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NameID`: Feature ID as defined in [swFeatureNameID_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureNameID_e.html)

### Property Value

Feature name

## VBA Syntax

See [FeatureManager::FeatureName](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FeatureName.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeature::GetTypeName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName.html)
[IFeatureManager::ShowFeatureName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowFeatureName.html)
[IFeature::Name Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Name.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number
