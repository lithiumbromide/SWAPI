---
title: "RemoveCommands Method (ICommandTabBox)"
project: "SOLIDWORKS API Help"
interface: "ICommandTabBox"
member: "RemoveCommands"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~RemoveCommands.html"
---

# RemoveCommands Method (ICommandTabBox)

Removes the specified buttons from this CommandManager tab box.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveCommands( _
   ByVal CommandIDs As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandTabBox
Dim CommandIDs As System.Object
Dim value As System.Boolean

value = instance.RemoveCommands(CommandIDs)
```

### C#

```csharp
System.bool RemoveCommands(
   System.object CommandIDs
)
```

### C++/CLI

```cpp
System.bool RemoveCommands(
   System.Object^ CommandIDs
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CommandIDs`: Array of command IDs for the buttons you want removed from this CommandManager tab box (see **Remarks**)

### Return Value

True if the specified buttons are removed, false if not

## VBA Syntax

See [CommandTabBox::RemoveCommands](ms-its:sldworksapivb6.chm::/sldworks~CommandTabBox~RemoveCommands.html).

## Remarks

You can get the CommandID values using [ICommandGroup::CommandID](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~CommandID.html) or [ICommandGroup::ToolbarId](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~ToolbarId.html) after calling [ICommandGroup::Activate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~Activate.html).

## See Also

[ICommandTabBox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox.html)
[ICommandTabBox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox_members.html)
[ICommandTabBox::IRemoveCommands Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~IRemoveCommands.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
