---
title: "GetGroups Method (ICommandManager)"
project: "SOLIDWORKS API Help"
interface: "ICommandManager"
member: "GetGroups"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetGroups.html"
---

# GetGroups Method (ICommandManager)

Gets the CommandGroups in the CommandManager.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGroups() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandManager
Dim value As System.Object

value = instance.GetGroups()
```

### C#

```csharp
System.object GetGroups()
```

### C++/CLI

```cpp
System.Object^ GetGroups();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of the [ICommandGroup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup.html)s in the CommandManager

## VBA Syntax

See [CommandManager::GetGroups](ms-its:sldworksapivb6.chm::/sldworks~CommandManager~GetGroups.html).

## See Also

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html)
[ICommandManager::IGetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetGroups.html)
[ICommandManager::GetCommandGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandGroup.html)
[ICommandManager::RemoveCommandGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveCommandGroup.html)
[ICommandManager::NumberOfGroups Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~NumberOfGroups.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
