---
title: "MassProperty Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "MassProperty"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~MassProperty.html"
---

# MassProperty Property (IEModelViewControl)

Gets the value of the specified mass property.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MassProperty( _
   ByVal property As EMVMassProperty _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim property As EMVMassProperty
Dim value As System.Double

value = instance.MassProperty(property)
```

### C#

```csharp
System.double MassProperty(
   EMVMassProperty property
) {get;}
```

### C++/CLI

```cpp
property System.double MassProperty {
   System.double get(EMVMassProperty property);
}
```

### Parameters

- `property`: Type of mass property as defined in [EMVMassProperty](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.EMVMassProperty.html)

### Property Value

Value of mass property

## VBA Syntax

See [EModelViewControl::MassProperty](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~MassProperty.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2005 SP0
