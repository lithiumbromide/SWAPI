---
title: "FeatureXpert Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "FeatureXpert"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FeatureXpert.html"
---

# FeatureXpert Method (IPartDoc)

Executes FeatureXpert, powered by SOLIDWORKS Intelligent Feature Technology ( SWIFT), in parts.

## Syntax

### Visual Basic (Declaration)

```vb
Sub FeatureXpert()
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc

instance.FeatureXpert()
```

### C#

```csharp
void FeatureXpert()
```

### C++/CLI

```cpp
void FeatureXpert();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [PartDoc::FeatureXpert](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~FeatureXpert.html).

## Remarks

FeatureXpert works behind the scenes to resolve feature errors in [constant radius fillets](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2.html), [neutral plane drafts](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDraftFeatureData2.html), and [reference planes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html).

You must enable the FeatureXpert system option before using this method:

```vb
swApp.SetUserPreferenceToggle swUserEnableAutoFix, True
```

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IFeatureManager::DraftXpertChange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~DraftXpertChange.html)
[IFeatureManager::DraftXpertRemove Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~DraftXpertRemove.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
