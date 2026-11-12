---
title: "IGetTessTriStrips Method (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "IGetTessTriStrips"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~IGetTessTriStrips.html"
---

# IGetTessTriStrips Method (IFace)

Obsolete. Superseded by [IFace2::IGetTessTriStrips](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetTessTriStrips.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTessTriStrips( _
   ByVal NoConversion As System.Boolean _
) As System.Single
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim NoConversion As System.Boolean
Dim value As System.Single

value = instance.IGetTessTriStrips(NoConversion)
```

### C#

```csharp
System.float IGetTessTriStrips(
   System.bool NoConversion
)
```

### C++/CLI

```cpp
System.float IGetTessTriStrips(
   System.bool NoConversion
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NoConversion`:

## VBA Syntax

See [Face::IGetTessTriStrips](ms-its:sldworksapivb6.chm::/sldworks~Face~IGetTessTriStrips.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)
