---
title: "SetEntityForVelocityDirection Method (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "SetEntityForVelocityDirection"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~SetEntityForVelocityDirection.html"
---

# SetEntityForVelocityDirection Method (ICWDropTestSetup)

Obsolete. Superseded by [ICWDropTestSetup::SetEntityForVelocityDirection2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~SetEntityForVelocityDirection2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetEntityForVelocityDirection( _
   ByVal DispEntity As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim DispEntity As System.Object
Dim value As System.Integer

value = instance.SetEntityForVelocityDirection(DispEntity)
```

### C#

```csharp
System.int SetEntityForVelocityDirection(
   System.object DispEntity
)
```

### C++/CLI

```cpp
System.int SetEntityForVelocityDirection(
   System.Object^ DispEntity
)
```

### Parameters

- `DispEntity`: Face, edge, or plane geometry reference (see **Remarks**)

### Return Value

Error code as defined in [swsDropTestSetUpError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDropTestSetUpError_e.html) (see **Remarks**)

## VBA Syntax

See [CWDropTestSetup::SetEntityForVelocityDirection](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestSetup~SetEntityForVelocityDirection.html).

## Remarks

This method is valid only if [ICWDropTestSetup::DropType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup~DropType.html) = swsDropType_e.swsDropType_VelocityAtImpact.

If the reference entity is a plane or planar face, the velocity is applied in the direction normal to the reference entity.

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)
[ICWDropTestSetup::FlipVelocityDirection Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~FlipVelocityDirection.html)
[ICWDropTestSetup::Velocity Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~Velocity.html)
[ICWDropTestSetup::VelocityUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~VelocityUnit.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
