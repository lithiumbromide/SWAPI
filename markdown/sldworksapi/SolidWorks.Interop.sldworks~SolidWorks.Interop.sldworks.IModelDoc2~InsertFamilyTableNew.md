---
title: "InsertFamilyTableNew Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertFamilyTableNew"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertFamilyTableNew.html"
---

# InsertFamilyTableNew Method (IModelDoc2)

Inserts an existing design table from the model into the selected drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertFamilyTableNew()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.InsertFamilyTableNew()
```

### C#

```csharp
void InsertFamilyTableNew()
```

### C++/CLI

```cpp
void InsertFamilyTableNew();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::InsertFamilyTableNew](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertFamilyTableNew.html).

## Remarks

Before using this method in a drawing, you must have selected a drawing view and that drawing view must contain a model that has an existing family table. If you have not selected a drawing view before using this method or if the selected drawing view does not contain a family table, then this method takes no action.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::CloseFamilyTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CloseFamilyTable.html)
[IModelDoc2::DeleteDesignTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteDesignTable.html)
[IModelDoc2::GetDesignTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetDesignTable.html)
[IModelDoc2::IGetDesignTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetDesignTable.html)
[IModelDoc2::InsertFamilyTableEdit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertFamilyTableEdit.html)
[IModelDoc2::InsertFamilyTableOpen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertFamilyTableOpen.html)
[IModelDocExtension::HasDesignTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasDesignTable.html)
[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
