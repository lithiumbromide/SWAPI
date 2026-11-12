---
title: "HasDesignTable Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "HasDesignTable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~HasDesignTable.html"
---

# HasDesignTable Method (IView)

Gets whether this drawing view has a design table associated with it.

## Syntax

### Visual Basic (Declaration)

```vb
Function HasDesignTable() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

value = instance.HasDesignTable()
```

### C#

```csharp
System.bool HasDesignTable()
```

### C++/CLI

```cpp
System.bool HasDesignTable();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this drawing view has a design table, false if not

## VBA Syntax

See [View::HasDesignTable](ms-its:sldworksapivb6.chm::/sldworks~View~HasDesignTable.html).

## Examples

[Get Excel Design Table Worksheet (VBA)](Get_Excel_Design_Table_Worksheet_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDesignTableExtent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDesignTableExtent.html)
[IView::IGetDesignTableExtent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDesignTableExtent.html)

## Availability

SOLIDWORKS 99, datecode 1999207
