---
title: "ISetMaterialPropertyValues2 Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "ISetMaterialPropertyValues2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ISetMaterialPropertyValues2.html"
---

# ISetMaterialPropertyValues2 Method (IComponent2)

Sets the material properties for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetMaterialPropertyValues2( _
   ByRef Material_values As System.Double, _
   ByVal Config_opt As System.Integer, _
   ByVal Config_count As System.Integer, _
   ByRef Config_names As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim Material_values As System.Double
Dim Config_opt As System.Integer
Dim Config_count As System.Integer
Dim Config_names As System.String

instance.ISetMaterialPropertyValues2(Material_values, Config_opt, Config_count, Config_names)
```

### C#

```csharp
void ISetMaterialPropertyValues2(
   ref System.double Material_values,
   System.int Config_opt,
   System.int Config_count,
   ref System.string Config_names
)
```

### C++/CLI

```cpp
void ISetMaterialPropertyValues2(
   System.double% Material_values,
   System.int Config_opt,
   System.int Config_count,
   System.String^% Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Material_values`: Array of doubles of size 9 (see **Remarks**)
- `Config_opt`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_count`: Number of configurations for this component
- `Config_names`: - in-process, unmanaged C++: Pointer to an array of configuration names of size Config_count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The material property values include the color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency, and emission.

The format of Material_values is an array of doubles:

**[** `R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission` **]**

To see a color change, you must:

1. Specify `R`, `G`, and `B`, each with a value between 0.0 and 1.0, inclusive. (These values are internally multiplied by 255.0 to determine the RGB color.)
2. Specify the reflectivity properties (`Diffuse`, `Specular`, `Shininess` (1.0 - Specular spread/Blurriness)), each with a value greater than 0.0 and less than or equal to 1.0.
3. Specify `Ambient`, `Transparency` and `Emission`, each with a value between 0.0 and 1.0, inclusive.
4. Refresh the graphics area after calling this method.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::SetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetMaterialPropertyValues2.html)
[IComponent2::IGetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetMaterialPropertyValues2.html)
[IComponent2::GetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialPropertyValues2.html)
[IComponent2::RemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemoveMaterialProperty2.html)
[IComponent2::IRemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IRemoveMaterialProperty2.html)
[IComponent2::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IMaterialPropertyValues.html)
[IComponent2::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MaterialPropertyValues.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
