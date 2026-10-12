---
title: "AlwaysShowWarningWatermark Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "AlwaysShowWarningWatermark"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~AlwaysShowWarningWatermark.html"
---

# AlwaysShowWarningWatermark Property (IEModelViewControl)

Gets or sets whether to show a warning watermark when an existing file is opened.

## Syntax

### Visual Basic (Declaration)

```vb
Property AlwaysShowWarningWatermark As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Integer

instance.AlwaysShowWarningWatermark = value

value = instance.AlwaysShowWarningWatermark
```

### C#

```csharp
System.int AlwaysShowWarningWatermark {get; set;}
```

### C++/CLI

```cpp
property System.int AlwaysShowWarningWatermark {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

-1 to show a warning watermark, 0 to not show a warning watermark

## VBA Syntax

See [EModelViewControl::AlwaysShowWarningWatermark](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~AlwaysShowWarningWatermark.html).

## Remarks

eDrawings detects when the graphics data for a component might not be synchronized with a later version of the file that was modified and saved in a SOLIDWORKS assembly. When a potentially outdated component is opened, a watermark displays a warning and suggests that the part in the SOLIDWORKS software be rebuilt.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::OpenDoc Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~OpenDoc.html)

## Availability

eDrawings API 2012 SP0
