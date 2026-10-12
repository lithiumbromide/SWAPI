---
title: "Entities Property (IDisplayStateSetting)"
project: "SOLIDWORKS API Help"
interface: "IDisplayStateSetting"
member: "Entities"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Entities.html"
---

# Entities Property (IDisplayStateSetting)

Gets and sets the entities for this display state setting.

## Syntax

### Visual Basic (Declaration)

```vb
Property Entities As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayStateSetting
Dim value As System.Object

instance.Entities = value

value = instance.Entities
```

### C#

```csharp
System.object Entities {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Entities {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of entities

## VBA Syntax

See [DisplayStateSetting::Entities](ms-its:sldworksapivb6.chm::/sldworks~DisplayStateSetting~Entities.html).

## Examples

[Get Display State Settings (C#)](Get_Display_State_Settings_CSharp.htm)
[Get Display State Settings (VB.NET)](Get_Display_State_Settings_VBNET.htm)
[Get Display State Settings (VBA)](Get_Display_State_Settings_Example_VB.htm)
[Change Color of Component in Specific Display State (C#)](Change_Color_of_Component_in_Specific_Display_State_Example_CSharp.htm)
[Change Color of Component in Specific Display State (VB.NET)](Change_Color_of_Component_in_Specific_Display_State_Example_VBNET.htm)
[Change Color of Component in Specific Display State (VBA)](Change_Color_of_Component_in_Specific_Display_State_Example_VB.htm)

## Remarks

After calling this method:

1. Call [IDisplayStateSetting::Names](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~Names.html) to specify the display states.
2. Call [IDisplayStateSetting::Option](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayStateSetting~Option.html) to specify the display state scope of the setting.
3. Get or set one or more of the following properties for the specified display states, entities, and scope:

  - [IModelDocExtension::DisplayMode](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~DisplayMode.html)
  - [IModelDocExtension::Transparency](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~Transparency.html)
  - [IModelDocExtension::Visibility](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~Visibility.html)
4. Call [IModelDocExtension::GetAppearanceSetting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetAppearanceSetting.html) to obtain an [IAppearanceSetting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAppearanceSetting.html) object.
5. Set the properties in the IAppearanceSetting object.
6. Get or set the material properties for the specified display states, entities, and scope using [IModelDocExtension::DisplayStateSpecMaterialPropertyValues](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~DisplayStateSpecMaterialPropertyValues.html).

## See Also

[IDisplayStateSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting.html)
[IDisplayStateSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting_members.html)
[IDisplayStateSetting::IGetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~IGetEntities.html)
[IDisplayStateSetting::ISetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~ISetEntities.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
