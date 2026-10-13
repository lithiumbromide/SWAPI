---
title: "HasEnabledButton Property (ICommandGroup)"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup"
member: "HasEnabledButton"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasEnabledButton.html"
---

# HasEnabledButton Property (ICommandGroup)

Gets whether any buttons in this CommandGroup are enabled.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property HasEnabledButton As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandGroup
Dim value As System.Boolean

value = instance.HasEnabledButton
```

### C#

```csharp
System.bool HasEnabledButton {get;}
```

### C++/CLI

```cpp
property System.bool HasEnabledButton {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if at least one CommandGroup button is enabled, false if not

## VBA Syntax

See [CommandGroup::HasEnabledButton](ms-its:sldworksapivb6.chm::/sldworks~CommandGroup~HasEnabledButton.html).

## Examples

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)

## Remarks

Add-in applications can call this method to determine whether to disable flyout buttons in the CommandManager.

## See Also

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html)
[ICommandGroup::AddCommandItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~AddCommandItem2.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20
