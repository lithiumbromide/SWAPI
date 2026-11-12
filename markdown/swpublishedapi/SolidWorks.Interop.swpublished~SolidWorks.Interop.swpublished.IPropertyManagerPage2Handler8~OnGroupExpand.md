---
title: "OnGroupExpand Method (IPropertyManagerPage2Handler8)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler8"
member: "OnGroupExpand"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8~OnGroupExpand.html"
---

# OnGroupExpand Method (IPropertyManagerPage2Handler8)

Obsolete. Superseded by [IPropertyManagerPage2Handler9::OnGroupExpand](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnGroupExpand.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnGroupExpand( _
   ByVal Id As System.Integer, _
   ByVal Expanded As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler8
Dim Id As System.Integer
Dim Expanded As System.Boolean

instance.OnGroupExpand(Id, Expanded)
```

### C#

```csharp
void OnGroupExpand(
   System.int Id,
   System.bool Expanded
)
```

### C++/CLI

```cpp
void OnGroupExpand(
   System.int Id,
   System.bool Expanded
)
```

### Parameters

- `Id`: ID of the arrow that opens a group box
- `Expanded`: True if the group box is opened, false if not

## VBA Syntax

See [PropertyManagerPage2Handler8::OnGroupExpand](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler8~OnGroupExpand.html).

## See Also

[IPropertyManagerPage2Handler8 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8.html)
[IPropertyManagerPage2Handler8 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
