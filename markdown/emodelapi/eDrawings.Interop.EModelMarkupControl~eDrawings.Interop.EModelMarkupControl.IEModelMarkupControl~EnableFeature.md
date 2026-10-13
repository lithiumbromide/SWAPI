---
title: "EnableFeature Property (IEModelMarkupControl)"
project: "eDrawings API Help"
interface: "IEModelMarkupControl"
member: "EnableFeature"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~EnableFeature.html"
---

# EnableFeature Property (IEModelMarkupControl)

Gets or sets the specified markup property.

## Syntax

### Visual Basic (Declaration)

```vb
Property EnableFeature( _
   ByVal feature As EMVMarkupEnableFeatures _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelMarkupControl
Dim feature As EMVMarkupEnableFeatures
Dim value As System.Boolean

instance.EnableFeature(feature) = value

value = instance.EnableFeature(feature)
```

### C#

```csharp
System.bool EnableFeature(
   EMVMarkupEnableFeatures feature
) {get; set;}
```

### C++/CLI

```cpp
property System.bool EnableFeature {
   System.bool get(EMVMarkupEnableFeatures feature);
   void set (EMVMarkupEnableFeatures feature, System.bool value);
}
```

### Parameters

- `feature`: Markup property as defined in [EMVMarkupEnableFeatures](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.EMVMarkupEnableFeatures.html)

### Property Value

True if the markup property is set, false if not

## VBA Syntax

See [EModelMarkupControl::EnableFeature](ms-its:emodelapivb6.chm::/EModelViewMarkup~EModelMarkupControl~EnableFeature.html).

## Remarks

You can only set this property at runtime; you cannot set it at design time.

To set multiple markup properties at the same time, use [IEModelMarkupViewControl::EnableFeatures](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~EnableFeatures.html).

## See Also

[IEModelMarkupControl Interface](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl.html)
[IEModelMarkupControl Members](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl_members.html)

## Availability

eDrawings API 2005 SP0
