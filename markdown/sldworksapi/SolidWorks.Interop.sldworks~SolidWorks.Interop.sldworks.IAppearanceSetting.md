---
title: "IAppearanceSetting Interface"
project: "SOLIDWORKS API Help"
interface: "IAppearanceSetting"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.html"
---

# IAppearanceSetting Interface

Allows access to visual property settings.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IAppearanceSetting
```

### Visual Basic (Usage)

```vb
Dim instance As IAppearanceSetting
```

### C#

```csharp
public interface IAppearanceSetting
```

### C++/CLI

```cpp
public interface class IAppearanceSetting
```

## VBA Syntax

See [AppearanceSetting](ms-its:sldworksapivb6.chm::/sldworks~AppearanceSetting.html).

## Examples

[Change Color of Component in Specific Display State (C#)](Change_Color_of_Component_in_Specific_Display_State_Example_CSharp.htm)
[Change Color of Component in Specific Display State (VB.NET)](Change_Color_of_Component_in_Specific_Display_State_Example_VBNET.htm)
[Change Color of Component in Specific Display State (VBA)](Change_Color_of_Component_in_Specific_Display_State_Example_VB.htm)

## Remarks

After implementing this interface:

1. Set one or more properties in the IAppearanceSetting object.
2. Call [IModelDocExtension::GetDisplayStateSetting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetDisplayStateSetting.html) to obtain an [IDisplayStateSetting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting.html) object.
3. Call [IDisplayStateSetting::Names](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~Names.html) or [IDisplayStateSetting::ISetNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~ISetNames.html) to specify the display states.
4. Call [IDisplayStateSetting::Entities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~Entities.html) or [IDisplayStateSetting::ISetEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~ISetEntities.html) to specify the components.
5. Call [IDisplayStateSetting::Option](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~Option.html) to specify the display state scope of the setting.
6. Get or set the visual properties for the specified display states, components, and scope using [IModelDocExtension::DisplayStateSpecMaterialPropertyValues](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~DisplayStateSpecMaterialPropertyValues.html).

## Accessors

[IModelDocExtension::GetAppearanceSetting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetAppearanceSetting.html)

[IModelDocExtension::DisplayStateSpecMaterialPropertyValues](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~DisplayStateSpecMaterialPropertyValues.html)

[ISwScene::FloorSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorSelection.html)

## Access Diagram

[AppearanceSetting](SWObjectModel.pdf#AppearanceSetting)

## See Also

[IAppearanceSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
