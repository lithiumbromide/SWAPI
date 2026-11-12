---
title: "OnGainedFocus Method (IPropertyManagerPage2Handler7)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler7"
member: "OnGainedFocus"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7~OnGainedFocus.html"
---

# OnGainedFocus Method (IPropertyManagerPage2Handler7)

Obsoleted. Superseded by [IPropertyManagerPage2Handler8::OnGainedFocus](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnGainedFocus.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnGainedFocus( _
   ByVal Id As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler7
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

See [PropertyManagerPage2Handler7::OnGainedFocus](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler7~OnGainedFocus.html).

## Remarks

To handle selection box focus, use [IPropertyManagerPage2Handler7::OnSelectionboxFocusChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler7~OnSelectionboxFocusChanged.html).

## See Also

[IPropertyManagerPage2Handler7 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7.html)
[IPropertyManagerPage2Handler7 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7_members.html)
[IPropertyManagerPage2Handler7::OnLostFocus Method](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7~OnLostFocus.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
