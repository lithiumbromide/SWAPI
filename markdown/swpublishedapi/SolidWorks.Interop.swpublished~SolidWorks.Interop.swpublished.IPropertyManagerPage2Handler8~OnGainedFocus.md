---
title: "OnGainedFocus Method (IPropertyManagerPage2Handler8)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler8"
member: "OnGainedFocus"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8~OnGainedFocus.html"
---

# OnGainedFocus Method (IPropertyManagerPage2Handler8)

Obsolete. Superseded by [IPropertyManagerPage2Handler9::OnGainedFocus](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnGainedFocus.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnGainedFocus( _
   ByVal Id As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler8
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

See [PropertyManagerPage2Handler8::OnGainedFocus](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler8~OnGainedFocus.html).

## Remarks

To handle selection box focus, use [IPropertyManagerPage2Handler8::OnSelectionboxFocusChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnSelectionboxFocusChanged.html).

## See Also

[IPropertyManagerPage2Handler8 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8.html)
[IPropertyManagerPage2Handler8 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
