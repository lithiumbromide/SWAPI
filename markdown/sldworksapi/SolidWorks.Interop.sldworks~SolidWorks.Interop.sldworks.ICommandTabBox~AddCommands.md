---
title: "AddCommands Method (ICommandTabBox)"
project: "SOLIDWORKS API Help"
interface: "ICommandTabBox"
member: "AddCommands"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~AddCommands.html"
---

# AddCommands Method (ICommandTabBox)

Adds buttons to this CommandManager tab box.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCommands( _
   ByVal CommandIDs As System.Object, _
   ByVal TextDisplayStyles As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandTabBox
Dim CommandIDs As System.Object
Dim TextDisplayStyles As System.Object
Dim value As System.Boolean

value = instance.AddCommands(CommandIDs, TextDisplayStyles)
```

### C#

```csharp
System.bool AddCommands(
   System.object CommandIDs,
   System.object TextDisplayStyles
)
```

### C++/CLI

```cpp
System.bool AddCommands(
   System.Object^ CommandIDs,
   System.Object^ TextDisplayStyles
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CommandIDs`: Array of command IDs for the buttons (see **Remarks**)
- `TextDisplayStyles`: Array of the text display styles for the buttons as defined in [swCommandTabButtonTextDisplay_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCommandTabButtonTextDisplay_e.html)

### Return Value

True if the buttons are added to the CommandManager tab box, false if not

## VBA Syntax

See [CommandTabBox::AddCommands](ms-its:sldworksapivb6.chm::/sldworks~CommandTabBox~AddCommands.html).

## Examples

[Create CommandManager Tab and Tab Boxes (VB.NET)](Create_CommandManager_Tab_and_Tab_Boxes_Example_VB.NET.htm)
[Create CommandManager Tab and Tab Boxes (C#)](Create_CommandManager_Tab_and_Tab_Boxes_Example_CSharp.htm)

## Remarks

You can add both CommandGroup and FlyoutGroup items to CommandManager. Populate CommandIDs by calling [IFlyoutGroup::CmdID](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFlyoutGroup~CmdID.html) for FlyoutGroups and [ICommandGroup::CommandID](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~CommandID.html) or [ICommandGroup::ToolbarId](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~ToolbarId.html) after calling [ICommandGroup::Activate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~Activate.html) for CommandGroups.

## See Also

[ICommandTabBox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox.html)
[ICommandTabBox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox_members.html)
[ICommandTabBox::IAddCommands Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~IAddCommands.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
