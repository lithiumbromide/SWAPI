---
title: "AddForce Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddForce"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddForce.html"
---

# AddForce Method (ICWLoadsAndRestraintsManager)

Obsolete. Superseded by [ICWLoadsAndRestraintsManager::AddForce2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWLoadsAndRestraintsManager~AddForce2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddForce( _
   ByVal NForceType As System.Integer, _
   ByVal DispArray As System.Object, _
   ByVal RefGeom As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWForce
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim NForceType As System.Integer
Dim DispArray As System.Object
Dim RefGeom As System.Object
Dim ErrorCode As System.Integer
Dim value As CWForce

value = instance.AddForce(NForceType, DispArray, RefGeom, ErrorCode)
```

### C#

```csharp
CWForce AddForce(
   System.int NForceType,
   System.object DispArray,
   System.object RefGeom,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWForce^ AddForce(
   System.int NForceType,
   System.Object^ DispArray,
   System.Object^ RefGeom,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NForceType`: Type of force as defined in [swsForceType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsForceType_e.html)
- `DispArray`: Array of entities (faces, edges, vertices, or points) to which to apply force
- `RefGeom`: Reference geometry entity to specify direction (see **Remarks**)
- `ErrorCode`: Error as defined in [swsForceError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsForceError_e.html)

### Return Value

[Force](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWForce.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddForce](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddForce.html).

## Remarks

Pass null in RefGeom if reference geometry is not used.

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2008, SP1.0
