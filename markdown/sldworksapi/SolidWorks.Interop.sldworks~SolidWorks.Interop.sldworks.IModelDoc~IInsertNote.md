---
title: "IInsertNote Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IInsertNote"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IInsertNote.html"
---

# IInsertNote Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IInsertNote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IInsertNote.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IInsertNote( _
   ByVal Text As System.String _
) As Note
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Text As System.String
Dim value As Note

value = instance.IInsertNote(Text)
```

### C#

```csharp
Note IInsertNote(
   System.string Text
)
```

### C++/CLI

```cpp
Note^ IInsertNote(
   System.String^ Text
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Text`:

## VBA Syntax

See [ModelDoc::IInsertNote](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IInsertNote.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
