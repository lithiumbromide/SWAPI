---
title: "IGetViewXform Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetViewXform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetViewXform.html"
---

# IGetViewXform Method (IView)

Gets the transform from model space origin to drawing space origin.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetViewXform() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Double

value = instance.IGetViewXform()
```

### C#

```csharp
System.double IGetViewXform()
```

### C++/CLI

```cpp
System.double IGetViewXform();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [View::IGetViewXform](ms-its:sldworksapivb6.chm::/sldworks~View~IGetViewXform.html).

## Remarks

The return value is formatted as the following array of 13 doubles:

- [0-8] is a 3x3 matrix of the view rotation
- [9-11] is a 1x3 vector of translation
- [12] is the scaling of the transformation

[IView::GetXform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetXform.html) and [IView::IGetXform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetXform.html) return the location of the drawing view center with respect to the drawing origin.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetViewXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetViewXform.html)
[IView::ModelToViewTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ModelToViewTransform.html)
