---
title: "EditUndo Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "EditUndo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~EditUndo.html"
---

# EditUndo Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::EditUndo](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditUndo.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub EditUndo( _
   ByVal NSteps As System.UInteger _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim NSteps As System.UInteger

instance.EditUndo(NSteps)
```

### C#

```csharp
void EditUndo(
   System.uint NSteps
)
```

### C++/CLI

```cpp
void EditUndo(
   System.uint NSteps
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NSteps`:

## VBA Syntax

See [ModelDoc::EditUndo](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~EditUndo.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
