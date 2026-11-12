---
title: "GetTessTriangles Method (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "GetTessTriangles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~GetTessTriangles.html"
---

# GetTessTriangles Method (IFace)

Obsolete. Superseded by [IFace2::GetTessTriangles.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetTessTriangles.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTessTriangles( _
   ByVal NoConversion As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim NoConversion As System.Boolean
Dim value As System.Object

value = instance.GetTessTriangles(NoConversion)
```

### C#

```csharp
System.object GetTessTriangles(
   System.bool NoConversion
)
```

### C++/CLI

```cpp
System.Object^ GetTessTriangles(
   System.bool NoConversion
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NoConversion`:

## VBA Syntax

See [Face::GetTessTriangles](ms-its:sldworksapivb6.chm::/sldworks~Face~GetTessTriangles.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)
