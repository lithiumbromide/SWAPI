---
title: "OnDoubleValueChanged Method (ISwManipulatorHandler2)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwManipulatorHandler2"
member: "OnDoubleValueChanged"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2~OnDoubleValueChanged.html"
---

# OnDoubleValueChanged Method (ISwManipulatorHandler2)

Indicates if the new value for the specified item is accepted or not.

## Syntax

### Visual Basic (Declaration)

```vb
Function OnDoubleValueChanged( _
   ByVal pManipulator As System.Object, _
   ByVal handleIndex As System.Integer, _
   ByRef Value As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwManipulatorHandler2
Dim pManipulator As System.Object
Dim handleIndex As System.Integer
Dim Value As System.Double
Dim value As System.Boolean

value = instance.OnDoubleValueChanged(pManipulator, handleIndex, Value)
```

### C#

```csharp
System.bool OnDoubleValueChanged(
   System.object pManipulator,
   System.int handleIndex,
   ref System.double Value
)
```

### C++/CLI

```cpp
System.bool OnDoubleValueChanged(
   System.Object^ pManipulator,
   System.int handleIndex,
   System.double% Value
)
```

### Parameters

- `pManipulator`: [IManipulator](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IManipulator.html) object
- `handleIndex`: ID of the value to change
- `Value`: New value

### Return Value

True if successful, false if not

## VBA Syntax

See [SwManipulatorHandler2::OnDoubleValueChanged](ms-its:swpublishedapivb6.chm::/swpublished~SwManipulatorHandler2~OnDoubleValueChanged.html).

## Examples

See the [ISwManipulatorHandler2](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2.html) examples.

## Remarks

If the manipulator is a drag arrow manipulator, then the value is the length of the manipulator.

## See Also

[ISwManipulatorHandler2 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2.html)
[ISwManipulatorHandler2 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
