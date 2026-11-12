---
title: "ISwDMApplication4 Interface"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMApplication4"
member: ""
kind: "interface"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication4.html"
---

# ISwDMApplication4 Interface

Manages part, assembly, or drawing documents.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwDMApplication4
   Inherits ISwDMApplication, ISwDMApplication2, ISwDMApplication3
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMApplication4
```

### C#

```csharp
public interface ISwDMApplication4 : ISwDMApplication, ISwDMApplication2, ISwDMApplication3
```

### C++/CLI

```cpp
public interface class ISwDMApplication4 : public ISwDMApplication, ISwDMApplication2, ISwDMApplication3
```

## VBA Syntax

See [SwDMApplication4](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMApplication4.html).

## Examples

[Get External References for Part (C#)](Get_External_References_for_Part_Example_CSharp.htm)
[Get External References for Part (VB.NET)](Get_External_References_for_Part_Example_VBNET.htm)
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)

## Remarks

- You can access an SwDMApplication4 object by calling QueryInterface on an [ISwDMApplication](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMApplication.html) object in C++ or by direct assignment in Visual Basic.
- The SwDMApplication object can be assigned to a SwDMApplication4 variable, just like the SOLIDWORKS [IModelDoc2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object can be assigned to a SOLIDWORKS [IPartDoc](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html) variable.

## Accessors

[ISwDMClassFactory::GetApplication](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMClassFactory~GetApplication.html)

[ISwDMConfiguration::Application](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration~Application.html)

[ISwDMConfigurationMgr::Application](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfigurationMgr~Application.html)

## See Also

[ISwDMApplication4 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication4_members.html)
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
[ISwDMApplication2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication2.html)
[ISwDMClassFactory Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMClassFactory.html)
[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMSearchOption Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSearchOption.html)
[ISwDMApplication Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication.html)
[ISwDMApplication3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication3.html)
[ISwDMApplication5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication5.html)
