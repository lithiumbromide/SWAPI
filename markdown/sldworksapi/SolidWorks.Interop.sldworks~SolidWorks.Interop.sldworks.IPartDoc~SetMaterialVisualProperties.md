---
title: "SetMaterialVisualProperties Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "SetMaterialVisualProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialVisualProperties.html"
---

# SetMaterialVisualProperties Method (IPartDoc)

Sets the material visual properties for the active configuration and any specified configurations of this part.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMaterialVisualProperties( _
   ByVal Properties As MaterialVisualPropertiesData, _
   ByVal ConfigOption As System.Integer, _
   ByVal ConfigNames As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Properties As MaterialVisualPropertiesData
Dim ConfigOption As System.Integer
Dim ConfigNames As System.Object
Dim value As System.Integer

value = instance.SetMaterialVisualProperties(Properties, ConfigOption, ConfigNames)
```

### C#

```csharp
System.int SetMaterialVisualProperties(
   MaterialVisualPropertiesData Properties,
   System.int ConfigOption,
   System.object ConfigNames
)
```

### C++/CLI

```cpp
System.int SetMaterialVisualProperties(
   MaterialVisualPropertiesData^ Properties,
   System.int ConfigOption,
   System.Object^ ConfigNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Properties`: [Material visual properties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMaterialVisualPropertiesData.html)
- `ConfigOption`: Configurations as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `ConfigNames`: Array of strings of the names of the configurations whose material visual properties to set

### Return Value

0 on success, non-0 on failure

## VBA Syntax

See [PartDoc::SetMaterialVisualProperties](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~SetMaterialVisualProperties.html).

## Examples

[Get and Set Material Visual Properties (VBA)](Get_and_Set_Material_Visual_Properties_Example_VB.htm)
[Get and Set Material Visual Properties (VB.NET)](Get_and_Set_Material_Visual_Properties_Example_VBNET.htm)
[Get and Set Material Visual Properties (C#)](Get_and_Set_Material_Visual_Properties_Example_CSharp.htm)

## Remarks

ConfigNames is used only when ConfigOption is set to swSpecifyConfiguration. If a different value is specified for ConfigOption, then ConfigNames is ignored.

This method always affects the active configuration, regardless of the value specified for ConfigNames.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::GetMaterialPropertyName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialPropertyName2.html)
[IPartDoc::GetMaterialVisualProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialVisualProperties.html)
[IPartDoc::SetMaterialPropertyName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialPropertyName2.html)
[IPartDoc::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IMaterialPropertyValues.html)
[IPartDoc::MaterialIdName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialIdName.html)
[IPartDoc::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialPropertyValues.html)
[IPartDoc::MaterialUserName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialUserName.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
