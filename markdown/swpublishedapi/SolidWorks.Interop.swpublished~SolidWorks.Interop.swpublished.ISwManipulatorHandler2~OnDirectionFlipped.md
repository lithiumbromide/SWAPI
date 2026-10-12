---
title: "OnDirectionFlipped Method (ISwManipulatorHandler2)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwManipulatorHandler2"
member: "OnDirectionFlipped"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2~OnDirectionFlipped.html"
---

# OnDirectionFlipped Method (ISwManipulatorHandler2)

Flips the direction of the manipulator.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnDirectionFlipped( _
   ByVal pManipulator As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwManipulatorHandler2
Dim pManipulator As System.Object

instance.OnDirectionFlipped(pManipulator)
```

### C#

```csharp
void OnDirectionFlipped(
   System.object pManipulator
)
```

### C++/CLI

```cpp
void OnDirectionFlipped(
   System.Object^ pManipulator
)
```

### Parameters

- `pManipulator`: [IManipulator](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IManipulator.html) object

## VBA Syntax

See [SwManipulatorHandler2::OnDirectionFlipped](ms-its:swpublishedapivb6.chm::/swpublished~SwManipulatorHandler2~OnDirectionFlipped.html).

## Examples

See the [ISwManipulatorHandler2](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2.html) examples.

## See Also

[ISwManipulatorHandler2 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2.html)
[ISwManipulatorHandler2 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
