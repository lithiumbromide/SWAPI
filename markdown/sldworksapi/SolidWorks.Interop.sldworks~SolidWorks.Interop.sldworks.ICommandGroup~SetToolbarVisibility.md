---
title: "SetToolbarVisibility Method (ICommandGroup)"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup"
member: "SetToolbarVisibility"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SetToolbarVisibility.html"
---

# SetToolbarVisibility Method (ICommandGroup)

Sets the visibility of the toolbar in the CommandGroup.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetToolbarVisibility( _
   ByVal Visible As System.Boolean, _
   ByVal Mask As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandGroup
Dim Visible As System.Boolean
Dim Mask As System.Integer

instance.SetToolbarVisibility(Visible, Mask)
```

### C#

```csharp
void SetToolbarVisibility(
   System.bool Visible,
   System.int Mask
)
```

### C++/CLI

```cpp
void SetToolbarVisibility(
   System.bool Visible,
   System.int Mask
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Visible`: True to show the toolbar, false to hide it
- `Mask`: Context in which to show or hide toolbar as defined in [swDocTemplateTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocTemplateTypes_e.html)

## VBA Syntax

See [CommandGroup::SetToolbarVisibility](ms-its:sldworksapivb6.chm::/sldworks~CommandGroup~SetToolbarVisibility.html).

## See Also

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html)
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html)
[ICommandGroup::HasMenu Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasMenu.html)
[ICommandGroup::HasToolbar Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~HasToolbar.html)
[ICommandManager::AddContextMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~AddContextMenu.html)

## Availability

SOLIDWORKS 2006 SP4, Revision Number 14
