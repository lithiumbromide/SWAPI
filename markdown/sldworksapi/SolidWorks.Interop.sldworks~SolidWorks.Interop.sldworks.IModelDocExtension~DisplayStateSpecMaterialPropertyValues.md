---
title: "DisplayStateSpecMaterialPropertyValues Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "DisplayStateSpecMaterialPropertyValues"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayStateSpecMaterialPropertyValues.html"
---

# DisplayStateSpecMaterialPropertyValues Property (IModelDocExtension)

Gets and sets the appearance settings for the specified display state setting.

## Syntax

### Visual Basic (Declaration)

```vb
Property DisplayStateSpecMaterialPropertyValues( _
   ByVal Setting As DisplayStateSetting _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Setting As DisplayStateSetting
Dim value As System.Object

instance.DisplayStateSpecMaterialPropertyValues(Setting) = value

value = instance.DisplayStateSpecMaterialPropertyValues(Setting)
```

### C#

```csharp
System.object DisplayStateSpecMaterialPropertyValues(
   DisplayStateSetting Setting
) {get; set;}
```

### C++/CLI

```cpp
property System.Object^ DisplayStateSpecMaterialPropertyValues {
   System.Object^ get(DisplayStateSetting^ Setting);
   void set (DisplayStateSetting^ Setting, System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Setting`: [IDisplayStateSetting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting.html) (see **Remarks**)

### Property Value

One-dimensional array of [IAppearanceSetting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAppearanceSetting.html)s (see **Remarks**)

## VBA Syntax

See [ModelDocExtension::DisplayStateSpecMaterialPropertyValues](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~DisplayStateSpecMaterialPropertyValues.html).

## Examples

[Change Color of Component in Specific Display State (C#)](Change_Color_of_Component_in_Specific_Display_State_Example_CSharp.htm)
[Change Color of Component in Specific Display State (VB.NET)](Change_Color_of_Component_in_Specific_Display_State_Example_VBNET.htm)
[Change Color of Component in Specific Display State (VBA)](Change_Color_of_Component_in_Specific_Display_State_Example_VB.htm)

## Remarks

Before using this method to get or set appearance settings:

1. Call [IModelDocExtension::GetDisplayStateSetting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetDisplayStateSetting.html) to obtain an [IDisplayStateSetting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting.html) object.
2. Call [IDisplayStateSetting::Names](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~Names.html) or [IDisplayStateSetting::ISetNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~ISetNames.html) to specify the display states.
3. Call [IDisplayStateSetting::Entities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~Entities.html) or [IDisplayStateSetting::ISetEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~ISetEntities.html) to specify the components.
4. Call [IDisplayStateSetting::Option](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~Option.html) to specify the display state scope of the setting.
5. Specify the Setting parameter using the IDisplayStateSetting object.

Each [IAppearanceSetting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAppearanceSetting.html) in the array returned by this method maps to a component in a display state. The size of the returned array is ([IDisplayStateSetting::GetEntityCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~GetEntityCount.html) * [IDisplayStateSetting::GetNameCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~GetNameCount.html)).

The returned array stores appearance settings (AS) for N components in M display states as follows:

Component1 DisplayState1 AS, Component1 DisplayState2 AS, ..., Component1 DisplayStateM AS,

Component2 DisplayState1 AS, Component2 DisplayState2 AS, ..., Component2 DisplayStateM AS,

...

ComponentN DisplayState1 AS, ComponentN DisplayState2 AS, ..., ComponentN DisplayStateM AS

Before using this method to set appearance settings:

1. Perform steps1-5 as described above.
2. Call [IModelDocExtension::GetAppearanceSetting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetAppearanceSetting.html) to obtain an [IAppearanceSetting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAppearanceSetting.html) object.
3. Set the properties in the IAppearanceSetting object for the component in the display state.
4. Repeat steps 2 and 3 for each component in each display state.
5. Create an array of the IAppearanceSetting objects in the order described above.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::DisplayMode Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayMode.html)
[IModelDocExtension::Transparency Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Transparency.html)
[IModelDocExtension::Visibility Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Visibility.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
