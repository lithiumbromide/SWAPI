---
title: "CreateTaskpaneView2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "CreateTaskpaneView2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreateTaskpaneView2.html"
---

# CreateTaskpaneView2 Method (ISldWorks)

Obsolete. Superseded by [ISldworks::CreateTaskpaneView3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreateTaskpaneView3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateTaskpaneView2( _
   ByVal Bitmap As System.String, _
   ByVal ToolTip As System.String _
) As TaskpaneView
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Bitmap As System.String
Dim ToolTip As System.String
Dim value As TaskpaneView

value = instance.CreateTaskpaneView2(Bitmap, ToolTip)
```

### C#

```csharp
TaskpaneView CreateTaskpaneView2(
   System.string Bitmap,
   System.string ToolTip
)
```

### C++/CLI

```cpp
TaskpaneView^ CreateTaskpaneView2(
   System.String^ Bitmap,
   System.String^ ToolTip
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Bitmap`: Path and file name of the bitmap for the tab of this Task Pane view (see Remarks)
- `ToolTip`: ToolTip for this Task Pane view

### Return Value

[Task Pane view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITaskpaneView.html)

## VBA Syntax

See [SldWorks::CreateTaskpaneView2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~CreateTaskpaneView2.html).

## Remarks

The bitmap should be 16 colors and 16 x 18 (width x height) pixels. Any portions of the bitmap that are white (RGB 255,255,255) will be transparent.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::ActivateTaskPane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivateTaskPane.html)
[ISldWorks::RefreshTaskpaneContent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RefreshTaskpaneContent.html)
[ISldWorks::TaskPaneIsPinned Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~TaskPaneIsPinned.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
