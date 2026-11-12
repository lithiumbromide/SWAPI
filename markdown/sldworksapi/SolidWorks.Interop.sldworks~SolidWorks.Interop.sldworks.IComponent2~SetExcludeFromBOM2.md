---
title: "SetExcludeFromBOM2 Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "SetExcludeFromBOM2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetExcludeFromBOM2.html"
---

# SetExcludeFromBOM2 Method (IComponent2)

Sets whether to exclude this component from the bills of materials (BOMs) in the specified configurations.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetExcludeFromBOM2( _
   ByVal Exclude As System.Boolean, _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim Exclude As System.Boolean
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Integer

value = instance.SetExcludeFromBOM2(Exclude, Config_opt, Config_names)
```

### C#

```csharp
System.int SetExcludeFromBOM2(
   System.bool Exclude,
   System.int Config_opt,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.int SetExcludeFromBOM2(
   System.bool Exclude,
   System.int Config_opt,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Exclude`: True to exclude it, false to not
- `Config_opt`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_names`: Array of the names of configurations for which to set Exclude; null or Nothing if Config_opt is set to swInConfigurationOpts.swAllConfiguration or swInConfigurationOpts.swThisConfiguration

### Return Value

Return code as defined in [swExcludeFromBOMError_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swExcludeFromBOMError_e.html)

## VBA Syntax

See [Component2::SetExcludeFromBOM2](ms-its:sldworksapivb6.chm::/sldworks~Component2~SetExcludeFromBOM2.html).

## Remarks

This method is valid only for [table-based bills of materials](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html); it does not work for Microsoft Excel-based bills of materials.

If you set Exclude to true, the name of the component changes in the FeatureManager design tree of the specified configuration; (Excluded from BOM) is appended. To update the FeatureManager design tree, call [IFeatureManager::UpdateFeatureTree](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~UpdateFeatureTree.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IAssemblyDoc::CompConfigProperties6 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties6.html)
[IComponent2::GetExcludeFromBOM2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetExcludeFromBOM2.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
