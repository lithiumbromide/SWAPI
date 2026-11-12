---
title: "IGetMassProperties Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IGetMassProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IGetMassProperties.html"
---

# IGetMassProperties Method (IBody)

Obsolete. Superseded by [IBody2::IGetMassProperties.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IGetMassProperties.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMassProperties( _
   ByVal Density As System.Double _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim Density As System.Double
Dim value As System.Double

value = instance.IGetMassProperties(Density)
```

### C#

```csharp
System.double IGetMassProperties(
   System.double Density
)
```

### C++/CLI

```cpp
System.double IGetMassProperties(
   System.double Density
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Density`:

## VBA Syntax

See [Body::IGetMassProperties](ms-its:sldworksapivb6.chm::/sldworks~Body~IGetMassProperties.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
