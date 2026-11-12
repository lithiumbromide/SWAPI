---
title: "IRemoveCommands Method (ICommandTabBox)"
project: "SOLIDWORKS API Help"
interface: "ICommandTabBox"
member: "IRemoveCommands"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~IRemoveCommands.html"
---

# IRemoveCommands Method (ICommandTabBox)

Removes the specified buttons from this CommandManager tab box.

## Syntax

### Visual Basic (Declaration)

```vb
Function IRemoveCommands( _
   ByVal CommandIDCount As System.Integer, _
   ByRef CommandIDs As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandTabBox
Dim CommandIDCount As System.Integer
Dim CommandIDs As System.Integer
Dim value As System.Boolean

value = instance.IRemoveCommands(CommandIDCount, CommandIDs)
```

### C#

```csharp
System.bool IRemoveCommands(
   System.int CommandIDCount,
   ref System.int CommandIDs
)
```

### C++/CLI

```cpp
System.bool IRemoveCommands(
   System.int CommandIDCount,
   System.int% CommandIDs
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CommandIDCount`: Number of buttons to remove from this CommandManager tab box
- `CommandIDs`: - in-process, unmanaged C++: Pointer to an array of the command IDs for the buttons you want removed from this CommandManager tab box (see **Remarks**)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

True if the specified buttons are removed, false if not

## Remarks

You can get the CommandID values using [ICommandGroup::CommandID](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~CommandID.html) or [ICommandGroup::ToolbarId](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~ToolbarId.html) after calling [ICommandGroup::Activate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~Activate.html).

## See Also

[ICommandTabBox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox.html)
[ICommandTabBox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox_members.html)
[ICommandTabBox::RemoveCommands Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~RemoveCommands.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
