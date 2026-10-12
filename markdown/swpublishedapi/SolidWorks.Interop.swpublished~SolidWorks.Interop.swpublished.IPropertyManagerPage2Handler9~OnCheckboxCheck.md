---
title: "OnCheckboxCheck Method (IPropertyManagerPage2Handler9)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler9"
member: "OnCheckboxCheck"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnCheckboxCheck.html"
---

# OnCheckboxCheck Method (IPropertyManagerPage2Handler9)

Called when a user selects this check box on this PropertyManager page.

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
Dim instance As IPropertyManagerPage2Handler9
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

- `Id`: ID of the check box
- `Checked`: True if the check box is selected, false if not

## VBA Syntax

See [PropertyManagerPage2Handler9::OnCheckboxCheck](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler9~OnCheckboxCheck.html).

## Examples

See the [IPropertyManagerPage2Handler9](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html) examples.

## See Also

[IPropertyManagerPage2Handler9 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html)
[IPropertyManagerPage2Handler9 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
