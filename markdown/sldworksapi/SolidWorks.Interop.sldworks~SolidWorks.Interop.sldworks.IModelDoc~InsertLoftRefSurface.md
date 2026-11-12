---
title: "InsertLoftRefSurface Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertLoftRefSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertLoftRefSurface.html"
---

# InsertLoftRefSurface Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertLoftRefSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertLoftRefSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertLoftRefSurface( _
   ByVal Closed As System.Boolean, _
   ByVal KeepTangency As System.Boolean, _
   ByVal ForceNonRational As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Closed As System.Boolean
Dim KeepTangency As System.Boolean
Dim ForceNonRational As System.Boolean

instance.InsertLoftRefSurface(Closed, KeepTangency, ForceNonRational)
```

### C#

```csharp
void InsertLoftRefSurface(
   System.bool Closed,
   System.bool KeepTangency,
   System.bool ForceNonRational
)
```

### C++/CLI

```cpp
void InsertLoftRefSurface(
   System.bool Closed,
   System.bool KeepTangency,
   System.bool ForceNonRational
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Closed`:
- `KeepTangency`:
- `ForceNonRational`:

## VBA Syntax

See [ModelDoc::InsertLoftRefSurface](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertLoftRefSurface.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
