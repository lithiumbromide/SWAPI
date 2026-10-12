---
title: "ISwDMTable3 Interface"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable3"
member: ""
kind: "interface"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable3.html"
---

# ISwDMTable3 Interface

Accesses revision and bill of materials (BOM) tables.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwDMTable3
   Inherits ISwDMTable, ISwDMTable2
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable3
```

### C#

```csharp
public interface ISwDMTable3 : ISwDMTable, ISwDMTable2
```

### C++/CLI

```cpp
public interface class ISwDMTable3 : public ISwDMTable, ISwDMTable2
```

## VBA Syntax

See [SwDMTable3](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable3.html).

## Examples

[Get Table Cell Text (C#)](Get_Table_Cell_Text_Example_CSharp.htm)
[Get Table Cell Text (VB.NET)](Get_Table_Cell_Text_Example_VBNET.htm)

## Remarks

Only revision and bill of materials (BOM) tables are supported.

**NOTES**:

- You can access an SwDMTable3 object by calling QueryInterface on na [ISwDMTable](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMTable.html) object in C++ or by direct assignment in Visual Basic.
- The SwDMTable object can be assigned to a SwDMTable3 variable, just like the SOLIDWORKS [IModelDoc2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object can be assigned to a SOLIDWORKS [IPartDoc](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html) variable.

## Accessors

[ISwDMDocument10::GetTable](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument10~GetTable.html)

## See Also

[ISwDMTable3 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable3_members.html)
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
[ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.html)
[ISwDMTable2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2.html)
[ISwDMDocument10::GetTableNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument10~GetTableNames.html)
[ISwDMTable4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable4.html)
[ISwDMTable5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable5.html)
[ISwDMTable6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6.html)
