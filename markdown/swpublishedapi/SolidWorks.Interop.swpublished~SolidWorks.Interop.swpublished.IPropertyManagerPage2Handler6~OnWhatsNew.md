---
title: "OnWhatsNew Method (IPropertyManagerPage2Handler6)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler6"
member: "OnWhatsNew"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler6~OnWhatsNew.html"
---

# OnWhatsNew Method (IPropertyManagerPage2Handler6)

Obsoleted. Superseded by [IPropertyManagerPage2Handler7::OnWhatsNew](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler7~OnWhatsNew.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnWhatsNew()
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler6

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

See [PropertyManagerPage2Handler6::OnWhatsNew](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler6~OnWhatsNew.html).

## Remarks

Your add-in must implement this method.

When a user clicks the What's New button on this PropertyManager page, the appropriate What's New Help topic is displayed. Use [ISldWorks::ShowHelp](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ShowHelp.html) to display the What's New Help topic.

## See Also

[IPropertyManagerPage2Handler6 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler6.html)
[IPropertyManagerPage2Handler6 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler6_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
