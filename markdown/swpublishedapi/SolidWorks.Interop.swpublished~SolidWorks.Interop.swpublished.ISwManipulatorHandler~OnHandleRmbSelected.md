---
title: "OnHandleRmbSelected Method (ISwManipulatorHandler)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwManipulatorHandler"
member: "OnHandleRmbSelected"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler~OnHandleRmbSelected.html"
---

# OnHandleRmbSelected Method (ISwManipulatorHandler)

Obsolete. Superseded by [ISwManipulatorHandler2::OnHandleRmbSelected](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwManipulatorHandler2~OnHandleRmbSelected.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnHandleRmbSelected( _
   ByVal pManipulator As System.Object, _
   ByVal handleIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwManipulatorHandler
Dim pManipulator As System.Object
Dim handleIndex As System.Integer

instance.OnHandleRmbSelected(pManipulator, handleIndex)
```

### C#

```csharp
void OnHandleRmbSelected(
   System.object pManipulator,
   System.int handleIndex
)
```

### C++/CLI

```cpp
void OnHandleRmbSelected(
   System.Object^ pManipulator,
   System.int handleIndex
)
```

### Parameters

- `pManipulator`:
- `handleIndex`:

## VBA Syntax

See [SwManipulatorHandler::OnHandleRmbSelected](ms-its:swpublishedapivb6.chm::/swpublished~SwManipulatorHandler~OnHandleRmbSelected.html).

## See Also

[ISwManipulatorHandler Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler.html)
[ISwManipulatorHandler Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler_members.html)
