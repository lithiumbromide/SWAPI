---
title: "FinishSMNormalCut Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FinishSMNormalCut"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FinishSMNormalCut.html"
---

# FinishSMNormalCut Method (IFeatureManager)

Obsolete. See [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) and the Remarks in [ISMNormalCutGroupData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutGroupData.html), and [ISMNormalCutFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FinishSMNormalCut() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Object

value = instance.FinishSMNormalCut()
```

### C#

```csharp
System.object FinishSMNormalCut()
```

### C++/CLI

```cpp
System.Object^ FinishSMNormalCut();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::FinishSMNormalCut](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~FinishSMNormalCut.html).

## Remarks

To create a sheet metal Normal Cut feature, see the [IFeatureManager::AddSMNormalCutType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddSMNormalCutType.html) Remarks and Example sections.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::AddSMNormalCut Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddSMNormalCut.html)
[ISMNormalCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
