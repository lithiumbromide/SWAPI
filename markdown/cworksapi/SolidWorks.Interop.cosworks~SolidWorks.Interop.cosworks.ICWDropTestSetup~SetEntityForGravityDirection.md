---
title: "SetEntityForGravityDirection Method (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "SetEntityForGravityDirection"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~SetEntityForGravityDirection.html"
---

# SetEntityForGravityDirection Method (ICWDropTestSetup)

Obsolete. Superseded by [ICWDropTestSetup::SetEntityForGravityDirection2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~SetEntityForGravityDirection2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetEntityForGravityDirection( _
   ByVal DispEntity As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim DispEntity As System.Object
Dim value As System.Integer

value = instance.SetEntityForGravityDirection(DispEntity)
```

### C#

```csharp
System.int SetEntityForGravityDirection(
   System.object DispEntity
)
```

### C++/CLI

```cpp
System.int SetEntityForGravityDirection(
   System.Object^ DispEntity
)
```

### Parameters

- `DispEntity`: Face, edge, or plane geometry reference (see **Remarks**)

## VBA Syntax

See [CWDropTestSetup::SetEntityForGravityDirection](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestSetup~SetEntityForGravityDirection.html).

## Remarks

If the reference entity is a plane or planar face, the velocity is applied in the direction normal to the reference entity.

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)
[ICWDropTestSetup::FlipGravityDirection Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~FlipGravityDirection.html)
[ICWDropTestSetup::Gravity Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~Gravity.html)
[ICWDropTestSetup::GravityUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~GravityUnit.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
