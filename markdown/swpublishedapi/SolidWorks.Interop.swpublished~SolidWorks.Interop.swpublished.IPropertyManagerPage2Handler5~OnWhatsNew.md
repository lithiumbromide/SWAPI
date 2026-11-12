---
title: "OnWhatsNew Method (IPropertyManagerPage2Handler5)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler5"
member: "OnWhatsNew"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5~OnWhatsNew.html"
---

# OnWhatsNew Method (IPropertyManagerPage2Handler5)

Obsoleted. Superseded by [IPropertyManagerPage2Handler6::OnWhatsNew](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler6~OnWhatsNew.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnWhatsNew()
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler5

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

See [PropertyManagerPage2Handler5::OnWhatsNew](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler5~OnWhatsNew.html).

## Remarks

Your add-in must implement this method.

When a user clicks the What's New button on this PropertyManager page, the appropriate What's New Help topic is displayed. Use [ISldWorks::ShowHelp](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ShowHelp.html) to display the What's New Help topic.

## See Also

[IPropertyManagerPage2Handler5 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5.html)
[IPropertyManagerPage2Handler5 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
