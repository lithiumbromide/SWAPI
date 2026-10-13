---
title: "ActiveViewRectangle Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "ActiveViewRectangle"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ActiveViewRectangle.html"
---

# ActiveViewRectangle Property (IEModelViewControl)

Gets the screen coordinates of the upper-left and lower-right corners of the window.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ActiveViewRectangle As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Object

value = instance.ActiveViewRectangle
```

### C#

```csharp
System.object ActiveViewRectangle {get;}
```

### C++/CLI

```cpp
property System.Object^ ActiveViewRectangle {
   System.Object^ get();
}
```

### Property Value

Array of four longs or integers, which are the x and y coordinates of the upper-left and lower-right corners of the window

## VBA Syntax

See [EModelViewControl::ActiveViewRectangle](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~ActiveViewRectangle.html).

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2014 SP0
