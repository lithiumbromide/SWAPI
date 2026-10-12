---
title: "OnUpdateDrag Method (ISwManipulatorHandler)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwManipulatorHandler"
member: "OnUpdateDrag"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler~OnUpdateDrag.html"
---

# OnUpdateDrag Method (ISwManipulatorHandler)

Obsolete. Superseded by [ISwManipulatorHandler2::OnUpdateDrag](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwManipulatorHandler2~OnUpdateDrag.html).

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
Dim instance As ISwManipulatorHandler
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

- `pManipulator`:
- `handleIndex`:
- `newPosMathPt`:

## VBA Syntax

See [SwManipulatorHandler::OnUpdateDrag](ms-its:swpublishedapivb6.chm::/swpublished~SwManipulatorHandler~OnUpdateDrag.html).

## See Also

[ISwManipulatorHandler Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler.html)
[ISwManipulatorHandler Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler_members.html)
