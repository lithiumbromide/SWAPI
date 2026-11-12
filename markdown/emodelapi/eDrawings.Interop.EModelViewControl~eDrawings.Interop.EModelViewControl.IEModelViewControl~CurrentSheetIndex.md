---
title: "CurrentSheetIndex Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "CurrentSheetIndex"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CurrentSheetIndex.html"
---

# CurrentSheetIndex Property (IEModelViewControl)

Gets the index number of the currently displayed drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CurrentSheetIndex As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Integer

value = instance.CurrentSheetIndex
```

### C#

```csharp
System.int CurrentSheetIndex {get;}
```

### C++/CLI

```cpp
property System.int CurrentSheetIndex {
   System.int get();
}
```

### Property Value

Index of the currently displayed drawing sheet

## VBA Syntax

See [EModelViewControl::CurrentSheetIndex](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~CurrentSheetIndex.html).

## Remarks

This property returns a 0-based index number for the currently displayed sheet.

Call this property before calling [IEModelViewControl::SheetName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SheetName.html).

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::SheetCount Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SheetCount.html)
[IEModelViewControl::SheetHeight Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SheetHeight.html)
[IEModelViewControl::SheetWidth Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SheetWidth.html)
[IEModelViewControl::ShowSheet Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowSheet.html)

## Availability

eDrawings API 2005 SP0
