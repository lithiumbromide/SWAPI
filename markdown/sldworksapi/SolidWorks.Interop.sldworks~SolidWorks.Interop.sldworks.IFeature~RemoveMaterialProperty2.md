---
title: "RemoveMaterialProperty2 Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "RemoveMaterialProperty2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveMaterialProperty2.html"
---

# RemoveMaterialProperty2 Method (IFeature)

Removes material property values from this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveMaterialProperty2( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean

value = instance.RemoveMaterialProperty2(Config_opt, Config_names)
```

### C#

```csharp
System.bool RemoveMaterialProperty2(
   System.int Config_opt,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.bool RemoveMaterialProperty2(
   System.int Config_opt,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Config_opt`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_names`: Array of configuration names

### Return Value

True if material property values are removed, false if not

## VBA Syntax

See [Feature::RemoveMaterialProperty2](ms-its:sldworksapivb6.chm::/sldworks~Feature~RemoveMaterialProperty2.html).

## Remarks

This method is intended to be used on features that have a changed material property value, for example, color.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::IRemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IRemoveMaterialProperty2.html)
[IFeature::GetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialPropertyValues2.html)
[IFeature::IGetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetMaterialPropertyValues2.html)
[IFeature::ISetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetMaterialPropertyValues2.html)
[IFeature::SetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialPropertyValues2.html)
[IFeature::HasMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~HasMaterialPropertyValues.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
