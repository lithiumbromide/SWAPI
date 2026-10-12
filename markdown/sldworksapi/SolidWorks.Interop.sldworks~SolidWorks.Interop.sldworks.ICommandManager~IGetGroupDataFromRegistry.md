---
title: "IGetGroupDataFromRegistry Method (ICommandManager)"
project: "SOLIDWORKS API Help"
interface: "ICommandManager"
member: "IGetGroupDataFromRegistry"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetGroupDataFromRegistry.html"
---

# IGetGroupDataFromRegistry Method (ICommandManager)

Gets the command IDs of the given command group from the registry.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetGroupDataFromRegistry( _
   ByVal UserGroupId As System.Integer, _
   ByVal Count As System.Integer, _
   ByRef UserIDs As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandManager
Dim UserGroupId As System.Integer
Dim Count As System.Integer
Dim UserIDs As System.Integer
Dim value As System.Boolean

value = instance.IGetGroupDataFromRegistry(UserGroupId, Count, UserIDs)
```

### C#

```csharp
System.bool IGetGroupDataFromRegistry(
   System.int UserGroupId,
   System.int Count,
   out System.int UserIDs
)
```

### C++/CLI

```cpp
System.bool IGetGroupDataFromRegistry(
   System.int UserGroupId,
   System.int Count,
   [Out] System.int UserIDs
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserGroupId`: User-defined ID of a command group
- `Count`: Number of command IDs in the given command group
- `UserIDs`: - in-process, unmanaged C++: Pointer to an array of integer IDs

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

True if successful, false if not

## Remarks

Before calling this method call [ICommandManager::GetCommandIDsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~GetCommandIDsCount.html) to populate Count.

Use this method to compare command group IDs obtained through the user interface with those stored in the registry.

## See Also

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html)
[ICommandManager::GetGroupDataFromRegistry Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetGroupDataFromRegistry.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
