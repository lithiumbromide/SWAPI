---
title: "ViewOperator Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "ViewOperator"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ViewOperator.html"
---

# ViewOperator Property (IEModelViewControl)

Sets the select, rotate, zoom, and pan tools.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property ViewOperator As EMVOperators
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl

instance.ViewOperator = value
```

### C#

```csharp
EMVOperators ViewOperator {set;}
```

### C++/CLI

```cpp
property EMVOperators ViewOperator {
   void set (    EMVOperators value);
}
```

### Property Value

Tools as defined by [EMVOperators](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.EMVOperators.html)

## VBA Syntax

See [EModelViewControl::ViewOperator](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~ViewOperator.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2005 SP0
