---
title: "CoCreateInstance Method (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "CoCreateInstance"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CoCreateInstance.html"
---

# CoCreateInstance Method (IEModelViewControl)

Creates an instance of an eDrawings add-in object, such as [IEModelViewMarkupControl](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CoCreateInstance( _
   ByVal CLSIDString As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim CLSIDString As System.String
Dim value As System.Object

value = instance.CoCreateInstance(CLSIDString)
```

### C#

```csharp
System.object CoCreateInstance(
   System.string CLSIDString
)
```

### C++/CLI

```cpp
System.Object^ CoCreateInstance(
   System.String^ CLSIDString
)
```

### Parameters

- `CLSIDString`: Class ID for an eDrawings add-in

### Return Value

Pointer to the add-in object

## VBA Syntax

See [EModelViewControl::CoCreateInstance](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~CoCreateInstance.html).

## Examples

```vb
Dim m_Markup as EModelViewMarkup.EModelMarkupControl
Set m_Markup = EModelViewControl1.CoCreateInstance("EModelViewMarkup.EmodelMarkupControl")
See IEModelViewControl examples.
```

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2005 SP0
