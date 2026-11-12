---
title: "OnGroupExpand Method (IPropertyManagerPage2Handler5)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler5"
member: "OnGroupExpand"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5~OnGroupExpand.html"
---

# OnGroupExpand Method (IPropertyManagerPage2Handler5)

Obsoleted. Superseded by [IPropertyManagerPage2Handler6::OnGroupExpand](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler6~OnGroupExpand.html).

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
Dim instance As IPropertyManagerPage2Handler5
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

See [PropertyManagerPage2Handler5::OnGroupExpand](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler5~OnGroupExpand.html).

## See Also

[IPropertyManagerPage2Handler5 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5.html)
[IPropertyManagerPage2Handler5 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
