---
title: "GetDisplayStateSetting Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetDisplayStateSetting"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDisplayStateSetting.html"
---

# GetDisplayStateSetting Method (IModelDocExtension)

Gets the display state setting for the specified scope.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayStateSetting( _
   ByVal Option As System.Integer _
) As DisplayStateSetting
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Option As System.Integer
Dim value As DisplayStateSetting

value = instance.GetDisplayStateSetting(Option)
```

### C#

```csharp
DisplayStateSetting GetDisplayStateSetting(
   System.int Option
)
```

### C++/CLI

```cpp
DisplayStateSetting^ GetDisplayStateSetting(
   System.int Option
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Option`: Scope of the display state setting as defined in [swDisplayStateOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayStateOpts_e.html)

### Return Value

[IDisplayStateSetting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting.html)

## VBA Syntax

See [ModelDocExtension::GetDisplayStateSetting](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~GetDisplayStateSetting.html).

## Examples

[Get Display State Settings (VBA)](Get_Display_State_Settings_Example_VB.htm)
[Get Display State Settings (VB.NET)](Get_Display_State_Settings_VBNET.htm)
[Get Display State Settings (C#)](Get_Display_State_Settings_CSharp.htm)
[Change Color of Component in Specific Display State (C#)](Change_Color_of_Component_in_Specific_Display_State_Example_CSharp.htm)
[Change Color of Component in Specific Display State (VB.NET)](Change_Color_of_Component_in_Specific_Display_State_Example_VBNET.htm)
[Change Color of Component in Specific Display State (VBA)](Change_Color_of_Component_in_Specific_Display_State_Example_VB.htm)

## Remarks

After calling this method:

1. Call [IDisplayStateSetting::Names](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~Names.html) or [IDisplayStateSetting::ISetNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~ISetNames.html) to specify the display states.
2. Call [IDisplayStateSetting::Entities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~Entities.html) or [IDisplayStateSetting::ISetEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~ISetEntities.html) to specify the components.
3. Get or set one or more of the following properties for the specified display states, components, and scope:

  - [IModelDocExtension::DisplayMode](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~DisplayMode.html)
  - [IModelDocExtension::Transparency](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~Transparency.html)
  - [IModelDocExtension::Visibility](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~Visibility.html)
4. Call [IModelDocExtension::GetAppearanceSetting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetAppearanceSetting.html) to obtain the [IAppearanceSetting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAppearanceSetting.html) object.
5. Set the properties in the IAppearanceSetting object.
6. Get or set the material properties for the specified display states, components, and scope using [IModelDocExtension::DisplayStateSpecMaterialPropertyValues](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~DisplayStateSpecMaterialPropertyValues.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
