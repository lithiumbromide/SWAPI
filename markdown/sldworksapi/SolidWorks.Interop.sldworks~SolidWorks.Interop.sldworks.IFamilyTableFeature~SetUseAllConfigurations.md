---
title: "SetUseAllConfigurations Method (IFamilyTableFeature)"
project: "SOLIDWORKS API Help"
interface: "IFamilyTableFeature"
member: "SetUseAllConfigurations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~SetUseAllConfigurations.html"
---

# SetUseAllConfigurations Method (IFamilyTableFeature)

Sets whether to use all configurations in this family table feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetUseAllConfigurations( _
   ByVal UseAllConfigs As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFamilyTableFeature
Dim UseAllConfigs As System.Boolean

instance.SetUseAllConfigurations(UseAllConfigs)
```

### C#

```csharp
void SetUseAllConfigurations(
   System.bool UseAllConfigs
)
```

### C++/CLI

```cpp
void SetUseAllConfigurations(
   System.bool UseAllConfigs
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseAllConfigs`: True to use all configurations, false to not

## VBA Syntax

See [FamilyTableFeature::SetUseAllConfigurations](ms-its:sldworksapivb6.chm::/sldworks~FamilyTableFeature~SetUseAllConfigurations.html).

## See Also

[IFamilyTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature.html)
[IFamilyTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
