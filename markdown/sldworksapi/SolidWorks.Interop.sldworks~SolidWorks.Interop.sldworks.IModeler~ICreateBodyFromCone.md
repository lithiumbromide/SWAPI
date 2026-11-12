---
title: "ICreateBodyFromCone Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreateBodyFromCone"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCone.html"
---

# ICreateBodyFromCone Method (IModeler)

Obsolete. Superseded by [IModeler::ICreateBodyFromCone2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateBodyFromCone2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateBodyFromCone( _
   ByRef ConeDimArray As System.Double _
) As Body
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim ConeDimArray As System.Double
Dim value As Body

value = instance.ICreateBodyFromCone(ConeDimArray)
```

### C#

```csharp
Body ICreateBodyFromCone(
   ref System.double ConeDimArray
)
```

### C++/CLI

```cpp
Body^ ICreateBodyFromCone(
   System.double% ConeDimArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConeDimArray`:

## VBA Syntax

See [Modeler::ICreateBodyFromCone](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreateBodyFromCone.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
