---
title: "GetXform Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetXform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetXform.html"
---

# GetXform Method (IView)

Gets the matrix used for displaying this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetXform() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetXform()
```

### C#

```csharp
System.object GetXform()
```

### C++/CLI

```cpp
System.Object^ GetXform();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of 3 doubles that describe the location and scale of the drawing view (see **Remarks**)

## VBA Syntax

See [View::GetXform](ms-its:sldworksapivb6.chm::/sldworks~View~GetXform.html).

## Remarks

The first two values returned are the X and Y locations of the view relative to the sheet origin, and the third value returned is the scale of the drawing view.

Because of a Microsoft compilation issue, the Dispatch name generated in the **swdisp.h** and **swdisp.cpp** files for the Dispatch version of this method is GetXform (with a lower-case letter f). To work around this:

- Use GetXform in your code instead of GetXForm.

  - or -
- Modify the swdisp.h and swdisp.cpp files so that the declaration for GetXForm in the [IView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) object is changed to GetXform. Remember to change it when you upgrade the SOLIDWORKS Design software.

[IView::GetViewXform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetViewXform.html) and [IView::IGetViewXform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetViewXform.html) get the transform from model space origin to drawing space origin.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetXform.html)
[IView::ISetXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ISetXform.html)
[IView::SetXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetXform.html)
[IView::ModelToViewTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ModelToViewTransform.html)
