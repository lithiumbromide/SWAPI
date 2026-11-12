---
title: "DragToolbarButtonFromCommandID Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "DragToolbarButtonFromCommandID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DragToolbarButtonFromCommandID.html"
---

# DragToolbarButtonFromCommandID Method (ISldWorks)

Copies a button to a toolbar using a command ID.

## Syntax

### Visual Basic (Declaration)

```vb
Function DragToolbarButtonFromCommandID( _
   ByVal CommandID As System.Integer, _
   ByVal TargetToolbar As System.Integer, _
   ByVal TargetIndex As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim CommandID As System.Integer
Dim TargetToolbar As System.Integer
Dim TargetIndex As System.Integer
Dim value As System.Integer

value = instance.DragToolbarButtonFromCommandID(CommandID, TargetToolbar, TargetIndex)
```

### C#

```csharp
System.int DragToolbarButtonFromCommandID(
   System.int CommandID,
   System.int TargetToolbar,
   System.int TargetIndex
)
```

### C++/CLI

```cpp
System.int DragToolbarButtonFromCommandID(
   System.int CommandID,
   System.int TargetToolbar,
   System.int TargetIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CommandID`: Command ID as defined by [swCommands_e](ms-its:swcommands.chm::/SOLIDWORKS.Interop.swcommands~SOLIDWORKS.Interop.swcommands.swCommands_e.html)
- `TargetToolbar`: Toolbar as defined by [swToolbar_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swToolbar_e.html) or if a CommandGroup toolbar, use [ICommandGroup::ToolbarId](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~ToolbarId.html)
- `TargetIndex`: 0-based index of the toolbar button on the native SOLIDWORKS toolbar or CommandGroup toolbar

### Return Value

Index of the toolbar or -1 if the button is not added

## VBA Syntax

See [SldWorks::DragToolbarButtonFromCommandID](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~DragToolbarButtonFromCommandID.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::DragToolbarButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DragToolbarButton.html)
[ISldWorks::AddToolbar4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar4.html)
[ISldWorks::AddToolbarCommand2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbarCommand2.html)
[ISldWorks::GetLastToolbarID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLastToolbarID.html)
[ISldWorks::GetToolbarDock2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarDock2.html)
[ISldWorks::GetToolbarState2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarState2.html)
[ISldWorks::HideToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideToolbar2.html)
[ISldWorks::RemoveToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveToolbar2.html)
[ISldWorks::SetToolbarDock2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetToolbarDock2.html)

## Availability

SOLIDWORKS 2008 SP4, Revision Number 16.4
