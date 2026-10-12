---
title: "GetKeepLinkedToBOM Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetKeepLinkedToBOM"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOM.html"
---

# GetKeepLinkedToBOM Method (IView)

Gets whether this drawing view is linked to a BOM or weldment cut-list table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetKeepLinkedToBOM() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

value = instance.GetKeepLinkedToBOM()
```

### C#

```csharp
System.bool GetKeepLinkedToBOM()
```

### C++/CLI

```cpp
System.bool GetKeepLinkedToBOM();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this drawing view is linked to a BOM or weldment cut-list table, false if not

## VBA Syntax

See [View::GetKeepLinkedToBOM](ms-its:sldworksapivb6.chm::/sldworks~View~GetKeepLinkedToBOM.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBomTable.html)
[IView::GetKeepLinkedToBOMName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOMName.html)
[IView::IGetBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBomTable.html)
[IView::IInsertBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IInsertBomTable.html)
[IView::InsertBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable.html)
[IView::InsertBomTable2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable2.html)
[IView::InsertWeldmentTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertWeldmentTable.html)
[IView::SetKeepLinkedToBOM Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetKeepLinkedToBOM.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14.2
