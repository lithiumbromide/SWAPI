---
title: "OnLostFocus Method (IPropertyManagerPage2Handler8)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler8"
member: "OnLostFocus"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8~OnLostFocus.html"
---

# OnLostFocus Method (IPropertyManagerPage2Handler8)

Obsolete. Superseded by [IPropertyManagerPage2Handler9::OnLostFocus](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnLostFocus.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnLostFocus( _
   ByVal Id As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler8
Dim Id As System.Integer

instance.OnLostFocus(Id)
```

### C#

```csharp
void OnLostFocus(
   System.int Id
)
```

### C++/CLI

```cpp
void OnLostFocus(
   System.int Id
)
```

### Parameters

- `Id`: ID of the control that lost focus

## VBA Syntax

See [PropertyManagerPage2Handler8::OnLostFocus](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler8~OnLostFocus.html).

## Remarks

To handle selection box focus, use [IPropertyManagerPage2Handler8::OnSelectionboxFocusChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnSelectionboxFocusChanged.html).

## See Also

[IPropertyManagerPage2Handler8 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8.html)
[IPropertyManagerPage2Handler8 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
