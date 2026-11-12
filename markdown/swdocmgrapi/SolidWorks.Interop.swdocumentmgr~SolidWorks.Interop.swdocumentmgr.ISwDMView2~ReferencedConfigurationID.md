---
title: "ReferencedConfigurationID Property (ISwDMView2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMView2"
member: "ReferencedConfigurationID"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView2~ReferencedConfigurationID.html"
---

# ReferencedConfigurationID Property (ISwDMView2)

Gets the ID of the configuration for this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferencedConfigurationID As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMView2
Dim value As System.Integer

value = instance.ReferencedConfigurationID
```

### C#

```csharp
System.int ReferencedConfigurationID {get;}
```

### C++/CLI

```cpp
property System.int ReferencedConfigurationID {
   System.int get();
}
```

### Property Value

ID of configuration or -1 for legacy files (see **Remarks**)

## VBA Syntax

See [SwDMView2::ReferencedConfigurationID](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMView2~ReferencedConfigurationID.html).

## Remarks

This property works only with documents saved in SOLIDWORKS 2017 or later.

## See Also

[ISwDMView2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView2.html)
[ISwDMView2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView2_members.html)
[ISwDMView::ReferencedConfiguration Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView~ReferencedConfiguration.html)

## Availability

SOLIDWORKS Document Manager API 2017 FCS
