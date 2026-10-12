---
title: "AddSpacer2 Method (ICommandGroup)"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup"
member: "AddSpacer2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddSpacer2.html"
---

# AddSpacer2 Method (ICommandGroup)

Adds a spacer between items in a CommandGroup.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddSpacer2( _
   ByVal Position As System.Integer, _
   ByVal MenuTBOption As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandGroup
Dim Position As System.Integer
Dim MenuTBOption As System.Integer
Dim value As System.Integer

value = instance.AddSpacer2(Position, MenuTBOption)
```

### C#

```csharp
System.int AddSpacer2(
   System.int Position,
   System.int MenuTBOption
)
```

### C++/CLI

```cpp
System.int AddSpacer2(
   System.int Position,
   System.int MenuTBOption
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Position`: Position of the spacer within the CommandGroup

  NOTE: Specify 0 to add this a spacer to the beginning of the CommandGroup, or specify -1 to add it to the end of the CommandGroup. This argument specifies the position of the spacer in relation to its immediate parent item.
- `MenuTBOption`: Command item type as defined in [swCommandItemType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCommandItemType_e.html)

### Return Value

Index of the item within the CommandGroup as assigned by SOLIDWORKS

## VBA Syntax

See [CommandGroup::AddSpacer2](ms-its:sldworksapivb6.chm::/sldworks~CommandGroup~AddSpacer2.html).

## See Also

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
