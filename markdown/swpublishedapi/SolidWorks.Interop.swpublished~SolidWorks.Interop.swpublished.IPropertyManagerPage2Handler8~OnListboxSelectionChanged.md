---
title: "OnListboxSelectionChanged Method (IPropertyManagerPage2Handler8)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler8"
member: "OnListboxSelectionChanged"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8~OnListboxSelectionChanged.html"
---

# OnListboxSelectionChanged Method (IPropertyManagerPage2Handler8)

Obsolete. Superseded by [IPropertyManagerPage2Handler9::OnListboxSelectionChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnListboxSelectionChanged.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnListboxSelectionChanged( _
   ByVal Id As System.Integer, _
   ByVal Item As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler8
Dim Id As System.Integer
Dim Item As System.Integer

instance.OnListboxSelectionChanged(Id, Item)
```

### C#

```csharp
void OnListboxSelectionChanged(
   System.int Id,
   System.int Item
)
```

### C++/CLI

```cpp
void OnListboxSelectionChanged(
   System.int Id,
   System.int Item
)
```

### Parameters

- `Id`: ID of the list box
- `Item`: ID of the item

## VBA Syntax

See [PropertyManagerPage2Handler8::OnListboxSelectionChanged](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler8~OnListboxSelectionChanged.html).

## See Also

[IPropertyManagerPage2Handler8 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8.html)
[IPropertyManagerPage2Handler8 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
