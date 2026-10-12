---
title: "ViewOperator Property (IEModelMarkupControl)"
project: "eDrawings API Help"
interface: "IEModelMarkupControl"
member: "ViewOperator"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~ViewOperator.html"
---

# ViewOperator Property (IEModelMarkupControl)

Sets the markup tools.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property ViewOperator As EMVMarkupOperators
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelMarkupControl

instance.ViewOperator = value
```

### C#

```csharp
EMVMarkupOperators ViewOperator {set;}
```

### C++/CLI

```cpp
property EMVMarkupOperators ViewOperator {
   void set (    EMVMarkupOperators value);
}
```

### Property Value

Markup tools as defined by [EMVMarkupOperators](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.EMVMarkupOperators.html)

## VBA Syntax

See [EModelMarkupControl::ViewOperator](ms-its:emodelapivb6.chm::/EModelViewMarkup~EModelMarkupControl~ViewOperator.html).

## See Also

[IEModelMarkupControl Interface](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl.html)
[IEModelMarkupControl Members](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl_members.html)

## Availability

eDrawings API 2005 SP0
