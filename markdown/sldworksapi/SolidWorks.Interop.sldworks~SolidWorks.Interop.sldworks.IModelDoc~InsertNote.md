---
title: "InsertNote Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertNote"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertNote.html"
---

# InsertNote Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertNote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertNote.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertNote( _
   ByVal Text As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Text As System.String
Dim value As System.Object

value = instance.InsertNote(Text)
```

### C#

```csharp
System.object InsertNote(
   System.string Text
)
```

### C++/CLI

```cpp
System.Object^ InsertNote(
   System.String^ Text
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Text`:

## VBA Syntax

See [ModelDoc::InsertNote](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertNote.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
