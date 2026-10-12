---
title: "HasMenu Property (ICommandGroup)"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup"
member: "HasMenu"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasMenu.html"
---

# HasMenu Property (ICommandGroup)

Gets or sets whether this CommandGroup has a menu.

## Syntax

### Visual Basic (Declaration)

```vb
Property HasMenu As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandGroup
Dim value As System.Boolean

instance.HasMenu = value

value = instance.HasMenu
```

### C#

```csharp
System.bool HasMenu {get; set;}
```

### C++/CLI

```cpp
property System.bool HasMenu {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if this CommandGroup has a menu, false if not (see **Remarks**)

## VBA Syntax

See [CommandGroup::HasMenu](ms-its:sldworksapivb6.chm::/sldworks~CommandGroup~HasMenu.html).

## Examples

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)
[Create Submenus in the CommandManager (C#)](Create_Submenus_in_the_CommandManager_Example_CSharp.htm)

## Remarks

By default, this CommandGroup has a menu.

## See Also

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html)
[ICommandGroup::HasMenu Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasMenu.html)
[ICommandManager::AddContextMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~AddContextMenu.html)
[ICommandGroup::MenuPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~MenuPosition.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
