---
title: "CopyDisplayStateFromConfiguration Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "CopyDisplayStateFromConfiguration"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CopyDisplayStateFromConfiguration.html"
---

# CopyDisplayStateFromConfiguration Method (IConfiguration)

Copies the specified display state from the specified configuration to this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function CopyDisplayStateFromConfiguration( _
   ByVal CopyFromConfig As Configuration, _
   ByVal DisplayStateNameToCopy As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim CopyFromConfig As Configuration
Dim DisplayStateNameToCopy As System.String
Dim value As System.Boolean

value = instance.CopyDisplayStateFromConfiguration(CopyFromConfig, DisplayStateNameToCopy)
```

### C#

```csharp
System.bool CopyDisplayStateFromConfiguration(
   Configuration CopyFromConfig,
   System.string DisplayStateNameToCopy
)
```

### C++/CLI

```cpp
System.bool CopyDisplayStateFromConfiguration(
   Configuration^ CopyFromConfig,
   System.String^ DisplayStateNameToCopy
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CopyFromConfig`: Pointer to the [configuration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration.html) from which to copy the display state
- `DisplayStateNameToCopy`: Name of the display state to copy

### Return Value

True if the specified display is copied to this configuration, false if not

## VBA Syntax

See [Configuration::CopyDisplayStateFromConfiguration](ms-its:sldworksapivb6.chm::/sldworks~Configuration~CopyDisplayStateFromConfiguration.html).

## Remarks

Use [IConfiguration::GetDisplayStates](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetDisplayStates.html) or [IConfiguration::IGetDisplayStates](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~IGetDisplayStates.html) to get the names of the display states from the configuration from which to copy the display state.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::ApplyDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ApplyDisplayState.html)
[IConfiguration::CreateDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CreateDisplayState.html)
[IConfiguration::DeleteDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteDisplayState.html)
[IConfiguration::GetDisplayStatesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStatesCount.html)
[IConfiguration::RenameDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~RenameDisplayState.html)
[IConfigurationManager::LinkDisplayStatesToConfigurations Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~LinkDisplayStatesToConfigurations.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
