---
title: "OnGroupCheck Method (IPropertyManagerPage2Handler9)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler9"
member: "OnGroupCheck"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnGroupCheck.html"
---

# OnGroupCheck Method (IPropertyManagerPage2Handler9)

Called when a user selects the check box in the title of a group box on a PropertyManager page.

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
Dim instance As IPropertyManagerPage2Handler9
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

See [PropertyManagerPage2Handler9::OnGroupCheck](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler9~OnGroupCheck.html).

## Examples

See the [IPropertyManagerPage2Handler9](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html) examples.

## See Also

[IPropertyManagerPage2Handler9 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html)
[IPropertyManagerPage2Handler9 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
