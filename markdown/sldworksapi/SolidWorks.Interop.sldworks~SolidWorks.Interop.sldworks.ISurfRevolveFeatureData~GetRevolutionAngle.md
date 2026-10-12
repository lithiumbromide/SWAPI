---
title: "GetRevolutionAngle Method (ISurfRevolveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfRevolveFeatureData"
member: "GetRevolutionAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData~GetRevolutionAngle.html"
---

# GetRevolutionAngle Method (ISurfRevolveFeatureData)

Gets the angle for this surface revolve feature in Direction 1 or Direction 2.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRevolutionAngle( _
   ByVal Forward As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfRevolveFeatureData
Dim Forward As System.Boolean
Dim value As System.Double

value = instance.GetRevolutionAngle(Forward)
```

### C#

```csharp
System.double GetRevolutionAngle(
   System.bool Forward
)
```

### C++/CLI

```cpp
System.double GetRevolutionAngle(
   System.bool Forward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True gets the angle in Direction 1, false gets the angle in Direction 2

### Return Value

Angle of the revolution

## VBA Syntax

See [SurfRevolveFeatureData::GetRevolutionAngle](ms-its:sldworksapivb6.chm::/sldworks~SurfRevolveFeatureData~GetRevolutionAngle.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfRevolveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData.html)
[ISurfRevolveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData_members.html)
[ISurfRevolveFeatureData::SetRevolutionAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData~SetRevolutionAngle.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
