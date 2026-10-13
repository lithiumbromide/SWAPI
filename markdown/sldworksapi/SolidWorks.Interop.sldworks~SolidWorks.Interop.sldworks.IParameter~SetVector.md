---
title: "SetVector Method (IParameter)"
project: "SOLIDWORKS API Help"
interface: "IParameter"
member: "SetVector"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~SetVector.html"
---

# SetVector Method (IParameter)

Obsolete. Superseded by [IParameter::SetVector2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IParameter~SetVector2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetVector( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IParameter
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean

value = instance.SetVector(X, Y, Z)
```

### C#

```csharp
System.bool SetVector(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool SetVector(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`:
- `Y`:
- `Z`:

## VBA Syntax

See [Parameter::SetVector](ms-its:sldworksapivb6.chm::/sldworks~Parameter~SetVector.html).

## See Also

[IParameter Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.html)
[IParameter Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter_members.html)
