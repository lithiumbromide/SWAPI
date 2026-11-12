---
title: "HasToolbar Property (ICommandGroup)"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup"
member: "HasToolbar"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasToolbar.html"
---

# HasToolbar Property (ICommandGroup)

Gets or sets whether this CommandGroup has a toolbar.

## Syntax

### Visual Basic (Declaration)

```vb
Property HasToolbar As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandGroup
Dim value As System.Boolean

instance.HasToolbar = value

value = instance.HasToolbar
```

### C#

```csharp
System.bool HasToolbar {get; set;}
```

### C++/CLI

```cpp
property System.bool HasToolbar {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if this CommandGroup has a toolbar, false if not (see **Remarks**)

## VBA Syntax

See [CommandGroup::HasToolbar](ms-its:sldworksapivb6.chm::/sldworks~CommandGroup~HasToolbar.html).

## Examples

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)
[Create Submenus in the CommandManager (C#)](Create_Submenus_in_the_CommandManager_Example_CSharp.htm)

## Remarks

By default, this CommandGroup has a toolbar.

## See Also

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html)
[ICommandGroup::HasMenu Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasMenu.html)
[ICommandGroup::SetToolbarVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SetToolbarVisibility.html)
[ICommandGroup::DockingState Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~DockingState.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
