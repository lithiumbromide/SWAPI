---
title: "ViewOrientation Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "ViewOrientation"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ViewOrientation.html"
---

# ViewOrientation Property (IEModelViewControl)

Sets the view orientation.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property ViewOrientation As EMVViewOrientation
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl

instance.ViewOrientation = value
```

### C#

```csharp
EMVViewOrientation ViewOrientation {set;}
```

### C++/CLI

```cpp
property EMVViewOrientation ViewOrientation {
   void set (    EMVViewOrientation value);
}
```

### Property Value

View orientation as defined by [EMVViewOrientation](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.EMVViewOrientation.html)

## VBA Syntax

See [EModelViewControl::ViewOrientation](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~ViewOrientation.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2005 SP0
