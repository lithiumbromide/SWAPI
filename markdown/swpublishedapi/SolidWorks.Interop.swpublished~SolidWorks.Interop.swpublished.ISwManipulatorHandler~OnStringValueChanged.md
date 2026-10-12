---
title: "OnStringValueChanged Method (ISwManipulatorHandler)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwManipulatorHandler"
member: "OnStringValueChanged"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler~OnStringValueChanged.html"
---

# OnStringValueChanged Method (ISwManipulatorHandler)

Obsolete. Superseded by [ISwManipulatorHandler2::OnStringValueChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwManipulatorHandler2~OnStringValueChanged.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function OnStringValueChanged( _
   ByVal pManipulator As System.Object, _
   ByVal Id As System.Integer, _
   ByRef Value As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwManipulatorHandler
Dim pManipulator As System.Object
Dim Id As System.Integer
Dim Value As System.String
Dim value As System.Boolean

value = instance.OnStringValueChanged(pManipulator, Id, Value)
```

### C#

```csharp
System.bool OnStringValueChanged(
   System.object pManipulator,
   System.int Id,
   ref System.string Value
)
```

### C++/CLI

```cpp
System.bool OnStringValueChanged(
   System.Object^ pManipulator,
   System.int Id,
   System.String^% Value
)
```

### Parameters

- `pManipulator`:
- `Id`:
- `Value`:

## VBA Syntax

See [SwManipulatorHandler::OnStringValueChanged](ms-its:swpublishedapivb6.chm::/swpublished~SwManipulatorHandler~OnStringValueChanged.html).

## See Also

[ISwManipulatorHandler Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler.html)
[ISwManipulatorHandler Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler_members.html)
