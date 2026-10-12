---
title: "ISwDMSheet2 Interface"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMSheet2"
member: ""
kind: "interface"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2.html"
---

# ISwDMSheet2 Interface

Accesses the drawing sheet.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwDMSheet2
   Inherits ISwDMSheet
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMSheet2
```

### C#

```csharp
public interface ISwDMSheet2 : ISwDMSheet
```

### C++/CLI

```cpp
public interface class ISwDMSheet2 : public ISwDMSheet
```

## VBA Syntax

See [SwDMSheet2](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMSheet2.html).

## Examples

[Get Preview Bitmaps of Drawing Sheets (C#)](Get_Preview_Bitmaps_of_Drawing_Sheets_Example_CSharp.htm)
[Get Preview Bitmaps of Drawing Sheets (VB.NET)](Get_Preview_Bitmaps_of_Drawing_Sheets_Example_VBNET.htm)

## Remarks

- You can access an SwDMSheet2 object by calling QueryInterface on an [ISwDMSheet](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMSheet.html) object in C++ or by direct assignment in Visual Basic.
- The SwDMSheet object can be assigned to a SwDMSheet2 variable, just like the SOLIDWORKS [IModelDoc2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object can be assigned to a SOLIDWORKS [IPartDoc](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html) variable.

## Accessors

[ISwDMDocument10::GetSheets](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument10~GetSheets.html)

[ISwDMTable5::Sheet](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable5~Sheet.html)

[ISwDMView::Sheet](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMView~Sheet.html)

## See Also

[ISwDMSheet2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet2_members.html)
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
[ISwDMSheet Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet.html)
[ISwDMSheet3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet3.html)
[ISwDMSheet4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMSheet4.html)
