---
title: "PurgeDisplayState Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "PurgeDisplayState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PurgeDisplayState.html"
---

# PurgeDisplayState Method (IModelDocExtension)

Purges identical display states so that only unique display states remain.

## Syntax

### Visual Basic (Declaration)

```vb
Function PurgeDisplayState() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Boolean

value = instance.PurgeDisplayState()
```

### C#

```csharp
System.bool PurgeDisplayState()
```

### C++/CLI

```cpp
System.bool PurgeDisplayState();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if identical display states are purged, false if not

## VBA Syntax

See [ModelDocExtension::PurgeDisplayState](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~PurgeDisplayState.html).

## Examples

[Create, Unlink, and Purge Display States in Parts (VB.NET)](Create,_Unlink,_and_Purge_Display_States_in_Part_Example_VBNET.htm)
[Create, Unlink, and Purge Display States in Part (VBA)](Create,_Unlink,_and_Purge_Display_States_in_Part_Example_VB.htm)
[Create, Unlink, and Purge Display States in Parts (C#)](Create,_Unlink,_and_Purge_Display_States_in_Part_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IConfiguration::ApplyDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ApplyDisplayState.html)
[IConfiguration::CopyDisplayStateFromConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CopyDisplayStateFromConfiguration.html)
[IConfiguration::CreateDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CreateDisplayState.html)
[IConfiguration::DeleteDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteDisplayState.html)
[IConfiguration::GetDisplayStates Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStates.html)
[IConfiguration::GetDisplayStatesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStatesCount.html)
[IModelDocExtension::LinkedDisplayState Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~LinkedDisplayState.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
