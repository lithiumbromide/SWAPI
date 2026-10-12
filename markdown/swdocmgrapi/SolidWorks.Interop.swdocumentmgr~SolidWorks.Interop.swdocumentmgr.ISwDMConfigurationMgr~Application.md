---
title: "Application Property (ISwDMConfigurationMgr)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfigurationMgr"
member: "Application"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr~Application.html"
---

# Application Property (ISwDMConfigurationMgr)

Gets the [ISwDMApplication](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMApplication.html) object.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Application As SwDMApplication
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfigurationMgr
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

See [SwDMConfigurationMgr::Application](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfigurationMgr~Application.html).

## See Also

[ISwDMConfigurationMgr Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr.html)
[ISwDMConfigurationMgr Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
