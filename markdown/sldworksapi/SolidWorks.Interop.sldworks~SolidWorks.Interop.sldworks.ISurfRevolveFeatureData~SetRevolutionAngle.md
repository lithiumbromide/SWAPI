---
title: "SetRevolutionAngle Method (ISurfRevolveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfRevolveFeatureData"
member: "SetRevolutionAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData~SetRevolutionAngle.html"
---

# SetRevolutionAngle Method (ISurfRevolveFeatureData)

Sets the angle for this surface revolve feature in Direction 1 or Direction 2.

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
Dim instance As ISurfRevolveFeatureData
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

- `Forward`: True sets the angle in Direction 1, false sets the angle in Direction 2
- `Angle`: Angle of the revolution

## VBA Syntax

See [SurfRevolveFeatureData::SetRevolutionAngle](ms-its:sldworksapivb6.chm::/sldworks~SurfRevolveFeatureData~SetRevolutionAngle.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfRevolveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData.html)
[ISurfRevolveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData_members.html)
[ISurfRevolveFeatureData::GetRevolutionAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData~GetRevolutionAngle.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
