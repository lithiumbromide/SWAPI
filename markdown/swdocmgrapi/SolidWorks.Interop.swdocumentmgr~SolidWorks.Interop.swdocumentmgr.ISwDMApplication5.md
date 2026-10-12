---
title: "ISwDMApplication5 Interface"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMApplication5"
member: ""
kind: "interface"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication5.html"
---

# ISwDMApplication5 Interface

Manages part, assembly, or drawing documents.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwDMApplication5
   Inherits ISwDMApplication, ISwDMApplication2, ISwDMApplication3, ISwDMApplication4
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMApplication5
```

### C#

```csharp
public interface ISwDMApplication5 : ISwDMApplication, ISwDMApplication2, ISwDMApplication3, ISwDMApplication4
```

### C++/CLI

```cpp
public interface class ISwDMApplication5 : public ISwDMApplication, ISwDMApplication2, ISwDMApplication3, ISwDMApplication4
```

## VBA Syntax

See [SwDMApplication5](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMApplication5.html).

## Remarks

- You can access an SwDMApplication5 object by calling QueryInterface on an [ISwDMApplication](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMApplication.html) object in C++ or by direct assignment in Visual Basic.
- The SwDMApplication object can be assigned to a SwDMApplication5 variable, just like the SOLIDWORKS [IModelDoc2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object can be assigned to a SOLIDWORKS [IPartDoc](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html) variable.

## Accessors

[ISwDMClassFactory::GetApplication](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMClassFactory~GetApplication.html)

[ISwDMConfiguration::Application](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration~Application.html)

[ISwDMConfigurationMgr::Application](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfigurationMgr~Application.html)

## See Also

[ISwDMApplication5 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication5_members.html)
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
[ISwDMApplication Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication.html)
[ISwDMApplication2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication2.html)
[ISwDMApplication3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication3.html)
[ISwDMApplication4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication4.html)
[ISwDMClassFactory Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMClassFactory.html)
[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMSearchOption Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.html)
