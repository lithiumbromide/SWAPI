---
title: "OnCheckboxCheck Method (IPropertyManagerPage2Handler8)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler8"
member: "OnCheckboxCheck"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8~OnCheckboxCheck.html"
---

# OnCheckboxCheck Method (IPropertyManagerPage2Handler8)

Obsolete. Superseded by [IPropertyManagerPage2Handler9::OnCheckboxCheck](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnCheckboxCheck.html).

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
Dim instance As IPropertyManagerPage2Handler8
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

See [PropertyManagerPage2Handler8::OnCheckboxCheck](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler8~OnCheckboxCheck.html).

## See Also

[IPropertyManagerPage2Handler8 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8.html)
[IPropertyManagerPage2Handler8 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
