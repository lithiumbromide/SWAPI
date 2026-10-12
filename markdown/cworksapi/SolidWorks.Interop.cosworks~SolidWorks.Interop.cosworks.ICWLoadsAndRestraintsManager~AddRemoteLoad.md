---
title: "AddRemoteLoad Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddRemoteLoad"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddRemoteLoad.html"
---

# AddRemoteLoad Method (ICWLoadsAndRestraintsManager)

Creates a remote load of the specified type at the specified location.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddRemoteLoad( _
   ByVal NLoadType As System.Integer, _
   ByVal DispArray As System.Object, _
   ByVal NLocationUnits As System.Integer, _
   ByVal DXValue As System.Double, _
   ByVal DYValue As System.Double, _
   ByVal DZValue As System.Double, _
   ByRef ErrorCode As System.Integer _
) As CWRemoteLoad
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim NLoadType As System.Integer
Dim DispArray As System.Object
Dim NLocationUnits As System.Integer
Dim DXValue As System.Double
Dim DYValue As System.Double
Dim DZValue As System.Double
Dim ErrorCode As System.Integer
Dim value As CWRemoteLoad

value = instance.AddRemoteLoad(NLoadType, DispArray, NLocationUnits, DXValue, DYValue, DZValue, ErrorCode)
```

### C#

```csharp
CWRemoteLoad AddRemoteLoad(
   System.int NLoadType,
   System.object DispArray,
   System.int NLocationUnits,
   System.double DXValue,
   System.double DYValue,
   System.double DZValue,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWRemoteLoad^ AddRemoteLoad(
   System.int NLoadType,
   System.Object^ DispArray,
   System.int NLocationUnits,
   System.double DXValue,
   System.double DYValue,
   System.double DZValue,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NLoadType`: Type of restraint or load as defined in [swsRemoteLoadType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsRemoteLoadType_e.html)
- `DispArray`:

  | If NLoadType is ... | Then DispArray is an array of ... |
  | --- | --- |
  | swsRemoteLoadType_e .swsRemoteLoadType_RigidLoadOrMass - or - swsRemoteLoadType_e .swsRemoteLoadType_RigidDisplacement | Faces, edges, or vertices |
  | swsRemoteLoadType_e .swsRemoteLoadType_DirectLoad - or - swsRemoteLoadType_e .swsRemoteLoadType_DirectDisplacement | Faces |
- `NLocationUnits`: Units as defined in [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)
- `DXValue`: X-coordinate of the point of application of the remote load
- `DYValue`: Y-coordinate of the point of application of the remote load
- `DZValue`: Z-coordinate of the point of application of the remote load
- `ErrorCode`: Error code as defined in [swsLoadsAndRestraintsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLoadsAndRestraintsError_e.html)

### Return Value

[ICWRemoteLoad](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWRemoteLoad.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddRemoteLoad](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddRemoteLoad.html).

## Examples

[Add Remote Load (VBA)](Add_Remote_Load_Example_VB.htm)
[Add Remote Load (VB.NET)](Add_Remote_Load_Example_VBNET.htm)
[Add Remote Load (C#)](Add_Remote_Load_Example_CSharp.htm)

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
