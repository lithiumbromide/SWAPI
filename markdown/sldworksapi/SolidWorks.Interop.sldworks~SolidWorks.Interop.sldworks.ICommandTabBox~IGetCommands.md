---
title: "IGetCommands Method (ICommandTabBox)"
project: "SOLIDWORKS API Help"
interface: "ICommandTabBox"
member: "IGetCommands"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~IGetCommands.html"
---

# IGetCommands Method (ICommandTabBox)

Gets the buttons' Command IDs, text display styles, and number of commands on the CommandManager tab box.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCommands( _
   ByRef CommandIDs As System.Integer, _
   ByRef TextDisplayStyles As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandTabBox
Dim CommandIDs As System.Integer
Dim TextDisplayStyles As System.Integer
Dim value As System.Integer

value = instance.IGetCommands(CommandIDs, TextDisplayStyles)
```

### C#

```csharp
System.int IGetCommands(
   out System.int CommandIDs,
   out System.int TextDisplayStyles
)
```

### C++/CLI

```cpp
System.int IGetCommands(
   [Out] System.int CommandIDs,
   [Out] System.int TextDisplayStyles
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CommandIDs`: - in-process, unmanaged C++: Pointer to an array of command IDs (see **Remarks**)
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `TextDisplayStyles`: - in-process, unmanaged C++: Pointer to an array the text display styles for the buttons as defined in [swCommandTabButtonTextDisplay_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCommandTabButtonTextDisplay_e.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method

### Return Value

Number of buttons on this CommandManager tab box

## VBA Syntax

See [CommandTabBox::IGetCommands](ms-its:sldworksapivb6.chm::/sldworks~CommandTabBox~IGetCommands.html).

## See Also

[ICommandTabBox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox.html)
[ICommandTabBox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox_members.html)
[ICommandTabBox::GetCommands Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox~GetCommands.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
