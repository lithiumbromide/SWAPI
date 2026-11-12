---
title: "GetDisplayStatesCount Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetDisplayStatesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStatesCount.html"
---

# GetDisplayStatesCount Method (IConfiguration)

Gets the number of display states for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayStatesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Integer

value = instance.GetDisplayStatesCount()
```

### C#

```csharp
System.int GetDisplayStatesCount()
```

### C++/CLI

```cpp
System.int GetDisplayStatesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of display states for this configuration

## VBA Syntax

See [Configuration::GetDisplayStatesCount](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetDisplayStatesCount.html).

## Examples

[Add and Delete Appearances from Specific Display States (C#)](Add_and_Delete_Materials_from_Specific_Display_States_Example_CSharp.htm)
[Add and Delete Appearances from Specific Display States (VB.NET)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VBNET.htm)
[Add and Delete Appearances from Specific Display States (VBA)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VB.htm)

## Remarks

Call this method before calling [IConfiguration::IGetDisplayStates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetDisplayStates.html) to determine the size of the array needed.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::ApplyDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ApplyDisplayState.html)
[IConfiguration::CopyDisplayStateFromConfiguration Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CopyDisplayStateFromConfiguration.html)
[IConfiguration::GetDisplayStates Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStates.html)
[IConfiguration::IGetDisplayStates Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetDisplayStates.html)
[IConfiguration::DeleteDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DeleteDisplayState.html)
[IConfiguration::RenameDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~RenameDisplayState.html)
[IConfiguration::GetDisplayStateBodyProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateBodyProperties.html)
[IConfiguration::GetDisplayStateComponentProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateComponentProperties.html)
[IConfiguration::GetDisplayStateComponentVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateComponentVisibility.html)
[IConfiguration::GetDisplayStateFaceProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateFaceProperties.html)
[IConfiguration::GetDisplayStateFeatureProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateFeatureProperties.html)
[IConfiguration::GetDisplayStateProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStateProperties.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
