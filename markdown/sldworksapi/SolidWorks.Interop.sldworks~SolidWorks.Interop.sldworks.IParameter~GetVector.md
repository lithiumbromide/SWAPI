---
title: "GetVector Method (IParameter)"
project: "SOLIDWORKS API Help"
interface: "IParameter"
member: "GetVector"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~GetVector.html"
---

# GetVector Method (IParameter)

Extracts information of type vector from a parameter.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetVector( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IParameter
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double

instance.GetVector(X, Y, Z)
```

### C#

```csharp
void GetVector(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### C++/CLI

```cpp
void GetVector(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: x vector value stored on the parameter
- `Y`: y vector value stored on the parameter
- `Z`: z vector value stored on the parameter

## VBA Syntax

See [Parameter::GetVector](ms-its:sldworksapivb6.chm::/sldworks~Parameter~GetVector.html).

## See Also

[IParameter Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.html)
[IParameter Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter_members.html)
[IParameter::GetVectorVB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~GetVectorVB.html)
[IParameter::SetVector2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~SetVector2.html)
