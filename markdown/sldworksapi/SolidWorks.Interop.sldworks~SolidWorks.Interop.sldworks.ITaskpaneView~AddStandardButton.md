---
title: "AddStandardButton Method (ITaskpaneView)"
project: "SOLIDWORKS API Help"
interface: "ITaskpaneView"
member: "AddStandardButton"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddStandardButton.html"
---

# AddStandardButton Method (ITaskpaneView)

Adds a standard SOLIDWORKS button to the Task Pane.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddStandardButton( _
   ByVal BitmapOption As System.Integer, _
   ByVal ToolTip As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITaskpaneView
Dim BitmapOption As System.Integer
Dim ToolTip As System.String
Dim value As System.Boolean

value = instance.AddStandardButton(BitmapOption, ToolTip)
```

### C#

```csharp
System.bool AddStandardButton(
   System.int BitmapOption,
   System.string ToolTip
)
```

### C++/CLI

```cpp
System.bool AddStandardButton(
   System.int BitmapOption,
   System.String^ ToolTip
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BitmapOption`: Type of standard SOLIDWORKS button as defined in [swTaskPaneBitmapsOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTaskPaneBitmapsOptions_e.html)
- `ToolTip`: ToolTip for the standard SOLIDWORKS button

### Return Value

True if a standard SOLIDWORKS button is added to the Task Pane, false if not

## VBA Syntax

See [TaskpaneView::AddStandardButton](ms-its:sldworksapivb6.chm::/sldworks~TaskpaneView~AddStandardButton.html).

## Examples

[Add Buttons to Task Pane (VBA)](Add_Buttons_to_Task_Pane_Example_VB.htm)
[Add Buttons to Task Pane (VB.NET)](Add_Buttons_to_Task_Pane_Example_VBNET.htm)
[Add Buttons to Task Pane (C#)](Add_Buttons_to_Task_Pane_Example_CSharp.htm)

## See Also

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.html)
[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.html)
[ITaskpaneView::AddCustomButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddCustomButton.html)
[DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler.html)
[ITaskpaneView::GetButtonState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~GetButtonState.html)
[ITaskpaneView::SetButtonState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~SetButtonState.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
