---
title: "UPeriodicity Property (IBSurfParamData)"
project: "SOLIDWORKS API Help"
interface: "IBSurfParamData"
member: "UPeriodicity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~UPeriodicity.html"
---

# UPeriodicity Property (IBSurfParamData)

Gets whether the surface is periodic in the U direction.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property UPeriodicity As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBSurfParamData
Dim value As System.Boolean

value = instance.UPeriodicity
```

### C#

```csharp
System.bool UPeriodicity {get;}
```

### C++/CLI

```cpp
property System.bool UPeriodicity {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if surface is periodic in U direction, false if not

## VBA Syntax

See [BSurfParamData::UPeriodicity](ms-its:sldworksapivb6.chm::/sldworks~BSurfParamData~UPeriodicity.html).

## Examples

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

## Remarks

If a surface is periodic in one direction (that is, cylinder, cone, torus (apple and lemon shapes), spheres), then U is the periodic direction.

## See Also

[IBSurfParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData.html)
[IBSurfParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData_members.html)
[IBSurfParamData::VPeriodicity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~VPeriodicity.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
