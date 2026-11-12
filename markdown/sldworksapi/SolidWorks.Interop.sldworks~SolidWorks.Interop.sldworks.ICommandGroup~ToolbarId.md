---
title: "ToolbarId Property (ICommandGroup)"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup"
member: "ToolbarId"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~ToolbarId.html"
---

# ToolbarId Property (ICommandGroup)

Gets the toolbar ID of this CommandGroup.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ToolbarId As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandGroup
Dim value As System.Integer

value = instance.ToolbarId
```

### C#

```csharp
System.int ToolbarId {get;}
```

### C++/CLI

```cpp
property System.int ToolbarId {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Toolbar ID of this CommandGroup

## VBA Syntax

See [CommandGroup::ToolbarId](ms-its:sldworksapivb6.chm::/sldworks~CommandGroup~ToolbarId.html).

## Examples

[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)
[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)

## Remarks

Use this property when [dragging a toolbar button](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~DragToolbarButton.html) from one toolbar (native SOLIDWORKS or a CommandGroup toolbar) to another toolbar (native SOLIDWORKS or a CommandGroup toolbar).

## See Also

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html)
[ICommandManager::HasToolbar Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasToolbar.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
