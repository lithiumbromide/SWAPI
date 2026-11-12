---
title: "UpgradeLegacyCThreads Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "UpgradeLegacyCThreads"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpgradeLegacyCThreads.html"
---

# UpgradeLegacyCThreads Method (IModelDocExtension)

Upgrades cosmetic thread features in this legacy model to the latest cosmetic thread architecture.

## Syntax

### Visual Basic (Declaration)

```vb
Function UpgradeLegacyCThreads() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Boolean

value = instance.UpgradeLegacyCThreads()
```

### C#

```csharp
System.bool UpgradeLegacyCThreads()
```

### C++/CLI

```cpp
System.bool UpgradeLegacyCThreads();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if cosmetic threads upgraded successfully in this legacy model, false if not

## VBA Syntax

See [ModelDocExtension::UpgradeLegacyCThreads](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~UpgradeLegacyCThreads.html).

## Remarks

This method:

- is valid only if the system option allowing the upgrade of legacy files containing cosmetic threads is selected.
- corresponds to the user-interface command, `feature_manager_design_tree_top_node` **RMB** **> Upgrade cosmetic thread features**.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::HasLegacyCThreads Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasLegacyCThreads.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
