---
title: "ISwDMTable4 Interface"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable4"
member: ""
kind: "interface"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable4.html"
---

# ISwDMTable4 Interface

Accesses revision and bill of materials (BOM) tables.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwDMTable4
   Inherits ISwDMTable, ISwDMTable2, ISwDMTable3
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable4
```

### C#

```csharp
public interface ISwDMTable4 : ISwDMTable, ISwDMTable2, ISwDMTable3
```

### C++/CLI

```cpp
public interface class ISwDMTable4 : public ISwDMTable, ISwDMTable2, ISwDMTable3
```

## VBA Syntax

See [SwDMTable4](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable4.html).

## Examples

[Get BOM Tables (C#)](Get_BOM_Tables_Example_CSharp.htm)
[Get BOM Tables (VB.NET)](Get_BOM_Tables_Example_VBNET.htm)

## Remarks

Only revision and bill of materials (BOM) tables are supported.

**NOTES**:

- You can access an SwDMTable4 object by calling QueryInterface on an [ISwDMTable](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMTable.html) object in C++ or by direct assignment in Visual Basic.
- The SwDMTable object can be assigned to a SwDMTable4 variable, just like the SOLIDWORKS [IModelDoc2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object can be assigned to a SOLIDWORKS [IPartDoc](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html) variable.

## Accessors

[ISwDMDocument10::GetTable](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument10~GetTable.html)

## See Also

[ISwDMTable4 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable4_members.html)
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
[ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.html)
[ISwDMTable2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2.html)
[ISwDMTable3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable3.html)
[ISwDMTable5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable5.html)
[ISwDMTable6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6.html)
