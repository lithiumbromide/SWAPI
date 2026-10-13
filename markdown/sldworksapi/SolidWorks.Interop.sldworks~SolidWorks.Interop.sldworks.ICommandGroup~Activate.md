---
title: "Activate Method (ICommandGroup)"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup"
member: "Activate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~Activate.html"
---

# Activate Method (ICommandGroup)

Activates the CommandGroup.

## Syntax

### Visual Basic (Declaration)

```vb
Function Activate() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandGroup
Dim value As System.Boolean

value = instance.Activate()
```

### C#

```csharp
System.bool Activate()
```

### C++/CLI

```cpp
System.bool Activate();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the CommandGroup is activated, false if not

## VBA Syntax

See [CommandGroup::Activate](ms-its:sldworksapivb6.chm::/sldworks~CommandGroup~Activate.html).

## Examples

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)
[Create Submenus in the CommandManager (C#)](Create_Submenus_in_the_CommandManager_Example_CSharp.htm)

## Remarks

After completely creating a CommandGroup, use this method to activate it. You only need to activate the top-level group; you do not need to activate child groups.

## See Also

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html)
[ICommandGroup::MenuPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~MenuPosition.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
