---
title: "GetMaterialPropertyValues2 Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetMaterialPropertyValues2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialPropertyValues2.html"
---

# GetMaterialPropertyValues2 Method (IFeature)

Gets the material property values for this feature in the specified configurations.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialPropertyValues2( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Object

value = instance.GetMaterialPropertyValues2(Config_opt, Config_names)
```

### C#

```csharp
System.object GetMaterialPropertyValues2(
   System.int Config_opt,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.Object^ GetMaterialPropertyValues2(
   System.int Config_opt,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Config_opt`: Configuration options as defined by [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_names`: Array of configuration names for this component (see **Remarks**)

### Return Value

Array of material property values for this component

## VBA Syntax

See [Feature::GetMaterialPropertyValues2](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetMaterialPropertyValues2.html).

## Examples

[Get Material Properties (VBA)](Get_Material_Properties_Example_VB.htm)

## Remarks

The material property values returned include the face color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency, and emission. Valid values are between 0.0 and 1.0, inclusive, for all material properties. If a return value is -1, then that material property was not set for this feature.

If you set Config_opt to swThisConfiguration or swAllConfiguration, then Config_names is ignored. The size of the returned array depends on how you specify Config_opt and Config_names. See the example.

The format of the returned array:

[ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ] * `number_of_configurations`

where:

`number_of_configurations` = number of configurations specified by Config_opt and Config_names

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::IGetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetMaterialPropertyValues2.html)
[IFeature::ISetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetMaterialPropertyValues2.html)
[IFeature::IRemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IRemoveMaterialProperty2.html)
[IFeature::RemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveMaterialProperty2.html)
[IFeature::SetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialPropertyValues2.html)
[IFeature::HasMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~HasMaterialPropertyValues.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
