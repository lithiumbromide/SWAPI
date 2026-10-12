---
title: "RenameDisplayState Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "RenameDisplayState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~RenameDisplayState.html"
---

# RenameDisplayState Method (IConfiguration)

Renames a display state of this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function RenameDisplayState( _
   ByVal OldDisplayStateName As System.String, _
   ByVal NewDisplayStateName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim OldDisplayStateName As System.String
Dim NewDisplayStateName As System.String
Dim value As System.Boolean

value = instance.RenameDisplayState(OldDisplayStateName, NewDisplayStateName)
```

### C#

```csharp
System.bool RenameDisplayState(
   System.string OldDisplayStateName,
   System.string NewDisplayStateName
)
```

### C++/CLI

```cpp
System.bool RenameDisplayState(
   System.String^ OldDisplayStateName,
   System.String^ NewDisplayStateName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OldDisplayStateName`: Existing name of the display state
- `NewDisplayStateName`: New name for the display state

### Return Value

True if the display state is renamed, false if not

## VBA Syntax

See [Configuration::RenameDisplayState](ms-its:sldworksapivb6.chm::/sldworks~Configuration~RenameDisplayState.html).

## Remarks

Use [IConfiguration::GetDisplayStates](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetDisplayStates.html) or [IConfiguration::IGetDisplayStates](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~IGetDisplayStates.html) to get a list of the names of the existing display states for this configuration.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::ApplyDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ApplyDisplayState.html)
[IConfiguration::DeleteDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteDisplayState.html)
[IConfiguration::CreateDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CreateDisplayState.html)
[IConfiguration::CopyDisplayStateFromConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CopyDisplayStateFromConfiguration.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
