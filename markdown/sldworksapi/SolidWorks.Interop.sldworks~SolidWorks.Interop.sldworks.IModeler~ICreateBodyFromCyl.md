---
title: "ICreateBodyFromCyl Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreateBodyFromCyl"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCyl.html"
---

# ICreateBodyFromCyl Method (IModeler)

Obsolete. Superseded by [IModeler::ICreateBodyFromCyl2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateBodyFromCyl2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateBodyFromCyl( _
   ByRef CylDimArray As System.Double _
) As Body
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim CylDimArray As System.Double
Dim value As Body

value = instance.ICreateBodyFromCyl(CylDimArray)
```

### C#

```csharp
Body ICreateBodyFromCyl(
   ref System.double CylDimArray
)
```

### C++/CLI

```cpp
Body^ ICreateBodyFromCyl(
   System.double% CylDimArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CylDimArray`:

## VBA Syntax

See [Modeler::ICreateBodyFromCyl](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreateBodyFromCyl.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
