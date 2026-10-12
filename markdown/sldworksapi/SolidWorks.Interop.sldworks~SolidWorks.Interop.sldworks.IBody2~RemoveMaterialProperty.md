---
title: "RemoveMaterialProperty Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "RemoveMaterialProperty"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveMaterialProperty.html"
---

# RemoveMaterialProperty Method (IBody2)

Removes the material property values (e.g., color) from the body in the specified configurations in parts and assemblies.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveMaterialProperty( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean

value = instance.RemoveMaterialProperty(Config_opt, Config_names)
```

### C#

```csharp
System.bool RemoveMaterialProperty(
   System.int Config_opt,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.bool RemoveMaterialProperty(
   System.int Config_opt,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Config_opt`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_names`: Array of configuration names

## VBA Syntax

See [Body2::RemoveMaterialProperty](ms-its:sldworksapivb6.chm::/sldworks~Body2~RemoveMaterialProperty.html).

## Examples

[Remove Material Properties from Body (C#)](Remove_Material_From_Bodies_Example_CSharp.htm)
[Remove Material Properties from Body (VB.NET)](Remove_Material_From_Bodies_Example_VBNET.htm)
[Remove Material Properties from Body (VBA)](Remove_Material_From_Bodies_Example_VB.htm)

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IRemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IRemoveMaterialProperty.html)
[IBody2::IGetMaterialPropertyValuesForFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetMaterialPropertyValuesForFace.html)
[IBody2::IMaterialPropertyValues2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMaterialPropertyValues2.html)
[IBody2::MaterialPropertyValues2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MaterialPropertyValues2.html)
[IBody2::GetMaterialIdName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialIdName2.html)
[IBody2::GetMaterialPropertyName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialPropertyName.html)
[IBody2::GetMaterialUserName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialUserName2.html)
[IBody2::SetMaterialIdName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialIdName2.html)
[IBody2::SetMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialProperty.html)
[IBody2::SetMaterialUserName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialUserName2.html)
[IBody2::HasMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~HasMaterialPropertyValues.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
