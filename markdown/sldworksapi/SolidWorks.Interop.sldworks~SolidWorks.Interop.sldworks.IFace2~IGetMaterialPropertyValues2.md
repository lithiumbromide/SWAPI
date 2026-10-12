---
title: "IGetMaterialPropertyValues2 Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IGetMaterialPropertyValues2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetMaterialPropertyValues2.html"
---

# IGetMaterialPropertyValues2 Method (IFace2)

Gets the material property values for this face.

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
Dim instance As IFace2
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
- `Config_count`: Number of configurations
- `Config_names`: Array of configuration names (see **Remarks**)

### Return Value

- in-process, unmanaged C++: Pointer to an array of 9 doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The material property values returned include the color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency, and emission.

If you set Config_opt to swThisConfiguration or swAllConfiguration, then pass Nothing because Config_names is ignored.

The format of material_values is an array of doubles:

[ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ]

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetMaterialPropertyValues2.html)
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
[IModelDocExtension::IGetMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetMaterialPropertyValues.html)
[IModelDocExtension::GetMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMaterialPropertyValues.html)
[IPartDoc::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialPropertyValues.html)
[IPartDoc::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IMaterialPropertyValues.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
