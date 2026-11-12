---
title: "ICreateBoundedSurface Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "ICreateBoundedSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreateBoundedSurface.html"
---

# ICreateBoundedSurface Method (IBody)

Obsolete. Superseded by [IBody2::ICreateBoundedSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateBoundedSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ICreateBoundedSurface( _
   ByVal UOpt As System.Boolean, _
   ByVal VOpt As System.Boolean, _
   ByRef UvParams As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim UOpt As System.Boolean
Dim VOpt As System.Boolean
Dim UvParams As System.Double

instance.ICreateBoundedSurface(UOpt, VOpt, UvParams)
```

### C#

```csharp
void ICreateBoundedSurface(
   System.bool UOpt,
   System.bool VOpt,
   ref System.double UvParams
)
```

### C++/CLI

```cpp
void ICreateBoundedSurface(
   System.bool UOpt,
   System.bool VOpt,
   System.double% UvParams
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UOpt`:
- `VOpt`:
- `UvParams`:

## VBA Syntax

See [Body::ICreateBoundedSurface](ms-its:sldworksapivb6.chm::/sldworks~Body~ICreateBoundedSurface.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
