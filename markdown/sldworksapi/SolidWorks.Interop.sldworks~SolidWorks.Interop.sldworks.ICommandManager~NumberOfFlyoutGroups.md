---
title: "NumberOfFlyoutGroups Property (ICommandManager)"
project: "SOLIDWORKS API Help"
interface: "ICommandManager"
member: "NumberOfFlyoutGroups"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~NumberOfFlyoutGroups.html"
---

# NumberOfFlyoutGroups Property (ICommandManager)

Gets the number of flyouts in the CommandManager.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property NumberOfFlyoutGroups As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandManager
Dim value As System.Integer

value = instance.NumberOfFlyoutGroups
```

### C#

```csharp
System.int NumberOfFlyoutGroups {get;}
```

### C++/CLI

```cpp
property System.int NumberOfFlyoutGroups {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of flyouts

## VBA Syntax

See [CommandManager::NumberOfFlyoutGroups](ms-its:sldworksapivb6.chm::/sldworks~CommandManager~NumberOfFlyoutGroups.html).

## Examples

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)

## See Also

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html)
[ICommandManager::CreateFlyoutGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CreateFlyoutGroup.html)
[ICommandManager::GetFlyoutGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetFlyoutGroup.html)
[ICommandManager::GetFlyoutGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetFlyoutGroups.html)
[ICommandManager::RemoveFlyoutGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveFlyoutGroup.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
