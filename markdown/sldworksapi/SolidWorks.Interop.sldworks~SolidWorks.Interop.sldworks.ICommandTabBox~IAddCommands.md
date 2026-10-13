---
title: "IAddCommands Method (ICommandTabBox)"
project: "SOLIDWORKS API Help"
interface: "ICommandTabBox"
member: "IAddCommands"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~IAddCommands.html"
---

# IAddCommands Method (ICommandTabBox)

Adds buttons to this CommandManager tab box.

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddCommands( _
   ByVal CommandIDCount As System.Integer, _
   ByRef CommandIDs As System.Integer, _
   ByRef TextDisplayStyles As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandTabBox
Dim CommandIDCount As System.Integer
Dim CommandIDs As System.Integer
Dim TextDisplayStyles As System.Integer
Dim value As System.Boolean

value = instance.IAddCommands(CommandIDCount, CommandIDs, TextDisplayStyles)
```

### C#

```csharp
System.bool IAddCommands(
   System.int CommandIDCount,
   ref System.int CommandIDs,
   ref System.int TextDisplayStyles
)
```

### C++/CLI

```cpp
System.bool IAddCommands(
   System.int CommandIDCount,
   System.int% CommandIDs,
   System.int% TextDisplayStyles
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CommandIDCount`: Number of buttons to add
- `CommandIDs`: - in-process, unmanaged C++: Pointer to an array of command IDs (see **Remarks**)
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `TextDisplayStyles`: - in-process, unmanaged C++: Pointer to an array the text display styles for the buttons as defined in [swCommandTabButtonTextDisplay_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCommandTabButtonTextDisplay_e.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

True if the buttons are added to the CommandManager tab box, false if not

## Remarks

You can get the CommandID values using [ICommandGroup::CommandID](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~CommandID.html) or [ICommandGroup::ToolbarId](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~ToolbarId.html) after calling [ICommandGroup::Activate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~Activate.html).

## See Also

[ICommandTabBox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox.html)
[ICommandTabBox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox_members.html)
[ICommandTabBox::AddCommands Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~AddCommands.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
