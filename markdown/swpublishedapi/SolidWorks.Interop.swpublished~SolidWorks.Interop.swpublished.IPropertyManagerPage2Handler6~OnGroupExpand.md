---
title: "OnGroupExpand Method (IPropertyManagerPage2Handler6)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler6"
member: "OnGroupExpand"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler6~OnGroupExpand.html"
---

# OnGroupExpand Method (IPropertyManagerPage2Handler6)

Obsoleted. Superseded by [IPropertyManagerPage2Handler7::OnGroupExpand](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler7~OnGroupExpand.html).

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
Dim instance As IPropertyManagerPage2Handler6
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

- `Id`: ID of the arrow that open a group box
- `Expanded`: True if the group box is opened, false if not

## VBA Syntax

See [PropertyManagerPage2Handler6::OnGroupExpand](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler6~OnGroupExpand.html).

## See Also

[IPropertyManagerPage2Handler6 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler6.html)
[IPropertyManagerPage2Handler6 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler6_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
