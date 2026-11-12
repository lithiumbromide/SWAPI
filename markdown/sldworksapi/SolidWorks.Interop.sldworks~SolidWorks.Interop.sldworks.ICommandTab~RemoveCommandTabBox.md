---
title: "RemoveCommandTabBox Method (ICommandTab)"
project: "SOLIDWORKS API Help"
interface: "ICommandTab"
member: "RemoveCommandTabBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~RemoveCommandTabBox.html"
---

# RemoveCommandTabBox Method (ICommandTab)

Removes the specified tab box and its buttons from this CommandManager tab.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveCommandTabBox( _
   ByVal CommandTabBox As CommandTabBox _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandTab
Dim CommandTabBox As CommandTabBox

instance.RemoveCommandTabBox(CommandTabBox)
```

### C#

```csharp
void RemoveCommandTabBox(
   CommandTabBox CommandTabBox
)
```

### C++/CLI

```cpp
void RemoveCommandTabBox(
   CommandTabBox^ CommandTabBox
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CommandTabBox`: [CommandManager tab box](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandTabBox.html) and its buttons to remove

## VBA Syntax

See [CommandTab::RemoveCommandTabBox](ms-its:sldworksapivb6.chm::/sldworks~CommandTab~RemoveCommandTabBox.html).

## See Also

[ICommandTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab.html)
[ICommandTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab_members.html)
[ICommandTab::AddCommandTabBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~AddCommandTabBox.html)
[ICommandTab::CommandTabBoxes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~CommandTabBoxes.html)
[ICommandTab::GetCommandTabBoxCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~GetCommandTabBoxCount.html)
[ICommandTab::IGetCommandTabBoxes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~IGetCommandTabBoxes.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
