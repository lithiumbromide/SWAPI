---
title: "SetPlyParameters Method (ICWCompositeShellOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions"
member: "SetPlyParameters"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~SetPlyParameters.html"
---

# SetPlyParameters Method (ICWCompositeShellOptions)

Obsolete. Superseded by [ICWCompositeShellOptions::SetPlyParameters2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~SetPlyParameters2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPlyParameters( _
   ByVal NPly As System.Integer, _
   ByVal DThickness As System.Double, _
   ByVal DAngle As System.Double, _
   ByVal PMaterial As CWMaterial _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCompositeShellOptions
Dim NPly As System.Integer
Dim DThickness As System.Double
Dim DAngle As System.Double
Dim PMaterial As CWMaterial
Dim value As System.Integer

value = instance.SetPlyParameters(NPly, DThickness, DAngle, PMaterial)
```

### C#

```csharp
System.int SetPlyParameters(
   System.int NPly,
   System.double DThickness,
   System.double DAngle,
   CWMaterial PMaterial
)
```

### C++/CLI

```cpp
System.int SetPlyParameters(
   System.int NPly,
   System.double DThickness,
   System.double DAngle,
   CWMaterial^ PMaterial
)
```

### Parameters

- `NPly`: Index of ply (see **Remarks**)
- `DThickness`: Thickness of ply
- `DAngle`: Angle of ply (see **Remarks**)
- `PMaterial`: [ICWMaterial](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)

### Return Value

Error code as defined in [swsCompositeShellOptionsError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCompositeShellOptionsError_e.html)

## VBA Syntax

See [CWCompositeShellOptions::SetPlyParameters](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCompositeShellOptions~SetPlyParameters.html).

## Remarks

Call [ICWCompositeShellOptions::GetTotalPlies](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~GetTotalPlies.html) to set NPly.

| If ICWCompositeShellOptions::PlyRelativeAngle is set to... | Then DAngle's value is... |
| --- | --- |
| 1 | Relative to the angle of ply 1 |
| 0 | Absolute |

## See Also

[ICWCompositeShellOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
[ICWCompositeShellOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions_members.html)
[ICWCompositeShellOptions::GetPlyParameters Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~GetPlyParameters.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
