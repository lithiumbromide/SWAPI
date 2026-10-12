---
title: "Application Property (ISwDMConfiguration)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration"
member: "Application"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~Application.html"
---

# Application Property (ISwDMConfiguration)

Gets the application for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Application As SwDMApplication
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration
Dim value As SwDMApplication

value = instance.Application
```

### C#

```csharp
SwDMApplication Application {get;}
```

### C++/CLI

```cpp
property SwDMApplication^ Application {
   SwDMApplication^ get();
}
```

### Property Value

Pointer to the [ISwDMApplication](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMApplication.html) object

## VBA Syntax

See [SwDMConfiguration::Application](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration~Application.html).

## See Also

[ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.html)
[ISwDMConfiguration Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
