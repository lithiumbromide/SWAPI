---
title: "InsertCosmeticThread Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertCosmeticThread"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertCosmeticThread.html"
---

# InsertCosmeticThread Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertCosmeticThread](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertCosmeticThread.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertCosmeticThread( _
   ByVal Type As System.Short, _
   ByVal Depth As System.Double, _
   ByVal Length As System.Double, _
   ByVal Note As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Type As System.Short
Dim Depth As System.Double
Dim Length As System.Double
Dim Note As System.String

instance.InsertCosmeticThread(Type, Depth, Length, Note)
```

### C#

```csharp
void InsertCosmeticThread(
   System.short Type,
   System.double Depth,
   System.double Length,
   System.string Note
)
```

### C++/CLI

```cpp
void InsertCosmeticThread(
   System.short Type,
   System.double Depth,
   System.double Length,
   System.String^ Note
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`:
- `Depth`:
- `Length`:
- `Note`:

## VBA Syntax

See [ModelDoc::InsertCosmeticThread](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertCosmeticThread.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
