---
title: "OnSelectionboxFocusChanged Method (IPropertyManagerPage2Handler7)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler7"
member: "OnSelectionboxFocusChanged"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7~OnSelectionboxFocusChanged.html"
---

# OnSelectionboxFocusChanged Method (IPropertyManagerPage2Handler7)

Obsoleted. Superseded by [IPropertyManagerPage2Handler8::OnSelectionboxFocusChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnSelectionboxFocusChanged.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnSelectionboxFocusChanged( _
   ByVal Id As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler7
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

- `Id`: ID of the selection box with focus

## VBA Syntax

See [PropertyManagerPage2Handler7::OnSelectionboxFocusChanged](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler7~OnSelectionboxFocusChanged.html).

## Remarks

A PropertyManager page often has more than one selection list. The focus is always on the active selection list. When the focus changes to another selection list, this subroutine is called. If there is only one selection list on the page, then the focus never leaves it, and this subroutine is never called.

## See Also

[IPropertyManagerPage2Handler7 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7.html)
[IPropertyManagerPage2Handler7 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
