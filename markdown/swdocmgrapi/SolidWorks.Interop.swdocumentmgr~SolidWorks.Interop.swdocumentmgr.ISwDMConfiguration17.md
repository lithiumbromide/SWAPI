---
title: "ISwDMConfiguration17 Interface"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration17"
member: ""
kind: "interface"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17.html"
---

# ISwDMConfiguration17 Interface

Accesses configuration-specific information for the part, assembly, or drawing document.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwDMConfiguration17
   Inherits ISwDMConfiguration, ISwDMConfiguration10, ISwDMConfiguration11, ISwDMConfiguration12, ISwDMConfiguration13, ISwDMConfiguration14, ISwDMConfiguration15, ISwDMConfiguration16, ISwDMConfiguration2, ISwDMConfiguration3, ISwDMConfiguration4, ISwDMConfiguration5, ISwDMConfiguration6, ISwDMConfiguration7, ISwDMConfiguration8, ISwDMConfiguration9
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration17
```

### C#

```csharp
public interface ISwDMConfiguration17 : ISwDMConfiguration, ISwDMConfiguration10, ISwDMConfiguration11, ISwDMConfiguration12, ISwDMConfiguration13, ISwDMConfiguration14, ISwDMConfiguration15, ISwDMConfiguration16, ISwDMConfiguration2, ISwDMConfiguration3, ISwDMConfiguration4, ISwDMConfiguration5, ISwDMConfiguration6, ISwDMConfiguration7, ISwDMConfiguration8, ISwDMConfiguration9
```

### C++/CLI

```cpp
public interface class ISwDMConfiguration17 : public ISwDMConfiguration, ISwDMConfiguration10, ISwDMConfiguration11, ISwDMConfiguration12, ISwDMConfiguration13, ISwDMConfiguration14, ISwDMConfiguration15, ISwDMConfiguration16, ISwDMConfiguration2, ISwDMConfiguration3, ISwDMConfiguration4, ISwDMConfiguration5, ISwDMConfiguration6, ISwDMConfiguration7, ISwDMConfiguration8, ISwDMConfiguration9
```

## VBA Syntax

See [SwDMConfiguration17](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration17.html).

## Examples

[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)
[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)

## Remarks

- You can access an ISwDMConfiguration17 object by calling QueryInterface on an [ISwDMConfiguration](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.html) object in C++ or by direct assignment in Visual Basic.
- The ISwDMConfiguration object can be assigned to an ISwDMConfiguration17 variable, just like the SOLIDWORKS [IModelDoc2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object can be assigned to a SOLIDWORKS [IPartDoc](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html) variable.

## Accessors

[ISwDMConfigurationMgr::GetConfigurationByName](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr~GetConfigurationByName.html)

## See Also

[ISwDMConfiguration17 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration17_members.html)
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
[ISwDMConfigurationMgr2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2.html)
[ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.html)
[ISwDMConfiguration2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2.html)
[ISwDMConfiguration3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration3.html)
[ISwDMConfiguration4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration4.html)
[ISwDMConfiguration5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration5.html)
[ISwDMConfiguration6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration6.html)
[ISwDMConfiguration7 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7.html)
[ISwDMConfiguration8 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration8.html)
[ISwDMConfiguration9 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration9.html)
[ISwDMConfiguration10 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration10.html)
[ISwDMConfiguration11 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11.html)
[ISwDMConfiguration12 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration12.html)
[ISwDMConfiguration13 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration13.html)
[ISwDMConfiguration14 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration14.html)
[ISwDMConfiguration15 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration15.html)
[ISwDMConfiguration16 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration16.html)
[ISwDMConfiguration18 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration18.html)
