---
title: "IGetSketch Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetSketch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSketch.html"
---

# IGetSketch Method (IView)

Gets the sketch used by this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSketch() As Sketch
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As Sketch

value = instance.IGetSketch()
```

### C#

```csharp
Sketch IGetSketch()
```

### C++/CLI

```cpp
Sketch^ IGetSketch();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)

## VBA Syntax

See [View::IGetSketch](ms-its:sldworksapivb6.chm::/sldworks~View~IGetSketch.html).

## Remarks

Each drawing view contains an underlying sketch. The user can activate the sketch for a drawing view by double-clicking the view. Once the drawing view is active, you can add sketch directly to the view's sketch.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSketch.html)
