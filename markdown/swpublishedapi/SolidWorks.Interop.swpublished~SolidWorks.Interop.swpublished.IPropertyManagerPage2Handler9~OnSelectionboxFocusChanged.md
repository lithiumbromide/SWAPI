---
title: "OnSelectionboxFocusChanged Method (IPropertyManagerPage2Handler9)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler9"
member: "OnSelectionboxFocusChanged"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnSelectionboxFocusChanged.html"
---

# OnSelectionboxFocusChanged Method (IPropertyManagerPage2Handler9)

Indicates that the active selection list box has changed.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnSelectionboxFocusChanged( _
   ByVal Id As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler9
Dim Id As System.Integer

instance.OnSelectionboxFocusChanged(Id)
```

### C#

```csharp
void OnSelectionboxFocusChanged(
   System.int Id
)
```

### C++/CLI

```cpp
void OnSelectionboxFocusChanged(
   System.int Id
)
```

### Parameters

- `Id`: ID of this selection box with focus

## VBA Syntax

See [PropertyManagerPage2Handler9::OnSelectionboxFocusChanged](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler9~OnSelectionboxFocusChanged.html).

## Examples

See the [IPropertyManagerPage2Handler9](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html) examples.

## Remarks

A PropertyManager page often has more than one selection list. The focus is always on the active selection list. When the focus changes to another selection list, this method is called. If there is only one selection list on the page, then the focus never leaves it and this method is never called.

## See Also

[IPropertyManagerPage2Handler9 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html)
[IPropertyManagerPage2Handler9 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
