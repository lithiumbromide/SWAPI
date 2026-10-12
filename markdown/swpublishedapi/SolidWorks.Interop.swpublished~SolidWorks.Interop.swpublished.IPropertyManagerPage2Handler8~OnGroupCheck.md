---
title: "OnGroupCheck Method (IPropertyManagerPage2Handler8)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler8"
member: "OnGroupCheck"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8~OnGroupCheck.html"
---

# OnGroupCheck Method (IPropertyManagerPage2Handler8)

Obsolete. Superseded by [IPropertyManagerPage2Handler9::OnGroupCheck](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnGroupCheck.html).

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
Dim instance As IPropertyManagerPage2Handler8
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

- `Id`: Resource ID of the check box in the title of the group box
- `Checked`: True if the check box in the title of the group box is selected, false if not

## VBA Syntax

See [PropertyManagerPage2Handler8::OnGroupCheck](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler8~OnGroupCheck.html).

## See Also

[IPropertyManagerPage2Handler8 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8.html)
[IPropertyManagerPage2Handler8 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
