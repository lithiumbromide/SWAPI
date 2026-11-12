---
title: "ISwDMTable5 Interface"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMTable5"
member: ""
kind: "interface"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable5.html"
---

# ISwDMTable5 Interface

Accesses revision and bill of materials (BOM) tables.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwDMTable5
   Inherits ISwDMTable, ISwDMTable2, ISwDMTable3, ISwDMTable4
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMTable5
```

### C#

```csharp
public interface ISwDMTable5 : ISwDMTable, ISwDMTable2, ISwDMTable3, ISwDMTable4
```

### C++/CLI

```cpp
public interface class ISwDMTable5 : public ISwDMTable, ISwDMTable2, ISwDMTable3, ISwDMTable4
```

## VBA Syntax

See [SwDMTable5](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMTable5.html).

## Examples

[Get BOM Tables (VB.NET)](Get_BOM_Tables_Example_VBNET.htm)
[Get BOM Tables (C#)](Get_BOM_Tables_Example_CSharp.htm)

## Remarks

Only revision and bill of materials (BOM) tables are supported.

**NOTES**:

- You can access an SwDMTable5 object by calling QueryInterface on an [ISwDMTable](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMTable.html) object in C++ or by direct assignment in Visual Basic.
- The SwDMTable object can be assigned to a SwDMTable5 variable, just like the SOLIDWORKS [IModelDoc2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object can be assigned to a SOLIDWORKS [IPartDoc](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html) variable.

## Accessors

[ISwDMDocument10::GetTable](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument10~GetTable.html)

## See Also

[ISwDMTable5 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable5_members.html)
[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
[ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.html)
[ISwDMTable2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable2.html)
[ISwDMTable3 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable3.html)
[ISwDMTable4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable4.html)
[ISwDMTable6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable6.html)
