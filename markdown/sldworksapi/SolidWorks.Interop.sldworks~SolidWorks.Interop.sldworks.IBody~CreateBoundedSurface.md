---
title: "CreateBoundedSurface Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "CreateBoundedSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~CreateBoundedSurface.html"
---

# CreateBoundedSurface Method (IBody)

Obsolete. Superseded by [IBody2::CreateBoundedSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateBoundedSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateBoundedSurface( _
   ByVal UOpt As System.Boolean, _
   ByVal VOpt As System.Boolean, _
   ByVal UvParams As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim UOpt As System.Boolean
Dim VOpt As System.Boolean
Dim UvParams As System.Object
Dim value As System.Boolean

value = instance.CreateBoundedSurface(UOpt, VOpt, UvParams)
```

### C#

```csharp
System.bool CreateBoundedSurface(
   System.bool UOpt,
   System.bool VOpt,
   System.object UvParams
)
```

### C++/CLI

```cpp
System.bool CreateBoundedSurface(
   System.bool UOpt,
   System.bool VOpt,
   System.Object^ UvParams
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UOpt`:
- `VOpt`:
- `UvParams`:

## VBA Syntax

See [Body::CreateBoundedSurface](ms-its:sldworksapivb6.chm::/sldworks~Body~CreateBoundedSurface.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
