---
title: "IGetDesignTable Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IGetDesignTable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetDesignTable.html"
---

# IGetDesignTable Method (IModelDoc2)

Gets the design table associated with this part or assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDesignTable() As DesignTable
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As DesignTable

value = instance.IGetDesignTable()
```

### C#

```csharp
DesignTable IGetDesignTable()
```

### C++/CLI

```cpp
DesignTable^ IGetDesignTable();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Design table](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable.html)

## VBA Syntax

See [ModelDoc2::IGetDesignTable](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IGetDesignTable.html).

## Remarks

If you call this method from a drawing document, NULL is returned.

To access design tables from a drawing document you must get the [IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object associated with a particular drawing view and then call this method from that IModelDoc2 object. To determine if a drawing view has a design table associated with it, use[IView::HasDesignTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~HasDesignTable.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::CloseFamilyTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CloseFamilyTable.html)
[IModelDoc2::DeleteDesignTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteDesignTable.html)
[IModelDoc2::GetDesignTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetDesignTable.html)
[IModelDoc2::InsertFamilyTableEdit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertFamilyTableEdit.html)
[IModelDoc2::InsertFamilyTableNew Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertFamilyTableNew.html)
[IModelDoc2::InsertFamilyTableOpen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertFamilyTableOpen.html)
[IModelDoc2::IGetDesignTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetDesignTable.html)
[IModelDocExtension::HasDesignTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasDesignTable.html)
[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
