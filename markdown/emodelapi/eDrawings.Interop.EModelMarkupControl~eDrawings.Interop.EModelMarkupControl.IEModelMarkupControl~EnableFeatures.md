---
title: "EnableFeatures Property (IEModelMarkupControl)"
project: "eDrawings API Help"
interface: "IEModelMarkupControl"
member: "EnableFeatures"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~EnableFeatures.html"
---

# EnableFeatures Property (IEModelMarkupControl)

Gets or sets markup properties of the [IEModelMarkupControl](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property EnableFeatures As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelMarkupControl
Dim value As System.Integer

instance.EnableFeatures = value

value = instance.EnableFeatures
```

### C#

```csharp
System.int EnableFeatures {get; set;}
```

### C++/CLI

```cpp
property System.int EnableFeatures {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Value of the bitmask as defined by [EMVMarkupEnableFeatures](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.EMVMarkupEnableFeatures.html)

## VBA Syntax

See [EModelMarkupControl::EnableFeatures](ms-its:emodelapivb6.chm::/EModelViewMarkup~EModelMarkupControl~EnableFeatures.html).

## Remarks

You can only set this property at runtime; you cannot set it at design time.

To set an individual markup property only, use [IEModelMarkupControl::EnableFeature](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~EnableFeature.html).

## See Also

[IEModelMarkupControl Interface](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl.html)
[IEModelMarkupControl Members](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl_members.html)

## Availability

eDrawings API 2005 SP0
