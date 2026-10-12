---
title: "OnCheckboxCheck Method (IPropertyManagerPage2Handler5)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler5"
member: "OnCheckboxCheck"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5~OnCheckboxCheck.html"
---

# OnCheckboxCheck Method (IPropertyManagerPage2Handler5)

Obsoleted. Superseded by [IPropertyManagerPage2Handler6::OnCheckboxCheck](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler6~OnCheckboxCheck.html).

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
Dim instance As IPropertyManagerPage2Handler5
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

See [PropertyManagerPage2Handler5::OnCheckboxCheck](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler5~OnCheckboxCheck.html).

## See Also

[IPropertyManagerPage2Handler5 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5.html)
[IPropertyManagerPage2Handler5 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
