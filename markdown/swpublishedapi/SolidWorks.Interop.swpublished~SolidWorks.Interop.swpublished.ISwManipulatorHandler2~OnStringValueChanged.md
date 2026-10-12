---
title: "OnStringValueChanged Method (ISwManipulatorHandler2)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwManipulatorHandler2"
member: "OnStringValueChanged"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2~OnStringValueChanged.html"
---

# OnStringValueChanged Method (ISwManipulatorHandler2)

Indicates if the new value for the specified item is accepted or not.

## Syntax

### Visual Basic (Declaration)

```vb
Function OnStringValueChanged( _
   ByVal pManipulator As System.Object, _
   ByVal handleIndex As System.Integer, _
   ByRef Value As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwManipulatorHandler2
Dim pManipulator As System.Object
Dim handleIndex As System.Integer
Dim Value As System.String
Dim value As System.Boolean

value = instance.OnStringValueChanged(pManipulator, handleIndex, Value)
```

### C#

```csharp
System.bool OnStringValueChanged(
   System.object pManipulator,
   System.int handleIndex,
   ref System.string Value
)
```

### C++/CLI

```cpp
System.bool OnStringValueChanged(
   System.Object^ pManipulator,
   System.int handleIndex,
   System.String^% Value
)
```

### Parameters

- `pManipulator`: [IManipulator](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IManipulator.html) object
- `handleIndex`: ID of the string value to change
- `Value`: New string value

### Return Value

True if the add-in application accepts the new string value, false if not

## VBA Syntax

See [SwManipulatorHandler2::OnStringValueChanged](ms-its:swpublishedapivb6.chm::/swpublished~SwManipulatorHandler2~OnStringValueChanged.html).

## Examples

See the [ISwManipulatorHandler2](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2.html) examples.

## See Also

[ISwManipulatorHandler2 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2.html)
[ISwManipulatorHandler2 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
