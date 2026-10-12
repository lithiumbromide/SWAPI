---
title: "MaterialPropertyName Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "MaterialPropertyName"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~MaterialPropertyName.html"
---

# MaterialPropertyName Property (IEModelViewControl)

Gets the material name.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MaterialPropertyName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.String

value = instance.MaterialPropertyName
```

### C#

```csharp
System.string MaterialPropertyName {get;}
```

### C++/CLI

```cpp
property System.String^ MaterialPropertyName {
   System.String^ get();
}
```

### Property Value

Name of material

## VBA Syntax

See [EModelViewControl::MaterialPropertyName](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~MaterialPropertyName.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## Remarks

If the material name is not available, the string <not specified> is returned.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2005 AP0
