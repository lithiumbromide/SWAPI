---
title: "SetPlyParameters2 Method (ICWCompositeShellOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions"
member: "SetPlyParameters2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~SetPlyParameters2.html"
---

# SetPlyParameters2 Method (ICWCompositeShellOptions)

Sets the thickness, angle, and material for the specified ply.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPlyParameters2( _
   ByVal NPly As System.Integer, _
   ByVal DThickness As System.Double, _
   ByVal DAngle As System.Double, _
   ByVal SMaterialLibName As System.String, _
   ByVal SMaterialName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCompositeShellOptions
Dim NPly As System.Integer
Dim DThickness As System.Double
Dim DAngle As System.Double
Dim SMaterialLibName As System.String
Dim SMaterialName As System.String
Dim value As System.Integer

value = instance.SetPlyParameters2(NPly, DThickness, DAngle, SMaterialLibName, SMaterialName)
```

### C#

```csharp
System.int SetPlyParameters2(
   System.int NPly,
   System.double DThickness,
   System.double DAngle,
   System.string SMaterialLibName,
   System.string SMaterialName
)
```

### C++/CLI

```cpp
System.int SetPlyParameters2(
   System.int NPly,
   System.double DThickness,
   System.double DAngle,
   System.String^ SMaterialLibName,
   System.String^ SMaterialName
)
```

### Parameters

- `NPly`: Index of ply (see **Remarks**)
- `DThickness`: Thickness of ply
- `DAngle`: Angle of ply (see **Remarks**)
- `SMaterialLibName`: Material library name
- `SMaterialName`: Material name

### Return Value

Error code as defined in [swsCompositeShellOptionsError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCompositeShellOptionsError_e.html)

## VBA Syntax

See [CWCompositeShellOptions::SetPlyParameters2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCompositeShellOptions~SetPlyParameters2.html).

## Examples

See the [ICWCompositeShellOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html) examples.

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

SOLIDWORKS Simulation API 2017 SP1
