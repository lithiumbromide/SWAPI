---
title: "GetKeepLinkedToBOMName Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetKeepLinkedToBOMName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOMName.html"
---

# GetKeepLinkedToBOMName Method (IView)

Gets the name of the BOM or weldment cut-list table feature to which this drawing view is linked.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetKeepLinkedToBOMName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.String

value = instance.GetKeepLinkedToBOMName()
```

### C#

```csharp
System.string GetKeepLinkedToBOMName()
```

### C++/CLI

```cpp
System.String^ GetKeepLinkedToBOMName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Name of BOM or weldment cut-list table feature

## VBA Syntax

See [View::GetKeepLinkedToBOMName](ms-its:sldworksapivb6.chm::/sldworks~View~GetKeepLinkedToBOMName.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBomTable.html)
[IView::GetKeepLinkedToBOM Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOM.html)
[IView::IGetBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBomTable.html)
[IView::IInsertBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IInsertBomTable.html)
[IView::InsertBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable.html)
[IView::InsertBomTable2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable2.html)
[IView::InsertWeldmentTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertWeldmentTable.html)
[IView::SetKeepLinkedToBOM Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetKeepLinkedToBOM.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14.2
