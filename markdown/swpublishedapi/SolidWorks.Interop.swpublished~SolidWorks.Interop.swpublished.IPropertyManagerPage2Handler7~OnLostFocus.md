---
title: "OnLostFocus Method (IPropertyManagerPage2Handler7)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler7"
member: "OnLostFocus"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7~OnLostFocus.html"
---

# OnLostFocus Method (IPropertyManagerPage2Handler7)

Obsoleted. Superseded by [IPropertyManagerPage2Handler8::OnLostFocus](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnLostFocus.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnLostFocus( _
   ByVal Id As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler7
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

See [PropertyManagerPage2Handler7::OnLostFocus](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler7~OnLostFocus.html).

## Remarks

To handle selection box focus, use [IPropertyManagerPage2Handler7::OnSelectionboxFocusChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler7~OnSelectionboxFocusChanged.html).

## See Also

[IPropertyManagerPage2Handler7 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7.html)
[IPropertyManagerPage2Handler7 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7_members.html)
[IPropertyManagerPage2Handler7::OnGainedFocus Method](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7~OnGainedFocus.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
