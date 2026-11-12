---
title: "OnUpdateDrag Method (ISwManipulatorHandler2)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwManipulatorHandler2"
member: "OnUpdateDrag"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2~OnUpdateDrag.html"
---

# OnUpdateDrag Method (ISwManipulatorHandler2)

Called when the pointer moves while the left-mouse or right-mouse button is held down.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnUpdateDrag( _
   ByVal pManipulator As System.Object, _
   ByVal handleIndex As System.Integer, _
   ByVal newPosMathPt As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwManipulatorHandler2
Dim pManipulator As System.Object
Dim handleIndex As System.Integer
Dim newPosMathPt As System.Object

instance.OnUpdateDrag(pManipulator, handleIndex, newPosMathPt)
```

### C#

```csharp
void OnUpdateDrag(
   System.object pManipulator,
   System.int handleIndex,
   System.object newPosMathPt
)
```

### C++/CLI

```cpp
void OnUpdateDrag(
   System.Object^ pManipulator,
   System.int handleIndex,
   System.Object^ newPosMathPt
)
```

### Parameters

- `pManipulator`: [IManipulator](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IManipulator.html) object
- `handleIndex`:

  | If the manipulator is a... | Then use... |
  | --- | --- |
  | Drag arrow | swDragArrowManipulatorOptions_e |
  | Triad | swTriadManipulatorControlPoints_e |
- `newPosMathPt`: [Math point](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) indicating the pointer's new position

## VBA Syntax

See [SwManipulatorHandler2::OnUpdateDrag](ms-its:swpublishedapivb6.chm::/swpublished~SwManipulatorHandler2~OnUpdateDrag.html).

## Examples

See the [ISwManipulatorHandler2](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2.html) examples.

## See Also

[ISwManipulatorHandler2 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2.html)
[ISwManipulatorHandler2 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
