---
title: "ISwDMComponent5 Interface"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMComponent5"
member: ""
kind: "interface"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent5.html"
---

# ISwDMComponent5 Interface

Accesses a component's data.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwDMComponent5
   Inherits ISwDMComponent, ISwDMComponent2, ISwDMComponent3, ISwDMComponent4
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMComponent5
```

### C#

```csharp
public interface ISwDMComponent5 : ISwDMComponent, ISwDMComponent2, ISwDMComponent3, ISwDMComponent4
```

### C++/CLI

```cpp
public interface class ISwDMComponent5 : public ISwDMComponent, ISwDMComponent2, ISwDMComponent3, ISwDMComponent4
```

## VBA Syntax

See [SwDMComponent5](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMComponent5.html).

## Examples

[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)

## Remarks

- You can access an ISwDMComponent5 object by calling QueryInterface on an [ISwDMComponent](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMComponent.html) object in C++ or by direct assignment in Visual Basic.
- The ISwDMComponent object can be assigned to an ISwDMComponent5 variable, just like the SOLIDWORKS [IModelDoc2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object can be assigned to a SOLIDWORKS [IPartDoc](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html) variable.

## Accessors

[ISwDMConfiguration2::GetComponents](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration2~GetComponents.html)

## See Also

[ISwDMComponent5 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent5_members.html)
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
[ISwDMComponent2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent2.html)
[ISwDMComponent3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent3.html)
[ISwDMComponent4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent4.html)
[ISwDMComponent6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent6.html)
[ISwDMComponent7 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent7.html)
[ISwDMComponent8 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent8.html)
[ISwDMComponent9 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent9.html)
[ISwDMComponent10 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent10.html)
[ISwDMComponent11 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent11.html)
[ISwDMComponent12 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent12.html)
