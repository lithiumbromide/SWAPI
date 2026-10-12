---
title: "RemoveMaterialProperty2 Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "RemoveMaterialProperty2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemoveMaterialProperty2.html"
---

# RemoveMaterialProperty2 Method (IComponent2)

Removes the appearance from the component.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveMaterialProperty2( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean

value = instance.RemoveMaterialProperty2(Config_opt, Config_names)
```

### C#

```csharp
System.bool RemoveMaterialProperty2(
   System.int Config_opt,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.bool RemoveMaterialProperty2(
   System.int Config_opt,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Config_opt`: Configuration options as defined by [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_names`: Array of configuration names for this component

### Return Value

True if the component's appearance is removed, false if not

## VBA Syntax

See [Component2::RemoveMaterialProperty2](ms-its:sldworksapivb6.chm::/sldworks~Component2~RemoveMaterialProperty2.html).

## Examples

[Remove Material Properties from Assembly Component (VBA)](Remove_Material_Properties_from_Assembly_Component_Example_VB.htm)

## Remarks

This method is intended to be used on a component whose appearance has changed; for example, color.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::IRemoveMaterialProperty2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IRemoveMaterialProperty2.html)
[IComponent2::GetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialPropertyValues2.html)
[IComponent2::IGetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetMaterialPropertyValues2.html)
[IComponent2::ISetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ISetMaterialPropertyValues2.html)
[IComponent2::SetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetMaterialPropertyValues2.html)
[IComponent2::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MaterialPropertyValues.html)
[IComponent2::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IMaterialPropertyValues.html)
[IComponent2::HasMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~HasMaterialPropertyValues.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
