---
title: "OnGroupExpand Method (IPropertyManagerPage2Handler9)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler9"
member: "OnGroupExpand"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnGroupExpand.html"
---

# OnGroupExpand Method (IPropertyManagerPage2Handler9)

Called when a user clicks an arrow to open a group box on the PropertyManager page.

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
Dim instance As IPropertyManagerPage2Handler9
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

See [PropertyManagerPage2Handler9::OnGroupExpand](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler9~OnGroupExpand.html).

## Examples

See the [IPropertyManagerPage2Handler9](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html) examples.

## See Also

[IPropertyManagerPage2Handler9 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html)
[IPropertyManagerPage2Handler9 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9_members.html)

## Availability

SOLIDWORKS FCS 2012, Revision Number 20.0
