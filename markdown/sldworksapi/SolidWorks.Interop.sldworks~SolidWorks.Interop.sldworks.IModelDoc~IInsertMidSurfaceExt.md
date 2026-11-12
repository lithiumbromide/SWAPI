---
title: "IInsertMidSurfaceExt Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IInsertMidSurfaceExt"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IInsertMidSurfaceExt.html"
---

# IInsertMidSurfaceExt Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IInsertMidSurfaceExt](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IInsertMidSurfaceExt.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IInsertMidSurfaceExt( _
   ByVal Placement As System.Double, _
   ByVal KnitFlag As System.Boolean _
) As MidSurface
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Placement As System.Double
Dim KnitFlag As System.Boolean
Dim value As MidSurface

value = instance.IInsertMidSurfaceExt(Placement, KnitFlag)
```

### C#

```csharp
MidSurface IInsertMidSurfaceExt(
   System.double Placement,
   System.bool KnitFlag
)
```

### C++/CLI

```cpp
MidSurface^ IInsertMidSurfaceExt(
   System.double Placement,
   System.bool KnitFlag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Placement`:
- `KnitFlag`:

## VBA Syntax

See [ModelDoc::IInsertMidSurfaceExt](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IInsertMidSurfaceExt.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
