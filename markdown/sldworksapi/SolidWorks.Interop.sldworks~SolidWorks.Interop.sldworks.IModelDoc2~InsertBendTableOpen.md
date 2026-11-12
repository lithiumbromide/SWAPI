---
title: "InsertBendTableOpen Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertBendTableOpen"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBendTableOpen.html"
---

# InsertBendTableOpen Method (IModelDoc2)

Inserts an existing bend table from a file into this model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertBendTableOpen( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim FileName As System.String
Dim value As System.Boolean

value = instance.InsertBendTableOpen(FileName)
```

### C#

```csharp
System.bool InsertBendTableOpen(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool InsertBendTableOpen(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: File name of the bend table to insert into this model document

### Return Value

True if the table is successfully inserted, false if not

## VBA Syntax

See [ModelDoc2::InsertBendTableOpen](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertBendTableOpen.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::InsertBendTableEdit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBendTableEdit.html)
[IModelDoc2::InsertBendTableNew Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBendTableNew.html)
[IModelDoc2::DeleteBendTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteBendTable.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
