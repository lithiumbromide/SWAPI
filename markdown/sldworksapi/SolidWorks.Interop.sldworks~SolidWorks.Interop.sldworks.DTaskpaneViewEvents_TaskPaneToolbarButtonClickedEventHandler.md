---
title: "DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler.html"
---

# DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when a toolbar button on the Task Pane is clicked.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler( _
   ByVal ButtonIndex As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler(
   System.int ButtonIndex
)
```

### C++/CLI

```cpp
public delegate System.int DTaskpaneViewEvents_TaskPaneToolbarButtonClickedEventHandler(
   System.int ButtonIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ButtonIndex`: Index of the toolbar button on the Task Pane that was clicked

## VBA Syntax

See [TaskPaneToolbarButtonClicked Event (TaskpaneView)](ms-its:sldworksapivb6.chm::/SldWorks~TaskpaneView~TaskPaneToolbarButtonClicked_EV.html).

## Examples

[Add Buttons to Task Pane (VBA)](Add_Buttons_to_Task_Pane_Example_VB.htm)
[Add Buttons to Task Pane (VB.NET)](Add_Buttons_to_Task_Pane_Example_VBNET.htm)
[Add Buttons to Task Pane (C#)](Add_Buttons_to_Task_Pane_Example_CSharp.htm)

## Remarks

If developing a C++ application, use [swAppTaskPaneToolbarButtonClicked](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTaskPaneNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
