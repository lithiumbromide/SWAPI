---
title: "Clone Method (IEnumDocuments)"
project: "SOLIDWORKS API Help"
interface: "IEnumDocuments"
member: "Clone"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments~Clone.html"
---

# Clone Method (IEnumDocuments)

Obsolete. Superseded by [IEnumDocuments2::Clone](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumDocuments2~Clone.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub Clone( _
   ByRef Ppenum As EnumDocuments _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnumDocuments
Dim Ppenum As EnumDocuments

instance.Clone(Ppenum)
```

### C#

```csharp
void Clone(
   out EnumDocuments Ppenum
)
```

### C++/CLI

```cpp
void Clone(
   [Out] EnumDocuments^ Ppenum
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ppenum`:

## VBA Syntax

See [EnumDocuments::Clone](ms-its:sldworksapivb6.chm::/sldworks~EnumDocuments~Clone.html).

## See Also

[IEnumDocuments Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments.html)
[IEnumDocuments Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments_members.html)
