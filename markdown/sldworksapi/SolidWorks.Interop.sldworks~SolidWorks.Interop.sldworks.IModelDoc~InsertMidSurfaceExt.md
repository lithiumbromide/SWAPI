---
title: "InsertMidSurfaceExt Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertMidSurfaceExt"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertMidSurfaceExt.html"
---

# InsertMidSurfaceExt Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertMidSurfaceExt](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertMidSurfaceExt.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertMidSurfaceExt( _
   ByVal Placement As System.Double, _
   ByVal KnitFlag As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Placement As System.Double
Dim KnitFlag As System.Boolean
Dim value As System.Object

value = instance.InsertMidSurfaceExt(Placement, KnitFlag)
```

### C#

```csharp
System.object InsertMidSurfaceExt(
   System.double Placement,
   System.bool KnitFlag
)
```

### C++/CLI

```cpp
System.Object^ InsertMidSurfaceExt(
   System.double Placement,
   System.bool KnitFlag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Placement`:
- `KnitFlag`:

## VBA Syntax

See [ModelDoc::InsertMidSurfaceExt](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertMidSurfaceExt.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
