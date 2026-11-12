---
title: "AddCentrifugalForce Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddCentrifugalForce"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddCentrifugalForce.html"
---

# AddCentrifugalForce Method (ICWLoadsAndRestraintsManager)

Creates a centrifugal force.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddCentrifugalForce( _
   ByVal DispEntity As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWCentriFugalForce
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim DispEntity As System.Object
Dim ErrorCode As System.Integer
Dim value As CWCentriFugalForce

value = instance.AddCentrifugalForce(DispEntity, ErrorCode)
```

### C#

```csharp
CWCentriFugalForce AddCentrifugalForce(
   System.object DispEntity,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWCentriFugalForce^ AddCentrifugalForce(
   System.Object^ DispEntity,
   [Out] System.int ErrorCode
)
```

### Parameters

- `DispEntity`: Reference geometry (axis, edge, or cylindrical face) to specify direction
- `ErrorCode`: Error as defined in [swsCentrifugalForceError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsCentrifugalForceError_e.html)

### Return Value

[Centrifugal force](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWCentriFugalForce.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddCentrifugalForce](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddCentrifugalForce.html).

## Examples

[Add Centrifugal Load (VBA)](Add_Centrifugal_Load_Example_VB.htm)
[Add Centrifugal Load (VB.NET)](Add_Centrifugal_Load_Example_VBNET.htm)
[Add Centrifugal Load (C#)](Add_Centrifugal_Load_Example_CSharp.htm)

## Remarks

The density material property must be specified to consider the effect of centrifugal loads.

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
