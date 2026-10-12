---
title: "OnHandleLmbSelected Method (ISwManipulatorHandler2)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwManipulatorHandler2"
member: "OnHandleLmbSelected"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2~OnHandleLmbSelected.html"
---

# OnHandleLmbSelected Method (ISwManipulatorHandler2)

Called when a user clicks the left-mouse button.

## Syntax

### Visual Basic (Declaration)

```vb
Function OnHandleLmbSelected( _
   ByVal pManipulator As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwManipulatorHandler2
Dim pManipulator As System.Object
Dim value As System.Boolean

value = instance.OnHandleLmbSelected(pManipulator)
```

### C#

```csharp
System.bool OnHandleLmbSelected(
   System.object pManipulator
)
```

### C++/CLI

```cpp
System.bool OnHandleLmbSelected(
   System.Object^ pManipulator
)
```

### Parameters

- `pManipulator`: [IManipulator](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IManipulator.html) object

### Return Value

True if successful, false if not

## VBA Syntax

See [SwManipulatorHandler2::OnHandleLmbSelected](ms-its:swpublishedapivb6.chm::/swpublished~SwManipulatorHandler2~OnHandleLmbSelected.html).

## Examples

See the [ISwManipulatorHandler2](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2.html) examples.

## See Also

[ISwManipulatorHandler2 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2.html)
[ISwManipulatorHandler2 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
