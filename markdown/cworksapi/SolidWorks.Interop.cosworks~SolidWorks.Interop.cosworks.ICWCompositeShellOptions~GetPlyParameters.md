---
title: "GetPlyParameters Method (ICWCompositeShellOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions"
member: "GetPlyParameters"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~GetPlyParameters.html"
---

# GetPlyParameters Method (ICWCompositeShellOptions)

Gets the thickness, angle, and material for the specified ply.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPlyParameters( _
   ByVal NPly As System.Integer, _
   ByRef DThickness As System.Double, _
   ByRef DAngle As System.Double, _
   ByRef NErrorCode As System.Integer _
) As CWMaterial
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCompositeShellOptions
Dim NPly As System.Integer
Dim DThickness As System.Double
Dim DAngle As System.Double
Dim NErrorCode As System.Integer
Dim value As CWMaterial

value = instance.GetPlyParameters(NPly, DThickness, DAngle, NErrorCode)
```

### C#

```csharp
CWMaterial GetPlyParameters(
   System.int NPly,
   out System.double DThickness,
   out System.double DAngle,
   out System.int NErrorCode
)
```

### C++/CLI

```cpp
CWMaterial^ GetPlyParameters(
   System.int NPly,
   [Out] System.double DThickness,
   [Out] System.double DAngle,
   [Out] System.int NErrorCode
)
```

### Parameters

- `NPly`: Index of ply (see **Remarks**)
- `DThickness`: Thickness of ply
- `DAngle`: Angle of ply (see **Remarks**)
- `NErrorCode`: Error code as defined in [swsCompositeShellOptionsError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCompositeShellOptionsError_e.html)

### Return Value

[ICWMaterial](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)

## VBA Syntax

See [CWCompositeShellOptions::GetPlyParameters](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCompositeShellOptions~GetPlyParameters.html).

## Remarks

Call [ICWCompositeShellOptions::GetTotalPlies](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~GetTotalPlies.html) to set NPly.

| If ICWCompositeShellOptions::PlyRelativeAngle is set to... | Then DAngle's value is... |
| --- | --- |
| 1 | Relative to the angle of ply 1 |
| 0 | Absolute |

## See Also

[ICWCompositeShellOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
[ICWCompositeShellOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions_members.html)
[ICWCompositeShellOptions::SetPlyParameters Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~SetPlyParameters.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
