---
title: "CommandTabBoxes Method (ICommandTab)"
project: "SOLIDWORKS API Help"
interface: "ICommandTab"
member: "CommandTabBoxes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~CommandTabBoxes.html"
---

# CommandTabBoxes Method (ICommandTab)

Gets the tab boxes on this CommandManager tab.

## Syntax

### Visual Basic (Declaration)

```vb
Function CommandTabBoxes() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandTab
Dim value As System.Object

value = instance.CommandTabBoxes()
```

### C#

```csharp
System.object CommandTabBoxes()
```

### C++/CLI

```cpp
System.Object^ CommandTabBoxes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [CommandManager tab boxes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandTabBox.html) on this CommandManager tab

## VBA Syntax

See [CommandTab::CommandTabBoxes](ms-its:sldworksapivb6.chm::/sldworks~CommandTab~CommandTabBoxes.html).

## See Also

[ICommandTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab.html)
[ICommandTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab_members.html)
[ICommandTab::GetCommandTabBoxCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~GetCommandTabBoxCount.html)
[ICommandTab::IGetCommandTabBoxes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~IGetCommandTabBoxes.html)
[ICommandTab::RemoveCommandTabBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~RemoveCommandTabBox.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
