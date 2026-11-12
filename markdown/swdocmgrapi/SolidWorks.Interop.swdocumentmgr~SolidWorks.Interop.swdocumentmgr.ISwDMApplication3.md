---
title: "ISwDMApplication3 Interface"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMApplication3"
member: ""
kind: "interface"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication3.html"
---

# ISwDMApplication3 Interface

Manages part, assembly, or drawing documents.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwDMApplication3
   Inherits ISwDMApplication, ISwDMApplication2
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMApplication3
```

### C#

```csharp
public interface ISwDMApplication3 : ISwDMApplication, ISwDMApplication2
```

### C++/CLI

```cpp
public interface class ISwDMApplication3 : public ISwDMApplication, ISwDMApplication2
```

## VBA Syntax

See [SwDMApplication3](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMApplication3.html).

## Remarks

- You can access an SwDMApplication3 object by calling QueryInterface on an [ISwDMApplication](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMApplication.html) object in C++ or by direct assignment in Visual Basic.
- The SwDMApplication object can be assigned to a SwDMApplication3 variable, just like the SOLIDWORKS [IModelDoc2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object can be assigned to a SOLIDWORKS [IPartDoc](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html) variable.

## Accessors

[ISwDMClassFactory::GetApplication](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMClassFactory~GetApplication.html)

[ISwDMConfiguration::Application](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration~Application.html)

[ISwDMConfigurationMgr::Application](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfigurationMgr~Application.html)

## See Also

[ISwDMApplication3 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication3_members.html)
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
[ISwDMApplication2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication2.html)
[ISwDMApplication4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication4.html)
[ISwDMClassFactory Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMClassFactory.html)
[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMSearchOption Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.html)
[ISwDMApplication Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication.html)
[ISwDMApplication5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication5.html)
