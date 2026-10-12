---
title: "SetConfigurations Method (IFamilyTableFeature)"
project: "SOLIDWORKS API Help"
interface: "IFamilyTableFeature"
member: "SetConfigurations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~SetConfigurations.html"
---

# SetConfigurations Method (IFamilyTableFeature)

Sets the configurations to use for this family table feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetConfigurations( _
   ByVal ConfigArray As System.Object, _
   ByVal VisibilityArray As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFamilyTableFeature
Dim ConfigArray As System.Object
Dim VisibilityArray As System.Object

instance.SetConfigurations(ConfigArray, VisibilityArray)
```

### C#

```csharp
void SetConfigurations(
   System.object ConfigArray,
   System.object VisibilityArray
)
```

### C++/CLI

```cpp
void SetConfigurations(
   System.Object^ ConfigArray,
   System.Object^ VisibilityArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigArray`: Array of configurations
- `VisibilityArray`: Array of booleans indicating visiblity, in order, of ConfigArray items; null or Nothing to indicate that all configurations are visible

## VBA Syntax

See [FamilyTableFeature::SetConfigurations](ms-its:sldworksapivb6.chm::/sldworks~FamilyTableFeature~SetConfigurations.html).

## Remarks

This method is valid only if [IFamilyTableFeature::GetUseAllConfigurations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~GetUseAllConfigurations.html) is set to false.

## See Also

[IFamilyTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature.html)
[IFamilyTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
