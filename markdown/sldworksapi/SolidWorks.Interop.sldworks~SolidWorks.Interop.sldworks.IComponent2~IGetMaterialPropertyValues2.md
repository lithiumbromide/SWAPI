---
title: "IGetMaterialPropertyValues2 Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IGetMaterialPropertyValues2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetMaterialPropertyValues2.html"
---

# IGetMaterialPropertyValues2 Method (IComponent2)

Gets the material properties for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMaterialPropertyValues2( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_count As System.Integer, _
   ByRef Config_names As System.String _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim Config_opt As System.Integer
Dim Config_count As System.Integer
Dim Config_names As System.String
Dim value As System.Double

value = instance.IGetMaterialPropertyValues2(Config_opt, Config_count, Config_names)
```

### C#

```csharp
System.double IGetMaterialPropertyValues2(
   System.int Config_opt,
   System.int Config_count,
   ref System.string Config_names
)
```

### C++/CLI

```cpp
System.double IGetMaterialPropertyValues2(
   System.int Config_opt,
   System.int Config_count,
   System.String^% Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Config_opt`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_count`: Number of configurations for this component
- `Config_names`: Array of configuration names for this component (see **Remarks**)

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles of size 9 doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

If you set Config_opt to swThisConfiguration or swAllConfiguration, then pass an empty array because Config_names is ignored.

The format of material_values is an array of doubles:

[ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ]

Valid values are from 0 to 1 for all variables. If material_values is all -1 values, then material property values were not assigned to the component. Therefore, the component will have the default properties in the user interface.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::IRemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IRemoveMaterialProperty2.html)
[IComponent2::ISetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ISetMaterialPropertyValues2.html)
[IComponent2::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IMaterialPropertyValues.html)
[IComponent2::GetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialPropertyValues2.html)
[IComponent2::HasMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~HasMaterialPropertyValues.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
