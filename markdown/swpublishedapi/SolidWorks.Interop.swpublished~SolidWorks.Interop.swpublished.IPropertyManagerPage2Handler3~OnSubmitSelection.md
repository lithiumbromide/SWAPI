---
title: "OnSubmitSelection Method (IPropertyManagerPage2Handler3)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler3"
member: "OnSubmitSelection"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler3~OnSubmitSelection.html"
---

# OnSubmitSelection Method (IPropertyManagerPage2Handler3)

Obsolete. Superseded by [IPropertyManagerPage2Handler5::OnSubmitSelection](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler5~OnSubmitSelection.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function OnSubmitSelection( _
   ByVal Id As System.Integer, _
   ByVal Selection As System.Object, _
   ByVal SelType As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler3
Dim Id As System.Integer
Dim Selection As System.Object
Dim SelType As System.Integer
Dim value As System.Boolean

value = instance.OnSubmitSelection(Id, Selection, SelType)
```

### C#

```csharp
System.bool OnSubmitSelection(
   System.int Id,
   System.object Selection,
   System.int SelType
)
```

### C++/CLI

```cpp
System.bool OnSubmitSelection(
   System.int Id,
   System.Object^ Selection,
   System.int SelType
)
```

### Parameters

- `Id`:
- `Selection`:
- `SelType`:

## VBA Syntax

See [PropertyManagerPage2Handler3::OnSubmitSelection](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler3~OnSubmitSelection.html).

## See Also

[IPropertyManagerPage2Handler3 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler3.html)
[IPropertyManagerPage2Handler3 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler3_members.html)
