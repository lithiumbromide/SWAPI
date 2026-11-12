---
title: "OnGroupCheck Method (IPropertyManagerPage2Handler6)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler6"
member: "OnGroupCheck"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler6~OnGroupCheck.html"
---

# OnGroupCheck Method (IPropertyManagerPage2Handler6)

Obsoleted. Superseded by [IPropertyManagerPage2Handler7::OnGroupCheck](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler7~OnGroupCheck.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnGroupCheck( _
   ByVal Id As System.Integer, _
   ByVal Checked As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler6
Dim Id As System.Integer
Dim Checked As System.Boolean

instance.OnGroupCheck(Id, Checked)
```

### C#

```csharp
void OnGroupCheck(
   System.int Id,
   System.bool Checked
)
```

### C++/CLI

```cpp
void OnGroupCheck(
   System.int Id,
   System.bool Checked
)
```

### Parameters

- `Id`: Resource ID of the check box in title of the group box
- `Checked`: True if the check box in the title of the group box is selected, false if not

## VBA Syntax

See [PropertyManagerPage2Handler6::OnGroupCheck](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler6~OnGroupCheck.html).

## See Also

[IPropertyManagerPage2Handler6 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler6.html)
[IPropertyManagerPage2Handler6 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler6_members.html)
[IPropertyManagerPageGroup::Checked](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageGroup~Checked.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
