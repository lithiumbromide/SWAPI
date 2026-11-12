---
title: "OnSelectionboxFocusChanged Method (IPropertyManagerPage2Handler8)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler8"
member: "OnSelectionboxFocusChanged"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8~OnSelectionboxFocusChanged.html"
---

# OnSelectionboxFocusChanged Method (IPropertyManagerPage2Handler8)

Obsolete. Superseded by [IPropertyManagerPage2Handler9::OnSelectionboxFocusChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnSelectionboxFocusChanged.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnSelectionboxFocusChanged( _
   ByVal Id As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler8
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

See [PropertyManagerPage2Handler8::OnSelectionboxFocusChanged](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler8~OnSelectionboxFocusChanged.html).

## Remarks

A PropertyManager page often has more than one selection list. The focus is always on the active selection list. When the focus changes to another selection list, this subroutine is called. If there is only one selection list on the page, then the focus never leaves it, and this subroutine is never called.

## See Also

[IPropertyManagerPage2Handler8 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8.html)
[IPropertyManagerPage2Handler8 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
