---
title: "GetDisplayStates Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetDisplayStates"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStates.html"
---

# GetDisplayStates Method (IConfiguration)

Gets the names of the display states for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayStates() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Object

value = instance.GetDisplayStates()
```

### C#

```csharp
System.object GetDisplayStates()
```

### C++/CLI

```cpp
System.Object^ GetDisplayStates();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of the names of the display states for this configuration

## VBA Syntax

See [Configuration::GetDisplayStates](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetDisplayStates.html).

## Examples

[Add and Delete Appearances from Specific Display States (C#)](Add_and_Delete_Materials_from_Specific_Display_States_Example_CSharp.htm)
[Add and Delete Appearances from Specific Display States (VB.NET)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VBNET.htm)
[Add and Delete Appearances from Specific Display States (VBA)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VB.htm)
[Get Display States and Visibilities of Components (C#)](Get_Display_State_Names_and_Visibilites_of_Components_Example_CSharp.htm)
[Get Display States and Visibilities of Components (VB.NET)](Get_Display_State_Names_and_Visibilites_of_Components_Example_VBNET.htm)
[Get Display States and Visibilities of Components (VBA)](Get_Display_State_Names_and_Visibilites_of_Components_Example_VB.htm)

## Remarks

The first name in the list is the active display state. If more than one display state is active in the current model, call [IComponent2::ReferencedDisplayState](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~ReferencedDisplayState.html) to obtain the active display state for each component in the model that references this configuration.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::ApplyDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ApplyDisplayState.html)
[IConfiguration::GetDisplayStatesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStatesCount.html)
[IConfiguration::IGetDisplayStates Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetDisplayStates.html)
[IConfiguration::CopyDisplayStateFromConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CopyDisplayStateFromConfiguration.html)
[IConfiguration::RenameDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~RenameDisplayState.html)
[IConfiguration::CreateDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CreateDisplayState.html)
[IConfigurationManager::LinkDisplayStatesToConfigurations Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~LinkDisplayStatesToConfigurations.html)
[IConfiguration::GetDisplayStateBodyProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateBodyProperties.html)
[IConfiguration::GetDisplayStateComponentProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateComponentProperties.html)
[IConfiguration::GetDisplayStateComponentVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateComponentVisibility.html)
[IConfiguration::GetDisplayStateFaceProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateFaceProperties.html)
[IConfiguration::GetDisplayStateFeatureProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateFeatureProperties.html)
[IConfiguration::GetDisplayStateProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateProperties.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
