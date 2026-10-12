---
title: "Application Property (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "Application"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~Application.html"
---

# Application Property (ISwDMDocument)

Gets the application for this document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Application As SwDMApplication
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
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

See [SwDMDocument::Application](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~Application.html).

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
