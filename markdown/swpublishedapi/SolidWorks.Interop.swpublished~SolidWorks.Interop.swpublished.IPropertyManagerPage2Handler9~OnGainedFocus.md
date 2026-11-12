---
title: "OnGainedFocus Method (IPropertyManagerPage2Handler9)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler9"
member: "OnGainedFocus"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnGainedFocus.html"
---

# OnGainedFocus Method (IPropertyManagerPage2Handler9)

Called when a control (edit box, combo box, list box, or number box) gains focus on this PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnGainedFocus( _
   ByVal Id As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler9
Dim Id As System.Integer

instance.OnGainedFocus(Id)
```

### C#

```csharp
void OnGainedFocus(
   System.int Id
)
```

### C++/CLI

```cpp
void OnGainedFocus(
   System.int Id
)
```

### Parameters

- `Id`: ID of the control that gained focus

## VBA Syntax

See [PropertyManagerPage2Handler9::OnGainedFocus](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler9~OnGainedFocus.html).

## Examples

See the [IPropertyManagerPage2Handler9](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html) examples.

## Remarks

To handle selection box focus, use [IPropertyManagerPage2Handler9::OnSelectionboxFocusChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnSelectionboxFocusChanged.html).

## See Also

[IPropertyManagerPage2Handler9 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html)
[IPropertyManagerPage2Handler9 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9_members.html)
[IPropertyManagerPage2Handler9::OnLostFocus Method](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnLostFocus.html)
