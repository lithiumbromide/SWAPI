---
title: "SheetName Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "SheetName"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SheetName.html"
---

# SheetName Property (IEModelViewControl)

Gets the name of the specified drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SheetName( _
   ByVal SheetIndex As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim SheetIndex As System.Integer
Dim value As System.String

value = instance.SheetName(SheetIndex)
```

### C#

```csharp
System.string SheetName(
   System.int SheetIndex
) {get;}
```

### C++/CLI

```cpp
property System.String^ SheetName {
   System.String^ get(System.int SheetIndex);
}
```

### Parameters

- `SheetIndex`: Index number of the drawing sheet to get

### Property Value

Name of the drawing sheet

## VBA Syntax

See [EModelViewControl::SheetName](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~SheetName.html).

## Remarks

Call [IEModelViewControl::CurrentSheetIndex](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CurrentSheetIndex.html) to get the index number of the currently displayed sheet.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::SheetCount Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SheetCount.html)
[IEModelViewControl::SheetHeight Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SheetHeight.html)
[IEModelViewControl::SheetWidth Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~SheetWidth.html)
[IEModelViewControl::ShowSheet Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowSheet.html)

## Availability

eDrawings API 2005 SP0
