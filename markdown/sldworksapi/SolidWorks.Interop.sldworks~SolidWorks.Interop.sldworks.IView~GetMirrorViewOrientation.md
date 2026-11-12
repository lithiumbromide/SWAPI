---
title: "GetMirrorViewOrientation Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetMirrorViewOrientation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetMirrorViewOrientation.html"
---

# GetMirrorViewOrientation Method (IView)

Gets whether this view is mirrored.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMirrorViewOrientation( _
   ByRef BIsMirrorView As System.Boolean, _
   ByRef LMirrorViewOrientation As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim BIsMirrorView As System.Boolean
Dim LMirrorViewOrientation As System.Integer
Dim value As System.Boolean

value = instance.GetMirrorViewOrientation(BIsMirrorView, LMirrorViewOrientation)
```

### C#

```csharp
System.bool GetMirrorViewOrientation(
   out System.bool BIsMirrorView,
   out System.int LMirrorViewOrientation
)
```

### C++/CLI

```cpp
System.bool GetMirrorViewOrientation(
   [Out] System.bool BIsMirrorView,
   [Out] System.int LMirrorViewOrientation
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BIsMirrorView`: True if the view is mirrored, false if not
- `LMirrorViewOrientation`: Orientation of the mirror view as defined in [swMirrorViewPositions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMirrorViewPositions_e.html)

### Return Value

True if the method executed successfully, false if not

## VBA Syntax

See [View::GetMirrorViewOrientation](ms-its:sldworksapivb6.chm::/sldworks~View~GetMirrorViewOrientation.html).

## Examples

[Mirror View (C#)](Mirror_View_Example_CSharp.htm)
[Mirror View (VB.NET)](Mirror_View_Example_VBNET.htm)
[Mirror View (VBA)](Mirror_View_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IViewe::SetMirrorViewOrientation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetMirrorViewOrientation.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
