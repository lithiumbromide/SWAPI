---
title: "ISwDMSheet4 Interface"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMSheet4"
member: ""
kind: "interface"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet4.html"
---

# ISwDMSheet4 Interface

Accesses the drawing sheet.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwDMSheet4
   Inherits ISwDMSheet, ISwDMSheet2, ISwDMSheet3
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMSheet4
```

### C#

```csharp
public interface ISwDMSheet4 : ISwDMSheet, ISwDMSheet2, ISwDMSheet3
```

### C++/CLI

```cpp
public interface class ISwDMSheet4 : public ISwDMSheet, ISwDMSheet2, ISwDMSheet3
```

## VBA Syntax

See [SwDMSheet4](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMSheet4.html).

## Examples

[Get BOM Tables (VB.NET)](Get_BOM_Tables_Example_VBNET.htm)
[Get BOM Tables (C#)](Get_BOM_Tables_Example_CSharp.htm)

## Remarks

- You can access an SwDMSheet4 object by calling QueryInterface on an [ISwDMSheet](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMSheet.html) object in C++ or by direct assignment in Visual Basic.
- The SwDMSheet object can be assigned to a SwDMSheet4 variable, just like the SOLIDWORKS [IModelDoc2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object can be assigned to a SOLIDWORKS [IPartDoc](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html) variable.

## Accessors

[ISwDMDocument10::GetSheets](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument10~GetSheets.html)

[ISwDMTable5::Sheet](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable5~Sheet.html)

[ISwDMView::Sheet](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMView~Sheet.html)

## See Also

[ISwDMSheet4 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet4_members.html)
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
[ISwDMSheet Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet.html)
[ISwDMSheet2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2.html)
[ISwDMSheet3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet3.html)
