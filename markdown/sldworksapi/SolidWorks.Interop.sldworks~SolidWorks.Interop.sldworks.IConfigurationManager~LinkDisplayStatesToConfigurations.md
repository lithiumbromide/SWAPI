---
title: "LinkDisplayStatesToConfigurations Property (IConfigurationManager)"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager"
member: "LinkDisplayStatesToConfigurations"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~LinkDisplayStatesToConfigurations.html"
---

# LinkDisplayStatesToConfigurations Property (IConfigurationManager)

Gets or sets whether to link or unlink display states to or from the active configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Property LinkDisplayStatesToConfigurations As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfigurationManager
Dim value As System.Boolean

instance.LinkDisplayStatesToConfigurations = value

value = instance.LinkDisplayStatesToConfigurations
```

### C#

```csharp
System.bool LinkDisplayStatesToConfigurations {get; set;}
```

### C++/CLI

```cpp
property System.bool LinkDisplayStatesToConfigurations {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to keep specific display states linked to the active configuration, false to unlink specific display states and make all display states available to the active configuration

## VBA Syntax

See [ConfigurationManager::LinkDisplayStatesToConfigurations](ms-its:sldworksapivb6.chm::/sldworks~configurationmanager~linkdisplaystatestoconfigurations.html).

## Examples

[Link Display States to Configurations (C#)](Link_Display_States_to_Configurations_Example_CSharp.htm)
[Link Display States to Configurations (VB.NET)](Link_Display_States_to_Configurations_Example_VBNET.htm)
[Link Display States to Configurations (VBA)](Link_Display_States_to_Configurations_Example_VB.htm)

## See Also

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html)
[IComponent2::ReferencedDisplayState Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReferencedDisplayState.html)
[IConfiguration::ApplyDisplayState Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ApplyDisplayState.html)
[IConfiguration::CopyDisplayStateFromConfiguration Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CopyDisplayStateFromConfiguration.html)
[IConfiguration::CreateDisplayState Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CreateDisplayState.html)
[IConfiguration::GetDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStates.html)
[IConfiguration::IGetDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetDisplayStates.html)
[IModelDocExtension::LinkedDisplayState Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~LinkedDisplayState.html)
[IPartDoc::RemoveAllDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~RemoveAllDisplayStates.html)
[IAssemblyDoc ActiveDisplayStateChangePostNotify Event](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ActiveDisplayStateChangePostNotifyEventHandler.html)
[IAssemblyDoc ActiveDisplayStateChangePreNotify Event](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ActiveDisplayStateChangePreNotifyEventHandler.html)
[IPartDoc ActiveDisplayStateChangePostNotify Event](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ActiveDisplayStateChangePostNotifyEventHandler.html)
[IPartDoc ActiveDisplayStateChangePreNotify Event](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ActiveDisplayStateChangePreNotifyEventHandler.html)

## Availability

SOLIDWORKS 2012 SP03, Revision Number 20.3
