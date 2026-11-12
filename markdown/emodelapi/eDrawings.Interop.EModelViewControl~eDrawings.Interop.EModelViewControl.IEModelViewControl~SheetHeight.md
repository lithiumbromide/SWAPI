---
title: "SheetHeight Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "SheetHeight"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SheetHeight.html"
---

# SheetHeight Property (IEModelViewControl)

Gets the height of the drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SheetHeight As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Double

value = instance.SheetHeight
```

### C#

```csharp
System.double SheetHeight {get;}
```

### C++/CLI

```cpp
property System.double SheetHeight {
   System.double get();
}
```

### Property Value

Height of drawing sheet in either inches or millimeters, depending on the regional settings of your computer, not the model units of the drawing

## VBA Syntax

See [EModelViewControl::SheetHeight](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~SheetHeight.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::ShowSheet Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowSheet.html)
[IEModelViewControl::SheetCount Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SheetCount.html)
[IEModelViewControl::SheetName Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SheetName.html)
[IEModelViewControl::SheetWidth Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SheetWidth.html)
[IEModelViewControl::CurrentSheetIndex Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CurrentSheetIndex.html)

## Availability

eDrawings API 2005 SP0
