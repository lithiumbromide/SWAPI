---
title: "CreateDisplayState Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "CreateDisplayState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CreateDisplayState.html"
---

# CreateDisplayState Method (IConfiguration)

Creates a display state for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateDisplayState( _
   ByVal DisplayStateName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim DisplayStateName As System.String
Dim value As System.Boolean

value = instance.CreateDisplayState(DisplayStateName)
```

### C#

```csharp
System.bool CreateDisplayState(
   System.string DisplayStateName
)
```

### C++/CLI

```cpp
System.bool CreateDisplayState(
   System.String^ DisplayStateName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DisplayStateName`: Name of display state to create for this configuration

### Return Value

True if the display state is created, false if not

## VBA Syntax

See [Configuration::CreateDisplayState](ms-its:sldworksapivb6.chm::/sldworks~Configuration~CreateDisplayState.html).

## Examples

[Create, Unlink, and Purge Display States in a Part (C#)](Create,_Unlink,_and_Purge_Display_States_in_Part_Example_CSharp.htm)
[Create, Unlink, and Purge Display States in a Part (VB.NET)](Create,_Unlink,_and_Purge_Display_States_in_Part_Example_VBNET.htm)
[Create, Unlink, and Purge Display States in a Part (VBA)](Create,_Unlink,_and_Purge_Display_States_in_Part_Example_VB.htm)
[Add and Delete Appearances from Specific Display States (C#)](Add_and_Delete_Materials_from_Specific_Display_States_Example_CSharp.htm)
[Add and Delete Appearances from Specific Display States (VB.NET)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VBNET.htm)
[Add and Delete Appearances from Specific Display States (VBA)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VB.htm)

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::ApplyDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ApplyDisplayState.html)
[IConfiguration::DeleteDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteDisplayState.html)
[IConfiguration::CopyDisplayStateFromConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CopyDisplayStateFromConfiguration.html)
[IConfiguration::GetDisplayStatesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStatesCount.html)
[IConfiguration::RenameDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~RenameDisplayState.html)
[IModelDocExtension::AddDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDisplayStateSpecificRenderMaterial.html)
[IModelDocExtension::IAddDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IAddDisplayStateSpecificRenderMaterial.html)
[IConfigurationManager::LinkDisplayStatesToConfigurations Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~LinkDisplayStatesToConfigurations.html)
[IConfiguration::GetDisplayStates Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStates.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
