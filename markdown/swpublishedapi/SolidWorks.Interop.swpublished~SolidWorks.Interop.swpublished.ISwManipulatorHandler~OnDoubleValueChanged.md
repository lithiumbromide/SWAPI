---
title: "OnDoubleValueChanged Method (ISwManipulatorHandler)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwManipulatorHandler"
member: "OnDoubleValueChanged"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler~OnDoubleValueChanged.html"
---

# OnDoubleValueChanged Method (ISwManipulatorHandler)

Obsolete. Superseded by [ISwManipulatorHandler2::OnDoubleValueChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwManipulatorHandler2~OnDoubleValueChanged.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function OnDoubleValueChanged( _
   ByVal pManipulator As System.Object, _
   ByVal Id As System.Integer, _
   ByRef Value As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwManipulatorHandler
Dim pManipulator As System.Object
Dim Id As System.Integer
Dim Value As System.Double
Dim value As System.Boolean

value = instance.OnDoubleValueChanged(pManipulator, Id, Value)
```

### C#

```csharp
System.bool OnDoubleValueChanged(
   System.object pManipulator,
   System.int Id,
   ref System.double Value
)
```

### C++/CLI

```cpp
System.bool OnDoubleValueChanged(
   System.Object^ pManipulator,
   System.int Id,
   System.double% Value
)
```

### Parameters

- `pManipulator`:
- `Id`:
- `Value`:

## VBA Syntax

See [SwManipulatorHandler::OnDoubleValueChanged](ms-its:swpublishedapivb6.chm::/swpublished~SwManipulatorHandler~OnDoubleValueChanged.html).

## See Also

[ISwManipulatorHandler Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler.html)
[ISwManipulatorHandler Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler_members.html)
