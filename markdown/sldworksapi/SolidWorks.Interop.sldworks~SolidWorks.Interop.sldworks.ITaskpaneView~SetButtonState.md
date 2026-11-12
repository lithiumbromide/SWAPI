---
title: "SetButtonState Method (ITaskpaneView)"
project: "SOLIDWORKS API Help"
interface: "ITaskpaneView"
member: "SetButtonState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~SetButtonState.html"
---

# SetButtonState Method (ITaskpaneView)

Sets whether the Task Pane button is enabled.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetButtonState( _
   ByVal ButtonIndex As System.Integer, _
   ByVal Enable As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ITaskpaneView
Dim ButtonIndex As System.Integer
Dim Enable As System.Boolean

instance.SetButtonState(ButtonIndex, Enable)
```

### C#

```csharp
void SetButtonState(
   System.int ButtonIndex,
   System.bool Enable
)
```

### C++/CLI

```cpp
void SetButtonState(
   System.int ButtonIndex,
   System.bool Enable
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ButtonIndex`: Index of Task Pane button
- `Enable`: True to enable Task Pane button, false to disable it

## VBA Syntax

See [TaskpaneView::SetButtonState](ms-its:sldworksapivb6.chm::/sldworks~TaskpaneView~SetButtonState.html).

## Examples

[Add Buttons to Task Pane (C#)](Add_Buttons_to_Task_Pane_Example_CSharp.htm)
[Add Buttons to Task Pane (VB.NET)](Add_Buttons_to_Task_Pane_Example_VBNET.htm)
[Add Buttons to Task Pane (VBA)](Add_Buttons_to_Task_Pane_Example_VB.htm)

## See Also

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.html)
[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.html)
[ITaskpaneView::GetButtonState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~GetButtonState.html)
[ITaskpaneView::AddCustomButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddCustomButton.html)
[ITaskpaneView::AddStandardButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddStandardButton.html)
[DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
