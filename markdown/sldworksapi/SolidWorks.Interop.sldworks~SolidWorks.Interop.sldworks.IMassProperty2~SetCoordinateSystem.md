---
title: "SetCoordinateSystem Method (IMassProperty2)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty2"
member: "SetCoordinateSystem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~SetCoordinateSystem.html"
---

# SetCoordinateSystem Method (IMassProperty2)

Sets the coordinate system to use when calculating mass properties for this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCoordinateSystem( _
   ByVal Coords As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty2
Dim Coords As System.Object
Dim value As System.Boolean

value = instance.SetCoordinateSystem(Coords)
```

### C#

```csharp
System.bool SetCoordinateSystem(
   System.object Coords
)
```

### C++/CLI

```cpp
System.bool SetCoordinateSystem(
   System.Object^ Coords
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Coords`: [Math transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

### Return Value

True if the coordinate system is set, false if not

## VBA Syntax

See [MassProperty2::SetCoordinateSystem](ms-its:sldworksapivb6.chm::/sldworks~MassProperty2~SetCoordinateSystem.html).

## See Also

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html)
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
