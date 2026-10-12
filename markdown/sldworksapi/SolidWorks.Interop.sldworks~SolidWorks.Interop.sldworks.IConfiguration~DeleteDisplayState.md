---
title: "DeleteDisplayState Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "DeleteDisplayState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteDisplayState.html"
---

# DeleteDisplayState Method (IConfiguration)

Deletes the specified display state from this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteDisplayState( _
   ByVal DisplayStateName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim DisplayStateName As System.String
Dim value As System.Boolean

value = instance.DeleteDisplayState(DisplayStateName)
```

### C#

```csharp
System.bool DeleteDisplayState(
   System.string DisplayStateName
)
```

### C++/CLI

```cpp
System.bool DeleteDisplayState(
   System.String^ DisplayStateName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DisplayStateName`: Name of display state to delete from this configuration

### Return Value

True if the specified display state is deleted, false if not

## VBA Syntax

See [Configuration::DeleteDisplayState](ms-its:sldworksapivb6.chm::/sldworks~Configuration~DeleteDisplayState.html).

## Remarks

Use [IConfiguration::GetDisplayStates](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetDisplayStates.html) or [IConfiguration::IGetDisplayStates](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~IGetDisplayStates.html) to get the names of the display states from the configuration from which to copy the display state.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::ApplyDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ApplyDisplayState.html)
[IConfiguration::CopyDisplayStateFromConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CopyDisplayStateFromConfiguration.html)
[IConfiguration::GetDisplayStatesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStatesCount.html)
[IConfiguration::RenameDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~RenameDisplayState.html)
[IModelDocExtension::DeleteDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDisplayStateSpecificRenderMaterial.html)
[IModelDocExtension::IDeleteDisplayStateSpecificRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IDeleteDisplayStateSpecificRenderMaterial.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
