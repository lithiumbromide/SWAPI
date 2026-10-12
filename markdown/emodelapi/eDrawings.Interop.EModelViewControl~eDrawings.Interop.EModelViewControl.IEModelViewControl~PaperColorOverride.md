---
title: "PaperColorOverride Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "PaperColorOverride"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~PaperColorOverride.html"
---

# PaperColorOverride Property (IEModelViewControl)

Specifies whether to override the color of the paper of an eDrawings document of a drawing and display the color specified by [IEModelViewControl::PaperColor](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~PaperColor.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property PaperColorOverride As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Boolean

instance.PaperColorOverride = value

value = instance.PaperColorOverride
```

### C#

```csharp
System.bool PaperColorOverride {get; set;}
```

### C++/CLI

```cpp
property System.bool PaperColorOverride {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to override the color of the paper, false to not

## VBA Syntax

See [EModelViewControl::PaperColorOverride](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~PaperColorOverride.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2007 SP0
