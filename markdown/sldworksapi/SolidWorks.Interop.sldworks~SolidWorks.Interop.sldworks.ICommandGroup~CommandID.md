---
title: "CommandID Property (ICommandGroup)"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup"
member: "CommandID"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~CommandID.html"
---

# CommandID Property (ICommandGroup)

Gets the command ID for the specified item in the CommandGroup.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CommandID( _
   ByVal CommandIndex As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandGroup
Dim CommandIndex As System.Integer
Dim value As System.Integer

value = instance.CommandID(CommandIndex)
```

### C#

```csharp
System.int CommandID(
   System.int CommandIndex
) {get;}
```

### C++/CLI

```cpp
property System.int CommandID {
   System.int get(System.int CommandIndex);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CommandIndex`: Index of the item in the CommandGroup

### Property Value

Command ID of the specified item

## VBA Syntax

See [CommandGroup::CommandID](ms-its:sldworksapivb6.chm::/sldworks~CommandGroup~CommandID.html).

## Examples

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)

## Remarks

The value of CommandIndex is the value returned by [ICommandGroup::AddCommandItem2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~AddCommandItem2.html).

## See Also

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html)
[ISldWorks::GetCommandID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCommandID.html)
[ICommandGroup::NumberOfGroupItems Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~NumberOfGroupItems.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
