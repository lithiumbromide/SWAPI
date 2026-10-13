---
title: "EnableFeatures Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "EnableFeatures"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~EnableFeatures.html"
---

# EnableFeatures Property (IEModelViewControl)

Gets or sets properties of the [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property EnableFeatures As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
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

Value of the bitmask as defined in [EMVEnableFeatures](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.EMVEnableFeatures.html)

## VBA Syntax

See [EModelViewControl::EnableFeatures](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~EnableFeatures.html).

## Remarks

You can only set this property at design time; you cannot set it at runtime. To set an individual property only, use [IEModelViewControl::EnableFeature](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~EnableFeature.html).

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2005 SP0
