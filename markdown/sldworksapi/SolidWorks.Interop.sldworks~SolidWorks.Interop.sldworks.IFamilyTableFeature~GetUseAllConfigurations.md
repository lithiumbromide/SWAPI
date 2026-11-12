---
title: "GetUseAllConfigurations Method (IFamilyTableFeature)"
project: "SOLIDWORKS API Help"
interface: "IFamilyTableFeature"
member: "GetUseAllConfigurations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~GetUseAllConfigurations.html"
---

# GetUseAllConfigurations Method (IFamilyTableFeature)

Gets whether all configurations are used in this family table feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUseAllConfigurations() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFamilyTableFeature
Dim value As System.Boolean

value = instance.GetUseAllConfigurations()
```

### C#

```csharp
System.bool GetUseAllConfigurations()
```

### C++/CLI

```cpp
System.bool GetUseAllConfigurations();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if all configurations are used, false if only some are used.

## VBA Syntax

See [FamilyTableFeature::GetUseAllConfigurations](ms-its:sldworksapivb6.chm::/sldworks~FamilyTableFeature~GetUseAllConfigurations.html).

## Remarks

Use [IFamilyTableFeature::GetConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~GetConfigurations.html) to obtain the configurations used in this feature.

## See Also

[IFamilyTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature.html)
[IFamilyTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
