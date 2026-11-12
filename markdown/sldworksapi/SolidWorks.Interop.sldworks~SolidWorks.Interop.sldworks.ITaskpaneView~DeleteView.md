---
title: "DeleteView Method (ITaskpaneView)"
project: "SOLIDWORKS API Help"
interface: "ITaskpaneView"
member: "DeleteView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~DeleteView.html"
---

# DeleteView Method (ITaskpaneView)

Removes the application-level tab from the Task Pane view.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteView() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITaskpaneView
Dim value As System.Boolean

value = instance.DeleteView()
```

### C#

```csharp
System.bool DeleteView()
```

### C++/CLI

```cpp
System.bool DeleteView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if tab is removed, false if not

## VBA Syntax

See [TaskpaneView::DeleteView](ms-its:sldworksapivb6.chm::/sldworks~TaskpaneView~DeleteView.html).

## Examples

[Add Buttons to Task Pane (VBA)](Add_Buttons_to_Task_Pane_Example_VB.htm)
[Add Buttons to Task Pane (VB.NET)](Add_Buttons_to_Task_Pane_Example_VBNET.htm)
[Add Buttons to Task Pane (C#)](Add_Buttons_to_Task_Pane_Example_CSharp.htm)

## See Also

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.html)
[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
