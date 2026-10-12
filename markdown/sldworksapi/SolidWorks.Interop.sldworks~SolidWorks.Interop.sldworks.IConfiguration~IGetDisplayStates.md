---
title: "IGetDisplayStates Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "IGetDisplayStates"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetDisplayStates.html"
---

# IGetDisplayStates Method (IConfiguration)

Gets the names of the display states for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDisplayStates( _
   ByVal Count As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim Count As System.Integer
Dim value As System.String

value = instance.IGetDisplayStates(Count)
```

### C#

```csharp
System.string IGetDisplayStates(
   System.int Count
)
```

### C++/CLI

```cpp
System.String^ IGetDisplayStates(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of displays states for this configuration

### Return Value

- in-process, unmanaged C++: Pointer to an array of names of the display states for this configuration

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IConfiguration::GetDisplayStatesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetDisplayStatesCount.html) to determine the size of array for the output.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::ApplyDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ApplyDisplayState.html)
[IConfiguration::CopyDisplayStateFromConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CopyDisplayStateFromConfiguration.html)
[IConfiguration::CreateDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CreateDisplayState.html)
[IConfiguration::DeleteDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteDisplayState.html)
[IConfiguration::GetDisplayStates Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStates.html)
[IConfiguration::RenameDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~RenameDisplayState.html)
[IConfigurationManager::LinkDisplayStatesToConfigurations Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~LinkDisplayStatesToConfigurations.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
