---
title: "IRemoveMaterialProperty Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IRemoveMaterialProperty"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IRemoveMaterialProperty.html"
---

# IRemoveMaterialProperty Method (IBody2)

Removes the material property values (e.g., color) from the body in the specified configurations in parts and assemblies.

## Syntax

### Visual Basic (Declaration)

```vb
Function IRemoveMaterialProperty( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_count As System.Integer, _
   ByRef Config_names As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Config_opt As System.Integer
Dim Config_count As System.Integer
Dim Config_names As System.String
Dim value As System.Boolean

value = instance.IRemoveMaterialProperty(Config_opt, Config_count, Config_names)
```

### C#

```csharp
System.bool IRemoveMaterialProperty(
   System.int Config_opt,
   System.int Config_count,
   ref System.string Config_names
)
```

### C++/CLI

```cpp
System.bool IRemoveMaterialProperty(
   System.int Config_opt,
   System.int Config_count,
   System.String^% Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Config_opt`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_count`: Number of configurations in the part or assembly
- `Config_names`: Array of configuration names

### Return Value

True if the material is removed from the body, false if not

## VBA Syntax

See [Body2::IRemoveMaterialProperty](ms-its:sldworksapivb6.chm::/sldworks~Body2~IRemoveMaterialProperty.html).

## Remarks

Before calling this method, call [IModelDoc2::GetConfigurationCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetConfigurationCount.html) to get the value for Config_Count.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::RemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveMaterialProperty.html)
[IBody2::IGetMaterialPropertyValuesForFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetMaterialPropertyValuesForFace.html)
[IBody2::IMaterialPropertyValues2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMaterialPropertyValues2.html)
[IBody2::MaterialPropertyValues2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MaterialPropertyValues2.html)
[IBody2::GetMaterialIdName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialIdName2.html)
[IBody2::GetMaterialPropertyName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialPropertyName.html)
[IBody2::SetMaterialIdName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialIdName2.html)
[IBody2::SetMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialProperty.html)
[IBody2::SetMaterialUserName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~SetMaterialUserName2.html)
[IBody2::GetMaterialUserName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMaterialUserName2.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
