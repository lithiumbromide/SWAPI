---
title: "RemoveCommandGroup2 Method (ICommandManager)"
project: "SOLIDWORKS API Help"
interface: "ICommandManager"
member: "RemoveCommandGroup2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveCommandGroup2.html"
---

# RemoveCommandGroup2 Method (ICommandManager)

Removes the specified CommandGroup from the CommandManager.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveCommandGroup2( _
   ByVal UserID As System.Integer, _
   ByVal RuntimeOnly As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandManager
Dim UserID As System.Integer
Dim RuntimeOnly As System.Boolean
Dim value As System.Integer

value = instance.RemoveCommandGroup2(UserID, RuntimeOnly)
```

### C#

```csharp
System.int RemoveCommandGroup2(
   System.int UserID,
   System.bool RuntimeOnly
)
```

### C++/CLI

```cpp
System.int RemoveCommandGroup2(
   System.int UserID,
   System.bool RuntimeOnly
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserID`: User-defined ID of the CommandGroup to remove
- `RuntimeOnly`: True to remove the CommandGroup , saving its toolbar information in the registry; false to remove both the CommandGroup and its toolbar information in the registry

### Return Value

Error code as defined in [swRemoveCommandGroupErrors](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRemoveCommandGroupErrors.html)

## VBA Syntax

See [CommandManager::RemoveCommandGroup2](ms-its:sldworksapivb6.chm::/sldworks~CommandManager~RemoveCommandGroup2.html).

## Remarks

This method removes CommandGroups created using [ICommandManager::AddContextMenu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~AddContextMenu.html) and [ICommandManager::CreateCommandGroup2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~CreateCommandGroup2.html).

## See Also

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
