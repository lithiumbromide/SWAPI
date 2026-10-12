---
title: "SetEntityForVelocityDirection2 Method (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "SetEntityForVelocityDirection2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~SetEntityForVelocityDirection2.html"
---

# SetEntityForVelocityDirection2 Method (ICWDropTestSetup)

Sets the face, edge, or plane reference to determine the direction of the velocity at impact.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetEntityForVelocityDirection2( _
   ByVal DispEntity As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim DispEntity As System.Object
Dim value As System.Boolean

value = instance.SetEntityForVelocityDirection2(DispEntity)
```

### C#

```csharp
System.bool SetEntityForVelocityDirection2(
   System.object DispEntity
)
```

### C++/CLI

```cpp
System.bool SetEntityForVelocityDirection2(
   System.Object^ DispEntity
)
```

### Parameters

- `DispEntity`: Face, edge, or plane geometry reference (see **Remarks**)

## Remarks

This method is valid only if [ICWDropTestSetup::DropType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup~DropType.html) = swsDropType_e.swsDropType_VelocityAtImpact.

If the reference entity is a plane or planar face, the velocity is applied in the direction normal to the reference entity.

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
