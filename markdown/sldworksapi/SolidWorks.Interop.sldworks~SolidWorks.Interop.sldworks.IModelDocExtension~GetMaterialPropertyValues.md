---
title: "GetMaterialPropertyValues Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetMaterialPropertyValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMaterialPropertyValues.html"
---

# GetMaterialPropertyValues Method (IModelDocExtension)

Gets the material properties for this model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialPropertyValues( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Object

value = instance.GetMaterialPropertyValues(Config_opt, Config_names)
```

### C#

```csharp
System.object GetMaterialPropertyValues(
   System.int Config_opt,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.Object^ GetMaterialPropertyValues(
   System.int Config_opt,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Config_opt`: Configuration options as defined by [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_names`: Array of configuration names for this component

### Return Value

Array of material values for this component (see **Remarks**)

## VBA Syntax

See [ModelDocExtension::GetMaterialPropertyValues](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetMaterialPropertyValues.html).

## Remarks

The material values returned include the face color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency, and emission.

The format of material_values is an array of doubles:

[ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ]

Valid values are from 0 to 1 for all variables. If material_values is all -1 values, then material property values were not assigned to the feature. Therefore, the feature will have the default properties in the user interface.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::IGetMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetMaterialPropertyValues.html)
[IModelDocExtension::RemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveMaterialProperty.html)
[IModelDocExtension::IRemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IRemoveMaterialProperty.html)
[IModelDocExtension::SetMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetMaterialPropertyValues.html)
[IModelDocExtension::ISetMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ISetMaterialPropertyValues.html)
[IModelDocExtension::HasMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasMaterialPropertyValues.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
