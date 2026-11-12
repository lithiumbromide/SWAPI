---
title: "GetMaterialPropertyValues2 Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetMaterialPropertyValues2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialPropertyValues2.html"
---

# GetMaterialPropertyValues2 Method (IComponent2)

Gets the material properties for this component.

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
Dim instance As IComponent2
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

- `Config_opt`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_names`: Array of configuration names for this component (see **Remarks**)

### Return Value

The material properties values include the color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency, and emission.

## VBA Syntax

See [Component2::GetMaterialPropertyValues2](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetMaterialPropertyValues2.html).

## Remarks

If you set Config_opt to swThisConfiguration or swAllConfiguration, then pass an empty Variant, Nothing, or any Variant because Config_names is ignored.

The format of material_values is an array of doubles:

[ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ]

Valid values are from 0 to 1 for all variables. If material_values is all -1 values, then material property values were not assigned to the component. Therefore, the component will have the default properties in the user interface.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::RemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemoveMaterialProperty2.html)
[IComponent2::SetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetMaterialPropertyValues2.html)
[IComponent2::IGetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetMaterialPropertyValues2.html)
[IComponent2::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MaterialPropertyValues.html)
[IComponent2::GetModelMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetModelMaterialPropertyValues.html)
[IComponent2::IGetModelMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetModelMaterialPropertyValues.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
