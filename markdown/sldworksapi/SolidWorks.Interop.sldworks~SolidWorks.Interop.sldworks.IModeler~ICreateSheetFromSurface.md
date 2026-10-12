---
title: "ICreateSheetFromSurface Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreateSheetFromSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromSurface.html"
---

# ICreateSheetFromSurface Method (IModeler)

Obsolete. Superseded by [IModeler::ICreateSheetFromSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateSheetFromSurface2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateSheetFromSurface( _
   ByVal SurfaceIn As Surface, _
   ByRef UvRange As System.Double _
) As Body
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim SurfaceIn As Surface
Dim UvRange As System.Double
Dim value As Body

value = instance.ICreateSheetFromSurface(SurfaceIn, UvRange)
```

### C#

```csharp
Body ICreateSheetFromSurface(
   Surface SurfaceIn,
   ref System.double UvRange
)
```

### C++/CLI

```cpp
Body^ ICreateSheetFromSurface(
   Surface^ SurfaceIn,
   System.double% UvRange
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SurfaceIn`:
- `UvRange`:

## VBA Syntax

See [Modeler::ICreateSheetFromSurface](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreateSheetFromSurface.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
