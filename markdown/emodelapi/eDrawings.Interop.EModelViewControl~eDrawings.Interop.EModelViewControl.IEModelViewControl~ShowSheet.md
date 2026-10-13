---
title: "ShowSheet Method (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "ShowSheet"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowSheet.html"
---

# ShowSheet Method (IEModelViewControl)

Displays the specified drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ShowSheet( _
   ByVal SheetIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim SheetIndex As System.Integer

instance.ShowSheet(SheetIndex)
```

### C#

```csharp
void ShowSheet(
   System.int SheetIndex
)
```

### C++/CLI

```cpp
void ShowSheet(
   System.int SheetIndex
)
```

### Parameters

- `SheetIndex`: Index number of the drawing sheet to display

## VBA Syntax

See [EModelViewControl::ShowSheet](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~ShowSheet.html).

## Remarks

Call [IEModelViewControl::CurrentSheetIndex](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CurrentSheetIndex.html) and [IEModelViewControl::SheetName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SheetName.html) to get the index number and name of a sheet to display.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::SheetCount Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SheetCount.html)
[IEModelViewControl::SheetHeight Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SheetHeight.html)
[IEModelViewControl::SheetName Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SheetName.html)
[IEModelViewControl::SheetWidth Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SheetWidth.html)
[IEModelViewControl::CurrentSheetIndex Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CurrentSheetIndex.html)

## Availability

eDrawings API 2005 SP0
