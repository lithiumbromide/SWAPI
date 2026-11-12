---
title: "IGetBomTable Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetBomTable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBomTable.html"
---

# IGetBomTable Method (IView)

Gets the BOM table found in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBomTable() As BomTable
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As BomTable

value = instance.IGetBomTable()
```

### C#

```csharp
BomTable IGetBomTable()
```

### C++/CLI

```cpp
BomTable^ IGetBomTable();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[BOM table](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable.html)

## VBA Syntax

See [View::IGetBomTable](ms-its:sldworksapivb6.chm::/sldworks~View~IGetBomTable.html).

## Remarks

This method only returns a BOM table if there is a Microsoft Excel-based BOM for the drawing view.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBomTable.html)
[InsertBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable.html)
[InsertBomTable2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable2.html)
[IView::GetKeepLinkedToBOM Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOM.html)
[IView::GetKeepLinkedToBOMName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOMName.html)
[IView::IInsertBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IInsertBomTable.html)
