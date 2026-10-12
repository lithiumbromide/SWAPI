---
title: "SetKeepLinkedToBOM Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "SetKeepLinkedToBOM"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetKeepLinkedToBOM.html"
---

# SetKeepLinkedToBOM Method (IView)

Sets whether this drawing view is linked to the specified BOM or weldment cut-list table.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetKeepLinkedToBOM( _
   ByVal Linked As System.Boolean, _
   ByVal Name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Linked As System.Boolean
Dim Name As System.String
Dim value As System.Boolean

value = instance.SetKeepLinkedToBOM(Linked, Name)
```

### C#

```csharp
System.bool SetKeepLinkedToBOM(
   System.bool Linked,
   System.string Name
)
```

### C++/CLI

```cpp
System.bool SetKeepLinkedToBOM(
   System.bool Linked,
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Linked`: True to set a drawing view to the specified BOM or weldment cut-list table, false to not
- `Name`: Name of the BOM or weldment cut-list table to which to link this drawing view

### Return Value

True if the BOM or weldment cut-list table is linked to this drawing view, false if not

## VBA Syntax

See [View::SetKeepLinkedToBOM](ms-its:sldworksapivb6.chm::/sldworks~View~SetKeepLinkedToBOM.html).

## Remarks

This method returns false if the string specified for Name does not correspond to the name of a BOM or weldment cut-list table feature created for the model in this drawing view.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetKeepLinkedToBOM Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOM.html)
[IView::GetKeepLinkedToBOMName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOMName.html)
[IView::IInsertBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IInsertBomTable.html)
[IView::InsertBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable.html)
[IView::InsertBomTable2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable2.html)
[IView::InsertWeldmentTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertWeldmentTable.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14.2
