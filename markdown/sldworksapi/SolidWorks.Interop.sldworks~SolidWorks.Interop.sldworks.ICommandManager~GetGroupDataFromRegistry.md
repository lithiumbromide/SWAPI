---
title: "GetGroupDataFromRegistry Method (ICommandManager)"
project: "SOLIDWORKS API Help"
interface: "ICommandManager"
member: "GetGroupDataFromRegistry"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetGroupDataFromRegistry.html"
---

# GetGroupDataFromRegistry Method (ICommandManager)

Gets the command IDs of the given command group from the registry.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGroupDataFromRegistry( _
   ByVal UserGroupId As System.Integer, _
   ByRef UserIDs As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandManager
Dim UserGroupId As System.Integer
Dim UserIDs As System.Object
Dim value As System.Boolean

value = instance.GetGroupDataFromRegistry(UserGroupId, UserIDs)
```

### C#

```csharp
System.bool GetGroupDataFromRegistry(
   System.int UserGroupId,
   out System.object UserIDs
)
```

### C++/CLI

```cpp
System.bool GetGroupDataFromRegistry(
   System.int UserGroupId,
   [Out] System.Object^ UserIDs
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserGroupId`: User-defined ID of a command group
- `UserIDs`: Array of command IDs for the given command group

### Return Value

True if successful, false if not

## VBA Syntax

See [CommandManager::GetGroupDataFromRegistry](ms-its:sldworksapivb6.chm::/sldworks~CommandManager~GetGroupDataFromRegistry.html).

## Examples

[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)
[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)

## Remarks

Call this API before calling [ICommandManager::CreateCommandGroup2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~CreateCommandGroup2.html). The array of command IDs returned by this method helps you decide how to set the IgnorePreviousVersion parameter of ICommandManager::CreateCommandGroup2.

## See Also

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html)
[ICommandManger::IGetGroupDataFromRegistry](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetGroupDataFromRegistry.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
