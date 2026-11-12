---
title: "OnTextboxChanged Method (IPropertyManagerPage2Handler9)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler9"
member: "OnTextboxChanged"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnTextboxChanged.html"
---

# OnTextboxChanged Method (IPropertyManagerPage2Handler9)

Called when a user changes the string in a text box on this PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnTextboxChanged( _
   ByVal Id As System.Integer, _
   ByVal Text As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler9
Dim Id As System.Integer
Dim Text As System.String

instance.OnTextboxChanged(Id, Text)
```

### C#

```csharp
void OnTextboxChanged(
   System.int Id,
   System.string Text
)
```

### C++/CLI

```cpp
void OnTextboxChanged(
   System.int Id,
   System.String^ Text
)
```

### Parameters

- `Id`: ID of the text box
- `Text`: Text string

## VBA Syntax

See [PropertyManagerPage2Handler9::OnTextboxChanged](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler9~OnTextboxChanged.html).

## Examples

See the [IPropertyManagerPage2Handler9](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html) examples.

## See Also

[IPropertyManagerPage2Handler9 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html)
[IPropertyManagerPage2Handler9 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
