---
title: "GetFlyoutGroup Method (ICommandManager)"
project: "SOLIDWORKS API Help"
interface: "ICommandManager"
member: "GetFlyoutGroup"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetFlyoutGroup.html"
---

# GetFlyoutGroup Method (ICommandManager)

Gets the flyout with the specified ID.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFlyoutGroup( _
   ByVal UserID As System.Integer _
) As FlyoutGroup
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandManager
Dim UserID As System.Integer
Dim value As FlyoutGroup

value = instance.GetFlyoutGroup(UserID)
```

### C#

```csharp
FlyoutGroup GetFlyoutGroup(
   System.int UserID
)
```

### C++/CLI

```cpp
FlyoutGroup^ GetFlyoutGroup(
   System.int UserID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserID`: User-defined ID for the flyout

### Return Value

[IFlyoutGroup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFlyoutGroup.html)

## VBA Syntax

See [CommandManager::GetFlyoutGroup](ms-its:sldworksapivb6.chm::/sldworks~CommandManager~GetFlyoutGroup.html).

## Examples

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)

## See Also

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html)
[ICommandManager::CreateFlyoutGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CreateFlyoutGroup.html)
[ICommandManager::GetFlyoutGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetFlyoutGroups.html)
[ICommandManager::RemoveFlyoutGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveFlyoutGroup.html)
[ICommandManager::NumberOfFlyoutGroups Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~NumberOfFlyoutGroups.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
