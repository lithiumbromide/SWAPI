---
title: "ReferencedConfiguration Property (ISwDMView)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMView"
member: "ReferencedConfiguration"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView~ReferencedConfiguration.html"
---

# ReferencedConfiguration Property (ISwDMView)

Gets the name of the configuration for this drawing view.

**NOTE:** **This property is a get-only property. Set is not implemented.**

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferencedConfiguration As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMView
Dim value As System.String

instance.ReferencedConfiguration = value

value = instance.ReferencedConfiguration
```

### C#

```csharp
System.string ReferencedConfiguration {get; set;}
```

### C++/CLI

```cpp
property System.String^ ReferencedConfiguration {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of configuration

## VBA Syntax

See [SwDMView::ReferencedConfiguration](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMView~ReferencedConfiguration.html).

## See Also

[ISwDMView Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView.html)
[ISwDMView Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView_members.html)
[ISwDMView2::ReferencedConfigurationID Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMView2~ReferencedConfigurationID.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
