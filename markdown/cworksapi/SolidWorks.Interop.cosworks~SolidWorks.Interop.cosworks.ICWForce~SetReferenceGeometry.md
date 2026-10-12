---
title: "SetReferenceGeometry Method (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "SetReferenceGeometry"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetReferenceGeometry.html"
---

# SetReferenceGeometry Method (ICWForce)

Sets the reference entity along whose direction this force is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetReferenceGeometry( _
   ByVal RefEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWForce
Dim RefEntity As System.Object

instance.SetReferenceGeometry(RefEntity)
```

### C#

```csharp
void SetReferenceGeometry(
   System.object RefEntity
)
```

### C++/CLI

```cpp
void SetReferenceGeometry(
   System.Object^ RefEntity
)
```

### Parameters

- `RefEntity`: Reference direction entity (see **Remarks**)

## VBA Syntax

See [CWForce::SetReferenceGeometry](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~SetReferenceGeometry.html).

## Remarks

This method is valid only if [ICWForce::ForceType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~ForceType.html) is set to [swsForceType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsForceType_e.html).swsForceTypeForceOrMoment or swsForceType_e.swsForceTypeTorque.

For forces or moments, specify RefEntity with a face, plane, or edge. For torques, specify RefEntity with a cylindrical face or axis.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)
[ICWForce::NormalForceOrTorqueValue Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~NormalForceOrTorqueValue.html)
[ICWForce::Unit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~Unit.html)
[ICWForce::GetForceComponentValues Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~GetForceComponentValues.html)
[ICWForce::GetMomentComponentValues Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~GetMomentComponentValues.html)
[ICWForce::InsertEntity Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~InsertEntity.html)
[ICWForce::SetForceComponentValues Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetForceComponentValues.html)
[ICWForce::SetMomentComponentValues Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetMomentComponentValues.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
