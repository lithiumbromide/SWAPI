---
title: "OnItemSetFocus Method (ISwManipulatorHandler)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwManipulatorHandler"
member: "OnItemSetFocus"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler~OnItemSetFocus.html"
---

# OnItemSetFocus Method (ISwManipulatorHandler)

Obsolete. Superseded by [ISwManipulatorHandler2::OnItemSetFocus](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwManipulatorHandler2~OnItemSetFocus.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnItemSetFocus( _
   ByVal pManipulator As System.Object, _
   ByVal Id As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwManipulatorHandler
Dim pManipulator As System.Object
Dim Id As System.Integer

instance.OnItemSetFocus(pManipulator, Id)
```

### C#

```csharp
void OnItemSetFocus(
   System.object pManipulator,
   System.int Id
)
```

### C++/CLI

```cpp
void OnItemSetFocus(
   System.Object^ pManipulator,
   System.int Id
)
```

### Parameters

- `pManipulator`:
- `Id`:

## VBA Syntax

See [SwManipulatorHandler::OnItemSetFocus](ms-its:swpublishedapivb6.chm::/swpublished~SwManipulatorHandler~OnItemSetFocus.html).

## See Also

[ISwManipulatorHandler Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler.html)
[ISwManipulatorHandler Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler_members.html)
