---
title: "OnTextboxChanged Method (IPropertyManagerPage2Handler5)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler5"
member: "OnTextboxChanged"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5~OnTextboxChanged.html"
---

# OnTextboxChanged Method (IPropertyManagerPage2Handler5)

Obsoleted. Superseded by [IPropertyManagerPage2Handler6::OnTextboxChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler6~OnTextboxChanged.html).

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
Dim instance As IPropertyManagerPage2Handler5
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

- `Id`: ID of text box
- `Text`: Text string

## VBA Syntax

See [PropertyManagerPage2Handler5::OnTextboxChanged](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler5~OnTextboxChanged.html).

## See Also

[IPropertyManagerPage2Handler5 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5.html)
[IPropertyManagerPage2Handler5 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
