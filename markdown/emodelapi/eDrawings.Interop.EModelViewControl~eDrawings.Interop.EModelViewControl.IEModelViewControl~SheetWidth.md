---
title: "SheetWidth Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "SheetWidth"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SheetWidth.html"
---

# SheetWidth Property (IEModelViewControl)

Gets the width of the drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SheetWidth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Double

value = instance.SheetWidth
```

### C#

```csharp
System.double SheetWidth {get;}
```

### C++/CLI

```cpp
property System.double SheetWidth {
   System.double get();
}
```

### Property Value

Width of drawing sheet in either inches or millimeters, depending on the regional settings of your computer, not the model units of the drawing

## VBA Syntax

See [EModelViewControl::SheetWidth](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~SheetWidth.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::ShowSheet Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowSheet.html)
[IEModelViewControl::CurrentSheetIndex Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CurrentSheetIndex.html)
[IEModelViewControl::SheetCount Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SheetCount.html)
[IEModelViewControl::SheetHeight Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SheetHeight.html)
[IEModelViewControl::SheetName Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SheetName.html)

## Availability

eDrawings API 2005 SP0
