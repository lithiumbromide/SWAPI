---
title: "BackgroundImagePath Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "BackgroundImagePath"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~BackgroundImagePath.html"
---

# BackgroundImagePath Property (IEModelViewControl)

Gets the fully qualified path and file name of the background image.

## Syntax

### Visual Basic (Declaration)

```vb
Property BackgroundImagePath As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.String

instance.BackgroundImagePath = value

value = instance.BackgroundImagePath
```

### C#

```csharp
System.string BackgroundImagePath {get; set;}
```

### C++/CLI

```cpp
property System.String^ BackgroundImagePath {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Fully qualified path and file name of the background image

## VBA Syntax

See [EModelViewControl::BackgroundImagePath](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~BackgroundImagePath.html).

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::BackgroundColor Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~BackgroundColor.html)

## Availability

eDrawings API 2014 SP0
