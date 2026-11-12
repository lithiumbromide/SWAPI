---
title: "SetMaterialPropertyValues2 Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "SetMaterialPropertyValues2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialPropertyValues2.html"
---

# SetMaterialPropertyValues2 Method (IFeature)

Sets the material property values for this feature in the specified configurations.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMaterialPropertyValues2( _
   ByVal Material_values As System.Object, _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim Material_values As System.Object
Dim Config_opt As System.Integer
Dim Config_names As System.Object

instance.SetMaterialPropertyValues2(Material_values, Config_opt, Config_names)
```

### C#

```csharp
void SetMaterialPropertyValues2(
   System.object Material_values,
   System.int Config_opt,
   System.object Config_names
)
```

### C++/CLI

```cpp
void SetMaterialPropertyValues2(
   System.Object^ Material_values,
   System.int Config_opt,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Material_values`: Array of material property values
- `Config_opt`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_names`: Array of configuration names

## VBA Syntax

See [Feature::SetMaterialPropertyValues2](ms-its:sldworksapivb6.chm::/sldworks~Feature~SetMaterialPropertyValues2.html).

## Remarks

The material properties are color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency, and emission. Valid values are between 0.0 and 1.0, inclusive, for all material properties.

If you set Config_opt to swThisConfiguration or swAllConfiguration, then Config_names is ignored.

The format of the Material_values array:

[ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ]

To see a color change, you must:

1. Specify `R`, `G`, and `B`, each with a value between 0.0 and 1.0, inclusive. (These values are internally multiplied by 255.0 to determine the RGB color.)
2. Specify the reflectivity properties (`Diffuse`, `Specular`, `Shininess` (1.0 - Specular spread/Blurriness)), each with a value greater than 0.0 and less than or equal to 1.0.
3. Specify `Ambient`, `Transparency` and `Emission`, each with a value between 0.0 and 1.0, inclusive.
4. Refresh the graphics area after calling this method.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::ISetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetMaterialPropertyValues2.html)
[IFeature::GetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialPropertyValues2.html)
[IFeature::IGetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetMaterialPropertyValues2.html)
[IFeature::IRemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IRemoveMaterialProperty2.html)
[IFeature::RemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveMaterialProperty2.html)
[IFeature::HasMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~HasMaterialPropertyValues.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
