---
title: "OnWhatsNew Method (IPropertyManagerPage2Handler9)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler9"
member: "OnWhatsNew"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnWhatsNew.html"
---

# OnWhatsNew Method (IPropertyManagerPage2Handler9)

Called when a user clicks the What's New button on this PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnWhatsNew()
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler9

instance.OnWhatsNew()
```

### C#

```csharp
void OnWhatsNew()
```

### C++/CLI

```cpp
void OnWhatsNew();
```

## VBA Syntax

See [PropertyManagerPage2Handler9::OnWhatsNew](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler9~OnWhatsNew.html).

## Examples

See the [IPropertyManagerPage2Handler9](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html) examples.

## Remarks

Your add-in must implement this method.

When a user clicks the What's New button on this PropertyManager page, the appropriate What's New Help topic is displayed. Use [ISldWorks::ShowHelp](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ShowHelp.html) to display the What's New Help topic.

## See Also

[IPropertyManagerPage2Handler9 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html)
[IPropertyManagerPage2Handler9 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
