---
title: "OnPreview Method (IPropertyManagerPage2Handler8)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler8"
member: "OnPreview"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8~OnPreview.html"
---

# OnPreview Method (IPropertyManagerPage2Handler8)

Obsolete. Superseded by [IPropertyManagerPage2Handler9::OnPreview](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnPreview.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function OnPreview() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler8
Dim value As System.Boolean

value = instance.OnPreview()
```

### C#

```csharp
System.bool OnPreview()
```

### C++/CLI

```cpp
System.bool OnPreview();
```

### Return Value

True if the operations specified by your add-in executes, false if not (see Remarks)

## VBA Syntax

See [PropertyManagerPage2Handler8::OnPreview](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler8~OnPreview.html).

## Remarks

To show a Preview button on a PropertyManager page, include swPropertyManagerOptions_PreviewButton in the Options argument of [ISldWorks::CreatePropertyManagerPage](ms-its:sldworksapi.chm::/Solidworks.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~CreatePropertyManagerPage.html) or [ISldWorks::ICreatePropertyManagerPage](ms-its:sldworksapi.chm::/Solidworks.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ICreatePropertyManagerPage.html).

You can do whatever you want in response to the Preview button being clicked. Your add-in is responsible for preview handling, including keeping track of the state of the Preview button. Your add-in controls what happens when the Preview button is clicked; SOLIDWORKS takes not action when the Preview button is clicked. SOLIDWORKS ignores the return value because by the time the callback handler is called, the button has already changed.

## See Also

[IPropertyManagerPage2Handler8 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8.html)
[IPropertyManagerPage2Handler8 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
