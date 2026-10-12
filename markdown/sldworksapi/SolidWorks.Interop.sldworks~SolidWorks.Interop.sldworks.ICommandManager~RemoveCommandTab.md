---
title: "RemoveCommandTab Method (ICommandManager)"
project: "SOLIDWORKS API Help"
interface: "ICommandManager"
member: "RemoveCommandTab"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveCommandTab.html"
---

# RemoveCommandTab Method (ICommandManager)

Removes the specified CommandManager tab, including its tab boxes and buttons, from the CommandManager.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveCommandTab( _
   ByVal TabToRemove As CommandTab _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandManager
Dim TabToRemove As CommandTab
Dim value As System.Boolean

value = instance.RemoveCommandTab(TabToRemove)
```

### C#

```csharp
System.bool RemoveCommandTab(
   CommandTab TabToRemove
)
```

### C++/CLI

```cpp
System.bool RemoveCommandTab(
   CommandTab^ TabToRemove
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TabToRemove`: [CommandManager tab](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandTab.html), including its tab boxes and buttons, to remove

### Return Value

True if the CommandManager tab is removed, false if not

## VBA Syntax

See [CommandManager::RemoveCommandTab](ms-its:sldworksapivb6.chm::/sldworks~CommandManager~RemoveCommandTab.html).

## See Also

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html)
[ICommandManager::AddCommandTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~AddCommandTab.html)
[ICommandManager::CommandTabs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CommandTabs.html)
[ICommandManager::GetCommandTab Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandTab.html)
[ICommandManager::GetCommandTabCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandTabCount.html)
[ICommandManager::IGetCommandTabs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetCommandTabs.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
