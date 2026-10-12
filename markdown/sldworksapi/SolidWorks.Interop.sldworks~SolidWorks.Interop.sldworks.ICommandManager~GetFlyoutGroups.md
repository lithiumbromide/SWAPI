---
title: "GetFlyoutGroups Method (ICommandManager)"
project: "SOLIDWORKS API Help"
interface: "ICommandManager"
member: "GetFlyoutGroups"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetFlyoutGroups.html"
---

# GetFlyoutGroups Method (ICommandManager)

Gets the flyouts in the CommandManager.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFlyoutGroups() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandManager
Dim value As System.Object

value = instance.GetFlyoutGroups()
```

### C#

```csharp
System.object GetFlyoutGroups()
```

### C++/CLI

```cpp
System.Object^ GetFlyoutGroups();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of the [IFlyoutGroup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFlyoutGroup.html)s in the CommandManager

## VBA Syntax

See [CommandManager::GetFlyoutGroups](ms-its:sldworksapivb6.chm::/sldworks~CommandManager~GetFlyoutGroups.html).

## Examples

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)

## See Also

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html)
[ICommandManager::CreateFlyoutGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CreateFlyoutGroup.html)
[ICommandManager::GetFlyoutGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetFlyoutGroup.html)
[ICommandManager::RemoveFlyoutGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveFlyoutGroup.html)
[ICommandManager::NumberOfFlyoutGroups Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~NumberOfFlyoutGroups.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
