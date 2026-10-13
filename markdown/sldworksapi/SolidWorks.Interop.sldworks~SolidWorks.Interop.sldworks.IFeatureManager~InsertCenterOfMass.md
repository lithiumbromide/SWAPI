---
title: "InsertCenterOfMass Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertCenterOfMass"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCenterOfMass.html"
---

# InsertCenterOfMass Method (IFeatureManager)

Inserts a Center of Mass feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCenterOfMass() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As Feature

value = instance.InsertCenterOfMass()
```

### C#

```csharp
Feature InsertCenterOfMass()
```

### C++/CLI

```cpp
Feature^ InsertCenterOfMass();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertCenterOfMass](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertCenterOfMass.html).

## Examples

[Insert Center of Mass Feature (VBA)](Insert_Center_of_Mass_Feature_Example_VB.htm)
[Insert Center of Mass Feature (VB.NET)](Insert_Center_of_Mass_Feature_Example_VBNET.htm)
[Insert Center of Mass Feature (C#)](Insert_Center_of_Mass_Feature_Example_CSharp.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::InsertCenterOfMassReferencePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCenterOfMassReferencePoint.html)
[ICenterOfMass Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterOfMass.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
