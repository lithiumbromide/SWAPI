---
title: "GetButtonState Method (ITaskpaneView)"
project: "SOLIDWORKS API Help"
interface: "ITaskpaneView"
member: "GetButtonState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~GetButtonState.html"
---

# GetButtonState Method (ITaskpaneView)

Gets whether the Task Pane button is enabled.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetButtonState( _
   ByVal ButtonIndex As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITaskpaneView
Dim ButtonIndex As System.Integer
Dim value As System.Boolean

value = instance.GetButtonState(ButtonIndex)
```

### C#

```csharp
System.bool GetButtonState(
   System.int ButtonIndex
)
```

### C++/CLI

```cpp
System.bool GetButtonState(
   System.int ButtonIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ButtonIndex`: Index of Task Pane button

### Return Value

True if the Task Pane button is enabled, false if not

## VBA Syntax

See [TaskpaneView::GetButtonState](ms-its:sldworksapivb6.chm::/sldworks~TaskpaneView~GetButtonState.html).

## Examples

[Add Buttons to Task Pane (C#)](Add_Buttons_to_Task_Pane_Example_CSharp.htm)
[Add Buttons to Task Pane (VB.NET)](Add_Buttons_to_Task_Pane_Example_VBNET.htm)
[Add Buttons to Task Pane (VBA)](Add_Buttons_to_Task_Pane_Example_VB.htm)

## See Also

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.html)
[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.html)
[ITaskpaneView::SetButtonState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~SetButtonState.html)
[ITaskpaneView::AddCustomButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddCustomButton.html)
[ITaskpaneView::AddStandardButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddStandardButton.html)
[DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
