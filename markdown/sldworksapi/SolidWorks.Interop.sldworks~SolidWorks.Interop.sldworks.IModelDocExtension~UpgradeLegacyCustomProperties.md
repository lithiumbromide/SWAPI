---
title: "UpgradeLegacyCustomProperties Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "UpgradeLegacyCustomProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpgradeLegacyCustomProperties.html"
---

# UpgradeLegacyCustomProperties Method (IModelDocExtension)

Upgrades custom properties in this legacy (created prior to SOLIDWORKS 2018) model to the latest custom properties architecture.

## Syntax

### Visual Basic (Declaration)

```vb
Function UpgradeLegacyCustomProperties( _
   ByVal UpgradeAllAssemComps As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim UpgradeAllAssemComps As System.Boolean
Dim value As System.Boolean

value = instance.UpgradeLegacyCustomProperties(UpgradeAllAssemComps)
```

### C#

```csharp
System.bool UpgradeLegacyCustomProperties(
   System.bool UpgradeAllAssemComps
)
```

### C++/CLI

```cpp
System.bool UpgradeLegacyCustomProperties(
   System.bool UpgradeAllAssemComps
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UpgradeAllAssemComps`: True to upgrade custom properties of this top-level assembly and all of its components, false to upgrade custom properties of this top-level assembly only

### Return Value

True if custom properties are successfully upgraded, false if not

## VBA Syntax

See [ModelDocExtension::UpgradeLegacyCustomProperties](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~UpgradeLegacyCustomProperties.html).

## Remarks

This method is valid only for parts, assemblies, and drawings:

- created prior to 2018.
- opened in resolved mode.
- corresponds to the user-interface command, `feature_manager_design_tree_top_node` **RMB** **> Upgrade custom properties**.

This method upgrades the custom properties of:

- parent parts only, not derived parts
- drawings, but not models in drawing views
- weldment cutlists
- (optionally) all components in assemblies

After running this method, you:

- must rebuild configurations to have their custom properties updated.
- cannot return to the old custom properties architecture.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
