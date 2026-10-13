---
title: "GetStatusBarPane Method (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "GetStatusBarPane"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetStatusBarPane.html"
---

# GetStatusBarPane Method (IFrame)

Gets a pointer to one of up to five panes on the right side of the status bar.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStatusBarPane() As StatusBarPane
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim value As StatusBarPane

value = instance.GetStatusBarPane()
```

### C#

```csharp
StatusBarPane GetStatusBarPane()
```

### C++/CLI

```cpp
StatusBarPane^ GetStatusBarPane();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to a [status bar pane object](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStatusBarPane.html)

## VBA Syntax

See [Frame::GetStatusBarPane](ms-its:sldworksapivb6.chm::/sldworks~Frame~GetStatusBarPane.html).

## Remarks

There are only 5 panes available starting from the right of the screen to the existing SOLIDWORKS panes.

This method returns a null pointer to a pane when you have used all possible panes.

These objects appear on the status bar until they go out of scope. To use them in a project, they should be declared globally in the Visual Basic project and managed during the life cycle of the client application.

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)
[IFrame::SetStatusBarText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~SetStatusBarText.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
