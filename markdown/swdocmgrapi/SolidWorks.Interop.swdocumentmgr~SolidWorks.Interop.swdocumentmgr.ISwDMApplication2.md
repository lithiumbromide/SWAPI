---
title: "ISwDMApplication2 Interface"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMApplication2"
member: ""
kind: "interface"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication2.html"
---

# ISwDMApplication2 Interface

Manages part, assembly, or drawing documents.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwDMApplication2
   Inherits ISwDMApplication
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMApplication2
```

### C#

```csharp
public interface ISwDMApplication2 : ISwDMApplication
```

### C++/CLI

```cpp
public interface class ISwDMApplication2 : public ISwDMApplication
```

## VBA Syntax

See [SwDMApplication2](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMApplication2.html).

## Remarks

- You can access an SwDMApplication2 object by calling QueryInterface on an [ISwDMApplication](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMApplication.html) object in C++ or by direct assignment in Visual Basic.
- The SwDMApplication object can be assigned to a SwDMApplication2 variable, just like the SOLIDWORKS [IModelDoc2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object can be assigned to a SOLIDWORKS [IPartDoc](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html) variable.

## Accessors

[ISwDMClassFactory::GetApplication](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMClassFactory~GetApplication.html)

[ISwDMConfiguration::Application](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration~Application.html)

[ISwDMConfigurationMgr::Application](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfigurationMgr~Application.html)

## See Also

[ISwDMApplication2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication2_members.html)
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
[ISwDMApplication4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication4.html)
[ISwDMClassFactory Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMClassFactory.html)
[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMSearchOption Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.html)
[ISwDMApplication Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication.html)
[ISwDMApplication3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication3.html)
[ISwDMApplication5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication5.html)
