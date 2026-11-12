---
title: "DragToolbarButton Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "DragToolbarButton"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DragToolbarButton.html"
---

# DragToolbarButton Method (ISldWorks)

Copies the specified toolbar button from the specified native SOLIDWORKS toolbar or [ICommandGroup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup.html) toolbar to the specified native SOLIDWORKS toolbar or ICommandGroup toolbar.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DragToolbarButton( _
   ByVal SourceToolbar As System.Integer, _
   ByVal TargetToolbar As System.Integer, _
   ByVal SourceIndex As System.Integer, _
   ByVal TargetIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim SourceToolbar As System.Integer
Dim TargetToolbar As System.Integer
Dim SourceIndex As System.Integer
Dim TargetIndex As System.Integer

instance.DragToolbarButton(SourceToolbar, TargetToolbar, SourceIndex, TargetIndex)
```

### C#

```csharp
void DragToolbarButton(
   System.int SourceToolbar,
   System.int TargetToolbar,
   System.int SourceIndex,
   System.int TargetIndex
)
```

### C++/CLI

```cpp
void DragToolbarButton(
   System.int SourceToolbar,
   System.int TargetToolbar,
   System.int SourceIndex,
   System.int TargetIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SourceToolbar`: Toolbar as defined by [swToolbar_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swToolbar_e.html) or if a CommandGroup toolbar, use [ICommandGroup::ToolbarId](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~ToolbarId.html)
- `TargetToolbar`: Toolbar as defined by [swToolbar_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swToolbar_e.html) or if a CommandGroup toolbar, use [ICommandGroup::ToolbarId](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~ToolbarId.html)
- `SourceIndex`: 0-based index of the toolbar button on the native SOLIDWORKS toolbar or CommandGroup toolbar
- `TargetIndex`: 0-based index of the toolbar button on the native SOLIDWORKS toolbar or CommandGroup toolbar

## VBA Syntax

See [SldWorks::DragToolbarButton](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~DragToolbarButton.html).

## Remarks

This method makes a copy of the specified source toolbar button and moves a copy of the toolbar button to the target toolbar. This method does not remove the specified source toolbar button from the source toolbar.

Examine the toolbars in the user interface to determine the values for SourceIndex and TargetIndex.

Using this method to drag a toolbar button from one toolbar to another is persistent across sessions of SOLIDWORKS and need only be performed once. For example, do not include this operation in any SolidsWorks API start-up routine because you would then be adding a copy of the same toolbar button to the same target toolbar every time you start up SOLIDWORKS.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::AddToolbar4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar4.html)
[ISldWorks::AddToolbarCommand2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbarCommand2.html)
[ISldWorks::GetCommandID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCommandID.html)
[ISldWorks::GetLastToolbarID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLastToolbarID.html)
[ISldWorks::GetToolbarDock2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarDock2.html)
[ISldWorks::GetToolbarState2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarState2.html)
[ISldWorks::HideToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideToolbar2.html)
[ISldWorks::RemoveToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveToolbar2.html)
[ISldWorks::SetToolbarDock2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetToolbarDock2.html)
[ISldWorks::DragToolbarButtonFromCommandID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DragToolbarButtonFromCommandID.html)

## Availability

SOLIDWORKS 206 FCS, Revision Number 14.0
