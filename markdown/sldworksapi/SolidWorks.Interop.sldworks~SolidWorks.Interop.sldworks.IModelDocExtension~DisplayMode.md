---
title: "DisplayMode Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "DisplayMode"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayMode.html"
---

# DisplayMode Property (IModelDocExtension)

Gets and sets the display modes for the specified display state setting.

## Syntax

### Visual Basic (Declaration)

```vb
Property DisplayMode( _
   ByVal Setting As DisplayStateSetting _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Setting As DisplayStateSetting
Dim value As System.Object

instance.DisplayMode(Setting) = value

value = instance.DisplayMode(Setting)
```

### C#

```csharp
System.object DisplayMode(
   DisplayStateSetting Setting
) {get; set;}
```

### C++/CLI

```cpp
property System.Object^ DisplayMode {
   System.Object^ get(DisplayStateSetting^ Setting);
   void set (DisplayStateSetting^ Setting, System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Setting`: [IDisplayStateSetting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting.html)

### Property Value

One-dimensional array of display modes as defined in [swDisplayMode_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayMode_e.html) (see **Remarks**)

## VBA Syntax

See [ModelDocExtension::DisplayMode](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~DisplayMode.html).

## Examples

[Get Display State Settings (VBA)](Get_Display_State_Settings_Example_VB.htm)
[Get Display State Settings (VB.NET)](Get_Display_State_Settings_VBNET.htm)
[Get Display State Settings (C#)](Get_Display_State_Settings_CSharp.htm)

## Remarks

Before calling this method:

1. Call [IModelDocExtension::GetDisplayStateSetting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetDisplayStateSetting.html) to obtain an [IDisplayStateSetting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting.html) object.
2. Call [IDisplayStateSetting::Names](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~Names.html) or [IDisplayStateSetting::ISetNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~ISetNames.html) to specify the display states.
3. Call [IDisplayStateSetting::Entities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~Entities.html) or [IDisplayStateSetting::ISetEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~ISetEntities.html) to specify the components.
4. Call [IDisplayStateSetting::Option](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~Option.html) to specify the display state scope of the setting.
5. Specify the Setting parameter using the IDisplayStateSetting object.

Each display mode in the array returned by this method maps to a component in a display state. The size of the returned array is ([IDisplayStateSetting::GetEntityCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~GetEntityCount.html) X [IDisplayStateSetting::GetNameCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~GetNameCount.html)).

The returned array stores display modes (DM) for N components in M display states as follows:

Component1 DisplayState1 DM, Component1 DisplayState2 DM, ..., Component1 DisplayStateM DM,

Component2 DisplayState1 DM, Component2 DisplayState2 DM, ..., Component2 DisplayStateM DM,

...,

ComponentN DisplayState1 DM, ComponentN DisplayState2 DM, ..., ComponentN DisplayStateM DM

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::DisplayStateSpecMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayStateSpecMaterialPropertyValues.html)
[IModelDocExtension::Transparency Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Transparency.html)
[IModelDocExtension::Visibility Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Visibility.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
