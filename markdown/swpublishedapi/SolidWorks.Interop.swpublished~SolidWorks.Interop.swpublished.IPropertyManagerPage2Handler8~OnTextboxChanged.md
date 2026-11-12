---
title: "OnTextboxChanged Method (IPropertyManagerPage2Handler8)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler8"
member: "OnTextboxChanged"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8~OnTextboxChanged.html"
---

# OnTextboxChanged Method (IPropertyManagerPage2Handler8)

Obsolete. Superseded by [IPropertyManagerPage2Handler9::OnTextboxChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnTextboxChanged.html).

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
Dim instance As IPropertyManagerPage2Handler8
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

See [PropertyManagerPage2Handler8::OnTextboxChanged](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler8~OnTextboxChanged.html).

## See Also

[IPropertyManagerPage2Handler8 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8.html)
[IPropertyManagerPage2Handler8 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
