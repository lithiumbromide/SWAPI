---
title: "AddCommandTabBox Method (ICommandTab)"
project: "SOLIDWORKS API Help"
interface: "ICommandTab"
member: "AddCommandTabBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~AddCommandTabBox.html"
---

# AddCommandTabBox Method (ICommandTab)

Adds a tab box to this CommandManager tab.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCommandTabBox() As CommandTabBox
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandTab
Dim value As CommandTabBox

value = instance.AddCommandTabBox()
```

### C#

```csharp
CommandTabBox AddCommandTabBox()
```

### C++/CLI

```cpp
CommandTabBox^ AddCommandTabBox();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[CommandManager tab box](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandTabBox.html)

## VBA Syntax

See [CommandTab::AddCommandTabBox](ms-its:sldworksapivb6.chm::/sldworks~CommandTab~AddCommandTabBox.html).

## Examples

[Create CommandManager Tab and Tab Boxes (VB.NET)](Create_CommandManager_Tab_and_Tab_Boxes_Example_VB.NET.htm)

## Remarks

The CommandManager tab box is always added to the end of the CommandManager tab, unless it is the first CommandManager tab box added to this CommandManager tab. If so, then this CommandManager tab box is placed at the beginning of the CommandManager tab.

The CommandManager tab box is not immediately visible. You must first [add buttons](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandTabBox~AddCommands.html) to the CommandManager tab box.

## See Also

[ICommandTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab.html)
[ICommandTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
