---
title: "OnEndNoDrag Method (ISwManipulatorHandler)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwManipulatorHandler"
member: "OnEndNoDrag"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler~OnEndNoDrag.html"
---

# OnEndNoDrag Method (ISwManipulatorHandler)

Obsolete. Superseded by [ISwManipulatorHandler2::OnEndNoDrag](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwManipulatorHandler2~OnEndNoDrag.html).

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
Dim instance As ISwManipulatorHandler
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

- `pManipulator`:
- `handleIndex`:

## VBA Syntax

See [SwManipulatorHandler::OnEndNoDrag](ms-its:swpublishedapivb6.chm::/swpublished~SwManipulatorHandler~OnEndNoDrag.html).

## See Also

[ISwManipulatorHandler Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler.html)
[ISwManipulatorHandler Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler_members.html)
