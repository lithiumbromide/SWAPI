---
title: "InsertOffsetSurface Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertOffsetSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertOffsetSurface.html"
---

# InsertOffsetSurface Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertOffsetSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertOffsetSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertOffsetSurface( _
   ByVal Thickness As System.Double, _
   ByVal Reverse As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Thickness As System.Double
Dim Reverse As System.Boolean

instance.InsertOffsetSurface(Thickness, Reverse)
```

### C#

```csharp
void InsertOffsetSurface(
   System.double Thickness,
   System.bool Reverse
)
```

### C++/CLI

```cpp
void InsertOffsetSurface(
   System.double Thickness,
   System.bool Reverse
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Thickness`:
- `Reverse`:

## VBA Syntax

See [ModelDoc::InsertOffsetSurface](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertOffsetSurface.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
