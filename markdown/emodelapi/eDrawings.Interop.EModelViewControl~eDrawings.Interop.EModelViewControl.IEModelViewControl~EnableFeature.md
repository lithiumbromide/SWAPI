---
title: "EnableFeature Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "EnableFeature"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~EnableFeature.html"
---

# EnableFeature Property (IEModelViewControl)

Gets or sets a property of the [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property EnableFeature( _
   ByVal feature As EMVEnableFeatures _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim feature As EMVEnableFeatures
Dim value As System.Boolean

instance.EnableFeature(feature) = value

value = instance.EnableFeature(feature)
```

### C#

```csharp
System.bool EnableFeature(
   EMVEnableFeatures feature
) {get; set;}
```

### C++/CLI

```cpp
property System.bool EnableFeature {
   System.bool get(EMVEnableFeatures feature);
   void set (EMVEnableFeatures feature, System.bool value);
}
```

### Parameters

- `feature`: Property as defined in [EMVEnableFeatures](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.EMVEnableFeatures.html)

### Property Value

True if the property is set, false if not

## VBA Syntax

See [EModelViewControl::EnableFeature](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~EnableFeature.html).

## Examples

```vb
meEmv.EnableFeature(16) = True ' Sets a IEModelViewControl to Complete UI mode
meEmv.EnableFeature(16)        ' Gets the value of the property
```

## Remarks

You can only set this property at design time; you cannot set it at runtime. To set multiple properties at the same time, use [IEModelViewControl::EnableFeatures](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~EnableFeatures.html).

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2005 SP0
