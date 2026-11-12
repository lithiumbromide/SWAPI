---
title: "GetCommands Method (ICommandTabBox)"
project: "SOLIDWORKS API Help"
interface: "ICommandTabBox"
member: "GetCommands"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~GetCommands.html"
---

# GetCommands Method (ICommandTabBox)

Gets the buttons' command IDs, text display styles, and number of commands on the CommandManager tab box.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCommands( _
   ByRef CommandIDs As System.Object, _
   ByRef TextDisplayStyles As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandTabBox
Dim CommandIDs As System.Object
Dim TextDisplayStyles As System.Object
Dim value As System.Integer

value = instance.GetCommands(CommandIDs, TextDisplayStyles)
```

### C#

```csharp
System.int GetCommands(
   out System.object CommandIDs,
   out System.object TextDisplayStyles
)
```

### C++/CLI

```cpp
System.int GetCommands(
   [Out] System.Object^ CommandIDs,
   [Out] System.Object^ TextDisplayStyles
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CommandIDs`: Array of command IDs for the buttons
- `TextDisplayStyles`: Array of the text display styles for the buttons as defined in [swCommandTabButtonTextDisplay_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCommandTabButtonTextDisplay_e.html)

### Return Value

Number of buttons on this CommandManager tab box

## VBA Syntax

See [CommandTabBox::GetCommands](ms-its:sldworksapivb6.chm::/sldworks~CommandTabBox~GetCommands.html).

## Examples

[Create CommandManager Tab and Tab Boxes (C#)](Create_CommandManager_Tab_and_Tab_Boxes_Example_CSharp.htm)
[Create CommandManager Tab and Tab Boxes (VB.NET)](Create_CommandManager_Tab_and_Tab_Boxes_Example_VB.NET.htm)

## See Also

[ICommandTabBox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox.html)
[ICommandTabBox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox_members.html)
[ICommandTabBox::IGetCommands Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~IGetCommands.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
