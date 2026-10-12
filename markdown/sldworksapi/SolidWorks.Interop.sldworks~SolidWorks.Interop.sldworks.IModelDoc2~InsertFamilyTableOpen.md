---
title: "InsertFamilyTableOpen Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertFamilyTableOpen"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertFamilyTableOpen.html"
---

# InsertFamilyTableOpen Method (IModelDoc2)

Inserts the specified Microsoft Excel design table.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertFamilyTableOpen( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim FileName As System.String
Dim value As System.Boolean

value = instance.InsertFamilyTableOpen(FileName)
```

### C#

```csharp
System.bool InsertFamilyTableOpen(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool InsertFamilyTableOpen(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Full path and filename of the Microsoft Excel design table

### Return Value

True if the design table is inserted, false if not

## VBA Syntax

See [ModelDoc2::InsertFamilyTableOpen](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertFamilyTableOpen.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::CloseFamilyTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CloseFamilyTable.html)
[IModelDoc2::DeleteDesignTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteDesignTable.html)
[IModelDoc2::GetDesignTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetDesignTable.html)
[IModelDoc2::IGetDesignTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetDesignTable.html)
[IModelDoc2::InsertFamilyTableEdit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertFamilyTableEdit.html)
[IModelDoc2::InsertFamilyTableNew Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertFamilyTableNew.html)
[IModelDocExtension::HasDesignTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasDesignTable.html)
[IDesignTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
