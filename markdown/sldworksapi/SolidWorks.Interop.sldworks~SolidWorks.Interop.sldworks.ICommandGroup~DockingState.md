---
title: "DockingState Property (ICommandGroup)"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup"
member: "DockingState"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~DockingState.html"
---

# DockingState Property (ICommandGroup)

Gets or sets the docking state of the toolbar in the CommandGroup.

## Syntax

### Visual Basic (Declaration)

```vb
Property DockingState As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandGroup
Dim value As System.Integer

instance.DockingState = value

value = instance.DockingState
```

### C#

```csharp
System.int DockingState {get; set;}
```

### C++/CLI

```cpp
property System.int DockingState {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Docking state of the toolbar as defined in [swToolbarDockStatePosition_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swToolbarDockStatePosition_e.html)

## VBA Syntax

See [CommandGroup::DockingState](ms-its:sldworksapivb6.chm::/sldworks~CommandGroup~DockingState.html).

## See Also

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html)
[ICommandGroup::SetToolbarVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SetToolbarVisibility.html)
[ICommandGroup::HasToolbar Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasToolbar.html)
[ICommandGroup::ToolbarId Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~ToolbarId.html)

## Availability

SOLIDWORKS 2006 SP5, Revision Number 14
