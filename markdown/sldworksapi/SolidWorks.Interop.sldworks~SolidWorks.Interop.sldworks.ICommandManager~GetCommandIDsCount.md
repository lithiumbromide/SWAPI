---
title: "GetCommandIDsCount Method (ICommandManager)"
project: "SOLIDWORKS API Help"
interface: "ICommandManager"
member: "GetCommandIDsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandIDsCount.html"
---

# GetCommandIDsCount Method (ICommandManager)

Gets the number of command IDs for the given command group.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCommandIDsCount( _
   ByVal UserGroupId As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandManager
Dim UserGroupId As System.Integer
Dim value As System.Integer

value = instance.GetCommandIDsCount(UserGroupId)
```

### C#

```csharp
System.int GetCommandIDsCount(
   System.int UserGroupId
)
```

### C++/CLI

```cpp
System.int GetCommandIDsCount(
   System.int UserGroupId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserGroupId`: User-defined ID of a command group

### Return Value

Number of command IDs in the given command group

## VBA Syntax

See [CommandManager::GetCommandIDsCount](ms-its:sldworksapivb6.chm::/sldworks~CommandManager~GetCommandIDsCount.html).

## Remarks

Call this method before calling [ICommandManager::IGetGroupDataFromRegistry](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~IGetGroupDataFromRegistry.html) to determine the size of the array for that method.

## See Also

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
