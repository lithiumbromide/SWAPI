---
title: "GetMaterialPropertyValues2 Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetMaterialPropertyValues2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetMaterialPropertyValues2.html"
---

# GetMaterialPropertyValues2 Method (IFace2)

Gets the material property values for this face.

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
Dim instance As IFace2
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
- `Config_names`: Array of configuration names (see **Remarks**)

### Return Value

Array of material property values of the material for this face (see **Remarks**)

## VBA Syntax

See [Face2::GetMaterialPropertyValues2](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetMaterialPropertyValues2.html).

## Remarks

The material property values returned include the color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency, and emission.

If you set Config_opt to swThisConfiguration or swAllConfiguration, then pass Nothing because Config_names is ignored.

The format of material_values is an array of doubles:

[ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ]

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::IGetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetMaterialPropertyValues2.html)
[IFace2::IRemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IRemoveMaterialProperty2.html)
[IFace2::ISetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ISetMaterialPropertyValues2.html)
[IFace2::RemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveMaterialProperty2.html)
[IFace2::SetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetMaterialPropertyValues2.html)
[IFace2::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IMaterialPropertyValues.html)
[IFace2::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~MaterialPropertyValues.html)
[IFeature::GetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialPropertyValues2.html)
[IFeature::IGetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetMaterialPropertyValues2.html)
[IModelDoc2::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IMaterialPropertyValues.html)
[IModelDoc2::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~MaterialPropertyValues.html)
[IModelDocExtension::GetMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMaterialPropertyValues.html)
[IModelDocExtension::IGetMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetMaterialPropertyValues.html)
[IPartDoc::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IMaterialPropertyValues.html)
[IPartDoc::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialPropertyValues.html)
[IFace2::HasMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~HasMaterialPropertyValues.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
