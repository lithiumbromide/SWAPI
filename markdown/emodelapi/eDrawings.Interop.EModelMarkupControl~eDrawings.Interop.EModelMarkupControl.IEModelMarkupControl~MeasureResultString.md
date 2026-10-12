---
title: "MeasureResultString Property (IEModelMarkupControl)"
project: "eDrawings API Help"
interface: "IEModelMarkupControl"
member: "MeasureResultString"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~MeasureResultString.html"
---

# MeasureResultString Property (IEModelMarkupControl)

Gets the most recent measurement results.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MeasureResultString As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelMarkupControl
Dim value As System.String

value = instance.MeasureResultString
```

### C#

```csharp
System.string MeasureResultString {get;}
```

### C++/CLI

```cpp
property System.String^ MeasureResultString {
   System.String^ get();
}
```

### Property Value

Most recent measurement results

## VBA Syntax

See [EModelViewControl::MeasureResultString](ms-its:emodelapivb6.chm::/EModelViewMarkup~EModelMarkupControl~MeasureResultString.html).

## See Also

[IEModelMarkupControl Interface](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl.html)
[IEModelMarkupControl Members](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl_members.html)
[IEModelMarkupControlEvents_OnMeasureResultsChangedEventHandler Delegate](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl._IEModelMarkupControlEvents_OnMeasureResultsChangedEventHandler.html)

## Availability

SOLIDWORKS eDrawings API 2010 SP0
