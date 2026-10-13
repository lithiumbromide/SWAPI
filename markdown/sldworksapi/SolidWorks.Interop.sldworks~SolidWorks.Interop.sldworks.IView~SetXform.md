---
title: "SetXform Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "SetXform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetXform.html"
---

# SetXform Method (IView)

Sets the matrix used for display of this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetXform( _
   ByVal Transform As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Transform As System.Object
Dim value As System.Boolean

value = instance.SetXform(Transform)
```

### C#

```csharp
System.bool SetXform(
   System.object Transform
)
```

### C++/CLI

```cpp
System.bool SetXform(
   System.Object^ Transform
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Transform`: Array of 3 doubles (see **Remarks**)

### Return Value

True if transform successfully set, false if not

## VBA Syntax

See [View::SetXform](ms-its:sldworksapivb6.chm::/sldworks~View~SetXform.html).

## Remarks

The 3 doubles are the X and Y position of the view, relative to the sheet origin, and the scale of the view.

Any view alignments that might affect this view are handled the same way as if you were using the user interface to draw the view to move it. If it is aligned with another view, then it will only move along the alignment vector. If it has child views that are aligned with it, then those views will also be moved along with this view.

Calling this method is equivalent to setting the [IView::Position](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~Position.html) or [IView::IPosition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IPosition.html) property (to set X and Y), and the [IView::ScaleDecimal](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~ScaleDecimal.html) property (to set the scale).

To get the view matrix, use [IView::GetXform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetXform.html) or [IView::IGetXform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetXform.html) method.

Using this method may cause changes to the graphics of the drawing. Once all the view-related changes have been made, the user should call [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html) to regenerate the drawing, in order to see these changes.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::ISetXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ISetXform.html)
[IView::GetXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetXform.html)
[IView::IGetXform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetXform.html)
