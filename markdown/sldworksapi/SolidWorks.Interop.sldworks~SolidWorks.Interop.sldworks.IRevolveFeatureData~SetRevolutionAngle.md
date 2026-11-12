---
title: "SetRevolutionAngle Method (IRevolveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData"
member: "SetRevolutionAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData~SetRevolutionAngle.html"
---

# SetRevolutionAngle Method (IRevolveFeatureData)

Obsolete. Superseded by [IRevolveFeatureData2::SetRevolutionAngle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevolveFeatureData2~SetRevolutionAngle.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetRevolutionAngle( _
   ByVal Forward As System.Boolean, _
   ByVal Angle As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRevolveFeatureData
Dim Forward As System.Boolean
Dim Angle As System.Double

instance.SetRevolutionAngle(Forward, Angle)
```

### C#

```csharp
void SetRevolutionAngle(
   System.bool Forward,
   System.double Angle
)
```

### C++/CLI

```cpp
void SetRevolutionAngle(
   System.bool Forward,
   System.double Angle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`:
- `Angle`:

## VBA Syntax

See [RevolveFeatureData::SetRevolutionAngle](ms-its:sldworksapivb6.chm::/sldworks~RevolveFeatureData~SetRevolutionAngle.html).

## See Also

[IRevolveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData.html)
[IRevolveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData_members.html)
