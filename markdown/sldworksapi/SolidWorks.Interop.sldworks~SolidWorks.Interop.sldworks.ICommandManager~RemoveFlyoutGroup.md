---
title: "RemoveFlyoutGroup Method (ICommandManager)"
project: "SOLIDWORKS API Help"
interface: "ICommandManager"
member: "RemoveFlyoutGroup"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveFlyoutGroup.html"
---

# RemoveFlyoutGroup Method (ICommandManager)

Removes the specified flyout from the CommandManager.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveFlyoutGroup( _
   ByVal UserID As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandManager
Dim UserID As System.Integer
Dim value As System.Boolean

value = instance.RemoveFlyoutGroup(UserID)
```

### C#

```csharp
System.bool RemoveFlyoutGroup(
   System.int UserID
)
```

### C++/CLI

```cpp
System.bool RemoveFlyoutGroup(
   System.int UserID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserID`: User-defined ID of the flyout to remove

### Return Value

True if removal successful, false if not

## VBA Syntax

See [CommandManager::RemoveFlyoutGroup](ms-its:sldworksapivb6.chm::/sldworks~CommandManager~RemoveFlyoutGroup.html).

## Examples

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)

## See Also

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html)
[ICommandManager::CreateFlyoutGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CreateFlyoutGroup.html)
[ICommandManager::GetFlyoutGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetFlyoutGroup.html)
[ICommandManager::GetFlyoutGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetFlyoutGroups.html)
[ICommandManager::NumberOfFlyoutGroups Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~NumberOfFlyoutGroups.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
