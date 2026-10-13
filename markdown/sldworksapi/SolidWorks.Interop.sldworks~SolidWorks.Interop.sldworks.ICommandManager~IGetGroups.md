---
title: "IGetGroups Method (ICommandManager)"
project: "SOLIDWORKS API Help"
interface: "ICommandManager"
member: "IGetGroups"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetGroups.html"
---

# IGetGroups Method (ICommandManager)

Gets the CommandGroups in the CommandManager.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetGroups( _
   ByVal Count As System.Integer _
) As System.IntPtr
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandManager
Dim Count As System.Integer
Dim value As System.IntPtr

value = instance.IGetGroups(Count)
```

### C#

```csharp
System.IntPtr IGetGroups(
   System.int Count
)
```

### C++/CLI

```cpp
System.IntPtr IGetGroups(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of CommandGroups in this CommandManager

### Return Value

- in-process, unmanaged C++: Pointer to an array of [ICommandGroup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup.html) objects in the CommandManager

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ICommandManager::NumberOfGroups](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~NumberOfGroups.html) to determine the size of the array.

## See Also

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html)
[ICommandManager::GetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetGroups.html)
[ICommandManager::GetCommandGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandGroup.html)
[ICommandManager::RemoveCommandGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveCommandGroup.html)
[ICommandManager::NumberOfGroups Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~NumberOfGroups.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
