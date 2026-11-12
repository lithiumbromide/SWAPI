---
title: "NumberOfGroups Property (ICommandManager)"
project: "SOLIDWORKS API Help"
interface: "ICommandManager"
member: "NumberOfGroups"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~NumberOfGroups.html"
---

# NumberOfGroups Property (ICommandManager)

Gets the number of CommandGroups.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property NumberOfGroups As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandManager
Dim value As System.Integer

value = instance.NumberOfGroups
```

### C#

```csharp
System.int NumberOfGroups {get;}
```

### C++/CLI

```cpp
property System.int NumberOfGroups {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of CommandGroups

## VBA Syntax

See [CommandManager::NumberOfGroups](ms-its:sldworksapivb6.chm::/sldworks~CommandManager~NumberOfGroups.html).

## Remarks

Call this method before calling [ICommandManager::IGetGroups](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~IGetGroups.html) to determine the size of the array for that method.

## See Also

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html)
[ICommandManager::GetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetGroups.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
