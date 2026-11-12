---
title: "RevisionTable Property (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "RevisionTable"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~RevisionTable.html"
---

# RevisionTable Property (ISheet)

Gets the revision table annotation for this drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property RevisionTable As RevisionTableAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim value As RevisionTableAnnotation

value = instance.RevisionTable
```

### C#

```csharp
RevisionTableAnnotation RevisionTable {get;}
```

### C++/CLI

```cpp
property RevisionTableAnnotation^ RevisionTable {
   RevisionTableAnnotation^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Revision table annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableAnnotation.html)

## VBA Syntax

See [Sheet::RevisionTable](ms-its:sldworksapivb6.chm::/sldworks~Sheet~RevisionTable.html).

## Examples

[Get Revision Table Annotation (VBA)](Get_Revision_Table_Example_VB.htm)

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::InsertRevisionTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~InsertRevisionTable.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
