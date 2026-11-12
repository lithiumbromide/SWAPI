---
title: "OnItemSetFocus Method (ISwManipulatorHandler2)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwManipulatorHandler2"
member: "OnItemSetFocus"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2~OnItemSetFocus.html"
---

# OnItemSetFocus Method (ISwManipulatorHandler2)

Sets the focus on the specified item.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnItemSetFocus( _
   ByVal pManipulator As System.Object, _
   ByVal handleIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwManipulatorHandler2
Dim pManipulator As System.Object
Dim handleIndex As System.Integer

instance.OnItemSetFocus(pManipulator, handleIndex)
```

### C#

```csharp
void OnItemSetFocus(
   System.object pManipulator,
   System.int handleIndex
)
```

### C++/CLI

```cpp
void OnItemSetFocus(
   System.Object^ pManipulator,
   System.int handleIndex
)
```

### Parameters

- `pManipulator`: [IManipulator](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IManipulator.html) object
- `handleIndex`: ID of item on which to set focus

## VBA Syntax

See [SwManipulatorHandler2::OnItemSetFocus](ms-its:swpublishedapivb6.chm::/swpublished~SwManipulatorHandler2~OnItemSetFocus.html).

## Examples

See the [ISwManipulatorHandler2](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2.html) examples.

## See Also

[ISwManipulatorHandler2 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2.html)
[ISwManipulatorHandler2 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
