---
title: "OnHandleSelected Method (ISwManipulatorHandler2)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwManipulatorHandler2"
member: "OnHandleSelected"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2~OnHandleSelected.html"
---

# OnHandleSelected Method (ISwManipulatorHandler2)

Gets the selected handle for this manipulator.

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
Dim instance As ISwManipulatorHandler2
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

- `pManipulator`: [IManipulator](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IManipulator.html) object
- `handleIndex`: Direction of the drag handle as defined by [swDragArrowManipulatorOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDragArrowManipulatorOptions_e.html)

## VBA Syntax

See [SwManipulatorHandler2::OnHandleSelected](ms-its:swpublishedapivb6.chm::/swpublished~SwManipulatorHandler2~OnHandleSelected.html).

## Examples

See the [ISwManipulatorHandler2](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2.html) examples.

## See Also

[ISwManipulatorHandler2 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2.html)
[ISwManipulatorHandler2 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
