---
title: "GetMassProperties Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "GetMassProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~GetMassProperties.html"
---

# GetMassProperties Method (IBody)

Obsolete. Superseded by [IBody2::GetMassProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetMassProperties.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMassProperties( _
   ByVal Density As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim Density As System.Double
Dim value As System.Object

value = instance.GetMassProperties(Density)
```

### C#

```csharp
System.object GetMassProperties(
   System.double Density
)
```

### C++/CLI

```cpp
System.Object^ GetMassProperties(
   System.double Density
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Density`:

## VBA Syntax

See [Body::GetMassProperties](ms-its:sldworksapivb6.chm::/sldworks~Body~GetMassProperties.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
