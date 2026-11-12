---
title: "SetProjectionEntity Method (IMeasure)"
project: "SOLIDWORKS API Help"
interface: "IMeasure"
member: "SetProjectionEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~SetProjectionEntity.html"
---

# SetProjectionEntity Method (IMeasure)

Sets the face or plane to which to project the measured distance.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetProjectionEntity( _
   ByVal Entity As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMeasure
Dim Entity As System.Object
Dim value As System.Boolean

value = instance.SetProjectionEntity(Entity)
```

### C#

```csharp
System.bool SetProjectionEntity(
   System.object Entity
)
```

### C++/CLI

```cpp
System.bool SetProjectionEntity(
   System.Object^ Entity
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entity`: [Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) or [plane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html)

### Return Value

True if Entity is set, false if not

## VBA Syntax

See [Measure::SetProjectionEntity](ms-its:sldworksapivb6.chm::/Sldworks~Measure~SetProjectionEntity.html).

## See Also

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.html)
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html)
[IMeasure::Projection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Projection.html)
[IMeasure::ProjectionOption Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~ProjectionOption.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
