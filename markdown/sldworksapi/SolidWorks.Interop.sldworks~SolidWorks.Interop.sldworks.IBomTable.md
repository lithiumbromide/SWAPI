---
title: "IBomTable Interface"
project: "SOLIDWORKS API Help"
interface: "IBomTable"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.html"
---

# IBomTable Interface

Allows access to BOM table information and values.

**IMPORTANT:** You can no longer insert IBomTable objects; you can now only insert [IBomTableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation.html) objects. IBomTable objects are not and cannot be converted to IBomTableAnnotation objects. Use the IBomTable APIs for legacy BOM tables only.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IBomTable
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTable
```

### C#

```csharp
public interface IBomTable
```

### C++/CLI

```cpp
public interface class IBomTable
```

## VBA Syntax

See [BomTable](ms-its:sldworksapivb6.chm::/sldworks~BomTable.html).

## Accessors

[IView::GetBomTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetBomTable.html) and [IView::IGetBomTable Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetBomTable.html)

[IView::InsertBomTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~InsertBomTable.html) and [IView::IInsertBomTable Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IInsertBomTable.html)

## Access Diagram

[BomTable](SWObjectModel.pdf#BomTable)

## See Also

[IBomTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
