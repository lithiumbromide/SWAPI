---
title: "FullUI Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "FullUI"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~FullUI.html"
---

# FullUI Property (IEModelViewControl)

Gets or sets whether to show complete UI mode or simple UI mode.

## Syntax

### Visual Basic (Declaration)

```vb
Property FullUI As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Integer

instance.FullUI = value

value = instance.FullUI
```

### C#

```csharp
System.int FullUI {get; set;}
```

### C++/CLI

```cpp
property System.int FullUI {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

-1 to show complete UI mode, 0 to show simple UI mode

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2008 SP0
