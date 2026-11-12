---
title: "IRemoveMaterialProperty2 Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IRemoveMaterialProperty2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IRemoveMaterialProperty2.html"
---

# IRemoveMaterialProperty2 Method (IComponent2)

Removes material property values from the component.

## Syntax

### Visual Basic (Declaration)

```vb
Function IRemoveMaterialProperty2( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_count As System.Integer, _
   ByRef Config_names As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim Config_opt As System.Integer
Dim Config_count As System.Integer
Dim Config_names As System.String
Dim value As System.Boolean

value = instance.IRemoveMaterialProperty2(Config_opt, Config_count, Config_names)
```

### C#

```csharp
System.bool IRemoveMaterialProperty2(
   System.int Config_opt,
   System.int Config_count,
   ref System.string Config_names
)
```

### C++/CLI

```cpp
System.bool IRemoveMaterialProperty2(
   System.int Config_opt,
   System.int Config_count,
   System.String^% Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Config_opt`: Configuration options as defined by [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_count`: Number of configurations for this component
- `Config_names`: Array of configuration names for this component

### Return Value

True if the material property values are removed, false if not

## Remarks

This method is intended to be used on components whose material property value has changed; for example, color.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialPropertyValues2.html)
[IComponent2::IGetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetMaterialPropertyValues2.html)
[IComponent2::RemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemoveMaterialProperty2.html)
[IComponent2::ISetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ISetMaterialPropertyValues2.html)
[IComponent2::SetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetMaterialPropertyValues2.html)
[IComponent2::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MaterialPropertyValues.html)
[IComponent2::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IMaterialPropertyValues.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.o
