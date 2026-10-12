---
title: "SetMirrorViewOrientation Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "SetMirrorViewOrientation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetMirrorViewOrientation.html"
---

# SetMirrorViewOrientation Method (IView)

Sets whether to mirror this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMirrorViewOrientation( _
   ByVal BSetIsMirrorView As System.Boolean, _
   ByVal BMirrorVieworientation As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim BSetIsMirrorView As System.Boolean
Dim BMirrorVieworientation As System.Integer
Dim value As System.Boolean

value = instance.SetMirrorViewOrientation(BSetIsMirrorView, BMirrorVieworientation)
```

### C#

```csharp
System.bool SetMirrorViewOrientation(
   System.bool BSetIsMirrorView,
   System.int BMirrorVieworientation
)
```

### C++/CLI

```cpp
System.bool SetMirrorViewOrientation(
   System.bool BSetIsMirrorView,
   System.int BMirrorVieworientation
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BSetIsMirrorView`: True to mirror the view, false to not
- `BMirrorVieworientation`: Orientation of the mirror view as defined in [swMirrorViewPositions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMirrorViewPositions_e.html)

### Return Value

True if the method executed successfully, false if not

## VBA Syntax

See [View::SetMirrorViewOrientation](ms-its:sldworksapivb6.chm::/sldworks~View~SetMirrorViewOrientation.html).

## Examples

[Mirror View (C#)](Mirror_View_Example_CSharp.htm)
[Mirror View (VB.NET)](Mirror_View_Example_VBNET.htm)
[Mirror View (VBA)](Mirror_View_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetMirrorViewOrientation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetMirrorViewOrientation.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
