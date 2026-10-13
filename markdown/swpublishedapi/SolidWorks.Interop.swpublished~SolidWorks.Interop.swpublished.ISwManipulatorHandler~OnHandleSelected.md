---
title: "OnHandleSelected Method (ISwManipulatorHandler)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwManipulatorHandler"
member: "OnHandleSelected"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler~OnHandleSelected.html"
---

# OnHandleSelected Method (ISwManipulatorHandler)

Obsolete. Superseded by [ISwManipulatorHandler2::OnHandleSelected](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwManipulatorHandler2~OnHandleSelected.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnHandleSelected( _
   ByVal pManipulator As System.Object, _
   ByVal handleIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwManipulatorHandler
Dim pManipulator As System.Object
Dim handleIndex As System.Integer

instance.OnHandleSelected(pManipulator, handleIndex)
```

### C#

```csharp
void OnHandleSelected(
   System.object pManipulator,
   System.int handleIndex
)
```

### C++/CLI

```cpp
void OnHandleSelected(
   System.Object^ pManipulator,
   System.int handleIndex
)
```

### Parameters

- `pManipulator`:
- `handleIndex`:

## VBA Syntax

See [SwManipulatorHandler::OnHandleSelected](ms-its:swpublishedapivb6.chm::/swpublished~SwManipulatorHandler~OnHandleSelected.html).

## See Also

[ISwManipulatorHandler Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler.html)
[ISwManipulatorHandler Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler_members.html)
