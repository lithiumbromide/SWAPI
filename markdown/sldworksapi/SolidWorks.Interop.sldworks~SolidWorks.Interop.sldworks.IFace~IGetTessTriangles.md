---
title: "IGetTessTriangles Method (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "IGetTessTriangles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~IGetTessTriangles.html"
---

# IGetTessTriangles Method (IFace)

Obsolete. Superseded by [IFace2::IGetTessTriangles](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetTessTriangles.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTessTriangles( _
   ByVal NoConversion As System.Boolean _
) As System.Single
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim NoConversion As System.Boolean
Dim value As System.Single

value = instance.IGetTessTriangles(NoConversion)
```

### C#

```csharp
System.float IGetTessTriangles(
   System.bool NoConversion
)
```

### C++/CLI

```cpp
System.float IGetTessTriangles(
   System.bool NoConversion
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NoConversion`:

## VBA Syntax

See [Face::IGetTessTriangles](ms-its:sldworksapivb6.chm::/sldworks~Face~IGetTessTriangles.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)
