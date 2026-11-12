---
title: "AddSeparator Method (ICommandTab)"
project: "SOLIDWORKS API Help"
interface: "ICommandTab"
member: "AddSeparator"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab~AddSeparator.html"
---

# AddSeparator Method (ICommandTab)

Adds a separator to this CommandManager tab.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddSeparator( _
   ByVal CommandTabBoxIn As CommandTabBox, _
   ByVal CommandID As System.Integer _
) As CommandTabBox
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandTab
Dim CommandTabBoxIn As CommandTabBox
Dim CommandID As System.Integer
Dim value As CommandTabBox

value = instance.AddSeparator(CommandTabBoxIn, CommandID)
```

### C#

```csharp
CommandTabBox AddSeparator(
   CommandTabBox CommandTabBoxIn,
   System.int CommandID
)
```

### C++/CLI

```cpp
CommandTabBox^ AddSeparator(
   CommandTabBox^ CommandTabBoxIn,
   System.int CommandID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CommandTabBoxIn`: [CommandManager tab box](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandTabBox.html) to which to add the separator
- `CommandID`: Button before which to place the separator (see Remarks)

### Return Value

New [CommandManager tab box](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandTabBox.html)

## VBA Syntax

See [CommandTab::AddSeparator](ms-its:sldworksapivb6.chm::/sldworks~CommandTab~AddSeparator.html).

## Examples

[Create CommandManager Tab and Tab Boxes (VB.NET)](Create_CommandManager_Tab_and_Tab_Boxes_Example_VB.NET.htm)

## Remarks

The specified CommandManager tab is split into two. The left side is the original CommandManager tab box, and the right side is the new CommandManager tab box. The first button on the new CommandManager tab box is the button specified by CommandID.

If the CommandManager tab box has multiple commands with the same CommandID, then a separator is added before the first matching CommandID.

You can get the CommandID using [ICommandGroup::CommandID](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~CommandID.html) or [ICommandGroup::ToolbarId](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~ToolbarId.html) after calling [ICommandGroup::Activate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~Activate.html).

## See Also

[ICommandTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab.html)
[ICommandTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
