---
title: "LinkedDisplayState Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "LinkedDisplayState"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~LinkedDisplayState.html"
---

# LinkedDisplayState Property (IModelDocExtension)

Gets or sets whether a display state is linked in this part.

## Syntax

### Visual Basic (Declaration)

```vb
Property LinkedDisplayState As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Boolean

instance.LinkedDisplayState = value

value = instance.LinkedDisplayState
```

### C#

```csharp
System.bool LinkedDisplayState {get; set;}
```

### C++/CLI

```cpp
property System.bool LinkedDisplayState {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if linked, false if not linked

## VBA Syntax

See [ModelDocExtension::LinkedDisplayState](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~LinkedDisplayState.html).

## Examples

[Create, Unlink, and Purge Display States in Part (VB.NET)](Create,_Unlink,_and_Purge_Display_States_in_Part_Example_VBNET.htm)
[Create, Unlink, and Purge Display States in Part (VBA)](Create,_Unlink,_and_Purge_Display_States_in_Part_Example_VB.htm)
[Create, Unlink, and Purge Display States in Part (C#)](Create,_Unlink,_and_Purge_Display_States_in_Part_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IConfiguration::ApplyDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ApplyDisplayState.html)
[IConfiguration::CreateDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CreateDisplayState.html)
[IConfiguration::DeleteDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteDisplayState.html)
[IConfiguration::GetDisplayStates Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStates.html)
[IConfiguration::GetDisplayStatesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStatesCount.html)
[IConfiguration::CopyDisplayStateFromConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CopyDisplayStateFromConfiguration.html)
[IModelDocExtension::PurgeDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PurgeDisplayState.html)
[IConfigurationManager::LinkDisplayStatesToConfigurations Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~LinkDisplayStatesToConfigurations.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
