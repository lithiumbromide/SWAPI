---
title: "ShowShadedEdges Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "ShowShadedEdges"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowShadedEdges.html"
---

# ShowShadedEdges Property (IEModelViewControl)

Gets or sets whether to show edges in shaded mode.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowShadedEdges As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Boolean

instance.ShowShadedEdges = value

value = instance.ShowShadedEdges
```

### C#

```csharp
System.bool ShowShadedEdges {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowShadedEdges {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to show edges in shaded mode, false to not

## VBA Syntax

See [EModelViewControl::ShowShadedEdges](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~ShowShadedEdges.html).

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::ViewState Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ViewState.html)

## Availability

eDrawings API 2014 SP0
