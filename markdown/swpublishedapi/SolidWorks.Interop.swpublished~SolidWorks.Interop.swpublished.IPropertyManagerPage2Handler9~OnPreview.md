---
title: "OnPreview Method (IPropertyManagerPage2Handler9)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler9"
member: "OnPreview"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnPreview.html"
---

# OnPreview Method (IPropertyManagerPage2Handler9)

Called when a user clicks the Preview button on a PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Function OnPreview() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler9
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

See [PropertyManagerPage2Handler9::OnPreview](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler9~OnPreview.html).

## Examples

See the [IPropertyManagerPage2Handler9](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html) examples.

## Remarks

To show a Preview button on a PropertyManager page, include swPropertyManagerOptions_PreviewButton in the Options argument of [ISldWorks::CreatePropertyManagerPage](ms-its:sldworksapi.chm::/Solidworks.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~CreatePropertyManagerPage.html) or [ISldWorks::ICreatePropertyManagerPage](ms-its:sldworksapi.chm::/Solidworks.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ICreatePropertyManagerPage.html).

You can do whatever you want in response to the Preview button being clicked. Your add-in is responsible for preview handling, including keeping track of the state of the Preview button. Your add-in controls what happens when the Preview button is clicked; SOLIDWORKS takes not action when the Preview button is clicked. SOLIDWORKS ignores the return value because by the time the callback handler is called, the button has already changed.

## See Also

[IPropertyManagerPage2Handler9 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html)
[IPropertyManagerPage2Handler9 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
