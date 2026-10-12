---
title: "ISwDMDocument12 Interface"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument12"
member: ""
kind: "interface"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument12.html"
---

# ISwDMDocument12 Interface

Obsolete.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwDMDocument12
   Inherits ISwDMDocument, ISwDMDocument10, ISwDMDocument3, ISwDMDocument4, ISwDMDocument5, ISwDMDocument6, ISwDMDocument7, ISwDMDocument8
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument12
```

### C#

```csharp
public interface ISwDMDocument12 : ISwDMDocument, ISwDMDocument10, ISwDMDocument3, ISwDMDocument4, ISwDMDocument5, ISwDMDocument6, ISwDMDocument7, ISwDMDocument8
```

### C++/CLI

```cpp
public interface class ISwDMDocument12 : public ISwDMDocument, ISwDMDocument10, ISwDMDocument3, ISwDMDocument4, ISwDMDocument5, ISwDMDocument6, ISwDMDocument7, ISwDMDocument8
```

## VBA Syntax

See [SwDMDocument12](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument12.html).

## Remarks

Before you can access this object, you must call [ISwDMApplication::GetDocument](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMApplication~GetDocument.html).

NOTES:

- You can access an ISwDMDocument12 object by calling QueryInterface on an [ISwDMDocument](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument.html) object in C++ or by direct assignment in Visual Basic.
- The SwDMDocument object can be assigned to an ISwDMDocument12 variable, just like the SOLIDWORKS [IModelDoc2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object can be assigned to a SOLIDWORKS [IPartDoc](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html) variable.

## Accessors

[ISwDMApplication::GetDocument](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMApplication~GetDocument.html)

[ISwDMConfiguration::Document](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration~Document.html)

[ISwDMConfigurationMgr::Document](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfigurationMgr~Document.html)

## See Also

[ISwDMDocument12 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument12_members.html)
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
