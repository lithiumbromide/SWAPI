---
title: "OnCheckboxCheck Method (IPropertyManagerPage2Handler6)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler6"
member: "OnCheckboxCheck"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler6~OnCheckboxCheck.html"
---

# OnCheckboxCheck Method (IPropertyManagerPage2Handler6)

Obsoleted. Superseded by [IPropertyManagerPage2Handler7::OnCheckboxCheck](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler7~OnCheckboxCheck.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnCheckboxCheck( _
   ByVal Id As System.Integer, _
   ByVal Checked As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler6
Dim Id As System.Integer
Dim Checked As System.Boolean

instance.OnCheckboxCheck(Id, Checked)
```

### C#

```csharp
void OnCheckboxCheck(
   System.int Id,
   System.bool Checked
)
```

### C++/CLI

```cpp
void OnCheckboxCheck(
   System.int Id,
   System.bool Checked
)
```

### Parameters

- `Id`: ID of this check box
- `Checked`: True if the check box is selected, false if not

## VBA Syntax

See [PropertyManagerPage2Handler6::OnCheckboxCheck](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler6~OnCheckboxCheck.html).

## See Also

[IPropertyManagerPage2Handler6 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler6.html)
[IPropertyManagerPage2Handler6 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler6_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
