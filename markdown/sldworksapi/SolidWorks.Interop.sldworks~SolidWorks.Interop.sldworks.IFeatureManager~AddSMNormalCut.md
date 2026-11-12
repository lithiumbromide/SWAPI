---
title: "AddSMNormalCut Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "AddSMNormalCut"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddSMNormalCut.html"
---

# AddSMNormalCut Method (IFeatureManager)

Obsolete. See [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) and the Remarks in [ISMNormalCutGroupData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutGroupData.html), and [ISMNormalCutFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddSMNormalCut() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Integer

value = instance.AddSMNormalCut()
```

### C#

```csharp
System.int AddSMNormalCut()
```

### C++/CLI

```cpp
System.int AddSMNormalCut();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Result code as defined in [swSMNormalCutError_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSMNormalCutError_e.html)

## VBA Syntax

See [FeatureManager::AddSMNormalCut](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~AddSMNormalCut.html).

## Remarks

To create a sheet metal Normal Cut feature, see the [IFeatureManager::AddSMNormalCutType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddSMNormalCutType.html) Remarks and Example sections.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::FinishSMNormalCut Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FinishSMNormalCut.html)
[ISMNormalCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
