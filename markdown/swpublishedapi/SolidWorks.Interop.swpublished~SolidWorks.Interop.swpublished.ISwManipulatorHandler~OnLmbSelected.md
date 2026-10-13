---
title: "OnLmbSelected Method (ISwManipulatorHandler)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwManipulatorHandler"
member: "OnLmbSelected"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler~OnLmbSelected.html"
---

# OnLmbSelected Method (ISwManipulatorHandler)

Obsolete. Superseded by [ISwManipulatorHandler2::OnHandleLmbSelected](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwManipulatorHandler2~OnHandleLmbSelected.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function OnLmbSelected( _
   ByVal pManipulator As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwManipulatorHandler
Dim pManipulator As System.Object
Dim value As System.Boolean

value = instance.OnLmbSelected(pManipulator)
```

### C#

```csharp
System.bool OnLmbSelected(
   System.object pManipulator
)
```

### C++/CLI

```cpp
System.bool OnLmbSelected(
   System.Object^ pManipulator
)
```

### Parameters

- `pManipulator`:

## VBA Syntax

See [SwManipulatorHandler::OnLmbSelected](ms-its:swpublishedapivb6.chm::/swpublished~SwManipulatorHandler~OnLmbSelected.html).

## See Also

[ISwManipulatorHandler Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler.html)
[ISwManipulatorHandler Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler_members.html)
