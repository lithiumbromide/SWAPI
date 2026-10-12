---
title: "OnNumberboxChanged Method (IPropertyManagerPage2Handler8)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler8"
member: "OnNumberboxChanged"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8~OnNumberboxChanged.html"
---

# OnNumberboxChanged Method (IPropertyManagerPage2Handler8)

Obsolete. Superseded by [IPropertyManagerPage2Handler9::OnNumberboxChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnNumberboxChanged.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnNumberboxChanged( _
   ByVal Id As System.Integer, _
   ByVal Value As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler8
Dim Id As System.Integer
Dim Value As System.Double

instance.OnNumberboxChanged(Id, Value)
```

### C#

```csharp
void OnNumberboxChanged(
   System.int Id,
   System.double Value
)
```

### C++/CLI

```cpp
void OnNumberboxChanged(
   System.int Id,
   System.double Value
)
```

### Parameters

- `Id`: ID of the number box
- `Value`: Number in the number box

## VBA Syntax

See [PropertyManagerPage2Handler8::OnNumberboxChanged](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler8~OnNumberboxChanged.html).

## See Also

[IPropertyManagerPage2Handler8 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8.html)
[IPropertyManagerPage2Handler8 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
