---
title: "OnListboxSelectionChanged Method (IPropertyManagerPage2Handler5)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler5"
member: "OnListboxSelectionChanged"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5~OnListboxSelectionChanged.html"
---

# OnListboxSelectionChanged Method (IPropertyManagerPage2Handler5)

Obsoleted. Superseded by [IPropertyManagerPage2Handler6::OnListboxSelectionChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler6~OnListboxSelectionChanged.html).

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
Dim instance As IPropertyManagerPage2Handler5
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

See [PropertyManagerPage2Handler5::OnListboxSelectionChanged](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler5~OnListboxSelectionChanged.html).

## See Also

[IPropertyManagerPage2Handler5 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5.html)
[IPropertyManagerPage2Handler5 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
