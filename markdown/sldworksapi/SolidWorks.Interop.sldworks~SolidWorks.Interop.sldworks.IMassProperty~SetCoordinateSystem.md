---
title: "SetCoordinateSystem Method (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "SetCoordinateSystem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetCoordinateSystem.html"
---

# SetCoordinateSystem Method (IMassProperty)

Sets the coordinate system to use when calculating mass properties for this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCoordinateSystem( _
   ByVal Coords As MathTransform _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim Coords As MathTransform
Dim value As System.Boolean

value = instance.SetCoordinateSystem(Coords)
```

### C#

```csharp
System.bool SetCoordinateSystem(
   MathTransform Coords
)
```

### C++/CLI

```cpp
System.bool SetCoordinateSystem(
   MathTransform^ Coords
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Coords`: [Math transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

### Return Value

True if the coordinate system is set, false if not

## VBA Syntax

See [MassProperty::SetCoordinateSystem](ms-its:sldworksapivb6.chm::/sldworks~MassProperty~SetCoordinateSystem.html).

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IModelDoc2::GetCurrentCoordinateSystemName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetCurrentCoordinateSystemName.html)
[IModelDoc2::InsertCoordinateSystem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCoordinateSystem.html)
[IModelDocExtension::GetCoordinateSystemTransformByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCoordinateSystemTransformByName.html)

## Availability

SOLIDWORKS 2003 SP2, Revision Number 11.2
