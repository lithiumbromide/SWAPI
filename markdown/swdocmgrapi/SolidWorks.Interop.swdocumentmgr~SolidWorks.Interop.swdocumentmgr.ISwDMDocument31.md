---
title: "ISwDMDocument31 Interface"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument31"
member: ""
kind: "interface"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument31.html"
---

# ISwDMDocument31 Interface

Accesses the document.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwDMDocument31
   Inherits ISwDMDocument, ISwDMDocument10, ISwDMDocument12, ISwDMDocument13, ISwDMDocument14, ISwDMDocument15, ISwDMDocument16, ISwDMDocument17, ISwDMDocument18, ISwDMDocument19, ISwDMDocument20, ISwDMDocument21, ISwDMDocument22, ISwDMDocument23, ISwDMDocument24, ISwDMDocument25, ISwDMDocument26, ISwDMDocument27, ISwDMDocument28, ISwDMDocument29, ISwDMDocument3, ISwDMDocument30, ISwDMDocument4, ISwDMDocument5, ISwDMDocument6, ISwDMDocument7, ISwDMDocument8
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument31
```

### C#

```csharp
public interface ISwDMDocument31 : ISwDMDocument, ISwDMDocument10, ISwDMDocument12, ISwDMDocument13, ISwDMDocument14, ISwDMDocument15, ISwDMDocument16, ISwDMDocument17, ISwDMDocument18, ISwDMDocument19, ISwDMDocument20, ISwDMDocument21, ISwDMDocument22, ISwDMDocument23, ISwDMDocument24, ISwDMDocument25, ISwDMDocument26, ISwDMDocument27, ISwDMDocument28, ISwDMDocument29, ISwDMDocument3, ISwDMDocument30, ISwDMDocument4, ISwDMDocument5, ISwDMDocument6, ISwDMDocument7, ISwDMDocument8
```

### C++/CLI

```cpp
public interface class ISwDMDocument31 : public ISwDMDocument, ISwDMDocument10, ISwDMDocument12, ISwDMDocument13, ISwDMDocument14, ISwDMDocument15, ISwDMDocument16, ISwDMDocument17, ISwDMDocument18, ISwDMDocument19, ISwDMDocument20, ISwDMDocument21, ISwDMDocument22, ISwDMDocument23, ISwDMDocument24, ISwDMDocument25, ISwDMDocument26, ISwDMDocument27, ISwDMDocument28, ISwDMDocument29, ISwDMDocument3, ISwDMDocument30, ISwDMDocument4, ISwDMDocument5, ISwDMDocument6, ISwDMDocument7, ISwDMDocument8
```

## VBA Syntax

See [SwDMDocument31](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument31.html).

## Remarks

Before you can access this object, you must call [ISwDMApplication::GetDocument](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMApplication~GetDocument.html).

NOTES:

- You can access an ISwDMDocument31 object by calling QueryInterface on an [ISwDMDocument](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument.html) object in C++ or by direct assignment in Visual Basic.
- The SwDMDocument object can be assigned to an ISwDMDocument31 variable, just like the SOLIDWORKS [IModelDoc2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object can be assigned to a SOLIDWORKS [IPartDoc](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html) variable.

## Accessors

[ISwDMApplication::GetDocument](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMApplication~GetDocument.html)

[ISwDMConfiguration::Document](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration~Document.html)

[ISwDMConfigurationMgr::Document](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfigurationMgr~Document.html)

## See Also

[ISwDMDocument31 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument31_members.html)
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
[ISwDMDocument30 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument30.html)
[ISwDMDocument29 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument29.html)
[ISwDMDocument28 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument28.html)
[ISwDMDocument27 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument27.html)
[ISwDMDocument26 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument26.html)
[ISwDMDocument25 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument25.html)
[ISwDMDocument24 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument24.html)
[ISwDMDocument23 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument23.html)
[ISwDMDocument22 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument22.html)
[ISwDMDocument21 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument21.html)
[ISwDMDocument20 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument20.html)
[ISwDMDocument19 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument19.html)
[ISwDMDocument18 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument18.html)
[ISwDMDocument17 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument17.html)
[ISwDMDocument16 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument16.html)
[ISwDMDocument15 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15.html)
[ISwDMDocument14 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument14.html)
[ISwDMDocument13 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13.html)
[ISwDMDocument12 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument12.html)
[ISwDMDocument11 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument11.html)
[ISwDMDocument10 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10.html)
[ISwDMDocument8 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8.html)
[ISwDMDocument7 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument7.html)
[ISwDMDocument6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument6.html)
[ISwDMDocument5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5.html)
[ISwDMDocument4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument4.html)
[ISwDMDocument3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument3.html)
[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
