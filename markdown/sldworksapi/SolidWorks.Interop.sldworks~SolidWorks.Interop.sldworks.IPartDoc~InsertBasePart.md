---
title: "InsertBasePart Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "InsertBasePart"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertBasePart.html"
---

# InsertBasePart Method (IPartDoc)

Obsolete. Superseded by [IPartDoc::InsertPart](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~InsertPart.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertBasePart( _
   ByVal FileName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim FileName As System.String
Dim value As System.Boolean

value = instance.InsertBasePart(FileName)
```

### C#

```csharp
System.bool InsertBasePart(
   System.string FileName
)
```

### C++/CLI

```cpp
System.bool InsertBasePart(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`:

## VBA Syntax

See [PartDoc::InsertBasePart](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~InsertBasePart.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
