---
title: "GetVisibleBox Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "GetVisibleBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetVisibleBox.html"
---

# GetVisibleBox Method (IModelView)

Gets the boundaries of the visible model view window.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVisibleBox() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Object

value = instance.GetVisibleBox()
```

### C#

```csharp
System.object GetVisibleBox()
```

### C++/CLI

```cpp
System.Object^ GetVisibleBox();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of four longs (win_x_min, win-y_min, win_x_max, and win_y_max) in screen pixels indicating the boundaries of the visible model view window; any part of the model view window blocked by the FeatureManager design tree is excluded

## VBA Syntax

See [ModelView::GetVisibleBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GetVisibleBox.html).

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::IGetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetVisibleBox.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
