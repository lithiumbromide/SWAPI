---
title: "InsertFeatureShell Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertFeatureShell"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertFeatureShell.html"
---

# InsertFeatureShell Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertFeatureShell](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertFeatureShell.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertFeatureShell( _
   ByVal Thickness As System.Double, _
   ByVal Outward As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Thickness As System.Double
Dim Outward As System.Boolean

instance.InsertFeatureShell(Thickness, Outward)
```

### C#

```csharp
void InsertFeatureShell(
   System.double Thickness,
   System.bool Outward
)
```

### C++/CLI

```cpp
void InsertFeatureShell(
   System.double Thickness,
   System.bool Outward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Thickness`:
- `Outward`:

## VBA Syntax

See [ModelDoc::InsertFeatureShell](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertFeatureShell.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
