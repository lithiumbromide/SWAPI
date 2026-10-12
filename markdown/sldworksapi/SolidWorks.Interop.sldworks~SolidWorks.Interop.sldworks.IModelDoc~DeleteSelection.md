---
title: "DeleteSelection Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "DeleteSelection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~DeleteSelection.html"
---

# DeleteSelection Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::DeleteSelection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~DeleteSelection.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteSelection( _
   ByVal ConfirmFlag As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim ConfirmFlag As System.Boolean
Dim value As System.Boolean

value = instance.DeleteSelection(ConfirmFlag)
```

### C#

```csharp
System.bool DeleteSelection(
   System.bool ConfirmFlag
)
```

### C++/CLI

```cpp
System.bool DeleteSelection(
   System.bool ConfirmFlag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfirmFlag`:

## VBA Syntax

See [ModelDoc::DeleteSelection](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~DeleteSelection.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
