---
title: "VPeriodicity Property (IBSurfParamData)"
project: "SOLIDWORKS API Help"
interface: "IBSurfParamData"
member: "VPeriodicity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~VPeriodicity.html"
---

# VPeriodicity Property (IBSurfParamData)

Gets whether the surface is periodic in the V direction.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property VPeriodicity As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBSurfParamData
Dim value As System.Boolean

value = instance.VPeriodicity
```

### C#

```csharp
System.bool VPeriodicity {get;}
```

### C++/CLI

```cpp
property System.bool VPeriodicity {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if surface is periodic in V direction, false if not

## VBA Syntax

See [BSurfParamData::VPeriodicity](ms-its:sldworksapivb6.chm::/sldworks~BSurfParamData~VPeriodicity.html).

## Examples

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

## See Also

[IBSurfParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData.html)
[IBSurfParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData_members.html)
[IBSurfParamData::UPeriodicity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~UPeriodicity.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
