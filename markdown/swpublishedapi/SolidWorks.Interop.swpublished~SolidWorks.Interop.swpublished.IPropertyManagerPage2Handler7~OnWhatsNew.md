---
title: "OnWhatsNew Method (IPropertyManagerPage2Handler7)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler7"
member: "OnWhatsNew"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7~OnWhatsNew.html"
---

# OnWhatsNew Method (IPropertyManagerPage2Handler7)

Obsoleted. Superseded by [IPropertyManagerPage2Handler8::OnWhatsNew](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnWhatsNew.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnWhatsNew()
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler7

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

See [PropertyManagerPage2Handler7::OnWhatsNew](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler7~OnWhatsNew.html).

## Remarks

Your add-in must implement this method.

When a user clicks the What's New button on this PropertyManager page, the appropriate What's New Help topic is displayed. Use [ISldWorks::ShowHelp](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ShowHelp.html) to display the What's New Help topic.

## See Also

[IPropertyManagerPage2Handler7 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7.html)
[IPropertyManagerPage2Handler7 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
