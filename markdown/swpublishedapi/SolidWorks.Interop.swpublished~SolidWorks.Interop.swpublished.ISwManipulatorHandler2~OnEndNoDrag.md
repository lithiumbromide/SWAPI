---
title: "OnEndNoDrag Method (ISwManipulatorHandler2)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwManipulatorHandler2"
member: "OnEndNoDrag"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2~OnEndNoDrag.html"
---

# OnEndNoDrag Method (ISwManipulatorHandler2)

Called when a user releases a mouse button and has not dragged the pointer.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnEndNoDrag( _
   ByVal pManipulator As System.Object, _
   ByVal handleIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwManipulatorHandler2
Dim pManipulator As System.Object
Dim handleIndex As System.Integer

instance.OnEndNoDrag(pManipulator, handleIndex)
```

### C#

```csharp
void OnEndNoDrag(
   System.object pManipulator,
   System.int handleIndex
)
```

### C++/CLI

```cpp
void OnEndNoDrag(
   System.Object^ pManipulator,
   System.int handleIndex
)
```

### Parameters

- `pManipulator`: [IManipulator](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IManipulator.html) object
- `handleIndex`:

  | If the manipulator is a... | Then use... |
  | --- | --- |
  | Drag arrow | swDragArrowManipulatorOptions_e |
  | Triad | swTriadManipulatorControlPoints_e |

## VBA Syntax

See [SwManipulatorHandler2::OnEndNoDrag](ms-its:swpublishedapivb6.chm::/swpublished~SwManipulatorHandler2~OnEndNoDrag.html).

## Examples

See the [ISwManipulatorHandler2](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2.html) examples.

## See Also

[ISwManipulatorHandler2 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2.html)
[ISwManipulatorHandler2 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2_members.html)
[ISwManipulatorHandler2::OnEndDrag Method ()](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2~OnEndDrag.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
