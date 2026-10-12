---
title: "OnRedo Method (IPropertyManagerPage2Handler7)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler7"
member: "OnRedo"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7~OnRedo.html"
---

# OnRedo Method (IPropertyManagerPage2Handler7)

Obsoleted. Superseded by [IPropertyManagerPage2Handler8::OnRedo](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnRedo.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnRedo()
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler7

instance.OnRedo()
```

### C#

```csharp
void OnRedo()
```

### C++/CLI

```cpp
void OnRedo();
```

## VBA Syntax

See [PropertyManagerPage2Handler7::OnRedo](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler7~OnRedo.html).

## Remarks

You control the Redo button using [IPropertyManagerPage2::EnableButton](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~EnableButton.html) and specifying swPropertyManagerPageButton_Redo for WhichOne.

## See Also

[IPropertyManagerPage2Handler7 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7.html)
[IPropertyManagerPage2Handler7 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
