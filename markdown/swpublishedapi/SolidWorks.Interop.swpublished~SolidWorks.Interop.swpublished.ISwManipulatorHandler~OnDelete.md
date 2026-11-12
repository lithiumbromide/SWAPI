---
title: "OnDelete Method (ISwManipulatorHandler)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwManipulatorHandler"
member: "OnDelete"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler~OnDelete.html"
---

# OnDelete Method (ISwManipulatorHandler)

Obsolete. Superseded by [ISwManipulatorHandler2::OnDelete](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwManipulatorHandler2~OnDelete.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function OnDelete( _
   ByVal pManipulator As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwManipulatorHandler
Dim pManipulator As System.Object
Dim value As System.Boolean

value = instance.OnDelete(pManipulator)
```

### C#

```csharp
System.bool OnDelete(
   System.object pManipulator
)
```

### C++/CLI

```cpp
System.bool OnDelete(
   System.Object^ pManipulator
)
```

### Parameters

- `pManipulator`:

## VBA Syntax

See [SwManipulatorHandler::OnDelete](ms-its:swpublishedapivb6.chm::/swpublished~SwManipulatorHandler~OnDelete.html).

## See Also

[ISwManipulatorHandler Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler.html)
[ISwManipulatorHandler Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler_members.html)
