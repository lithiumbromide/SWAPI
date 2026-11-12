---
title: "AddBearingLoad Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddBearingLoad"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddBearingLoad.html"
---

# AddBearingLoad Method (ICWLoadsAndRestraintsManager)

Adds a bearing load.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddBearingLoad( _
   ByVal CoordinateSystem As System.Object, _
   ByVal FirstFace As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWBearingLoad
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim CoordinateSystem As System.Object
Dim FirstFace As System.Object
Dim ErrorCode As System.Integer
Dim value As CWBearingLoad

value = instance.AddBearingLoad(CoordinateSystem, FirstFace, ErrorCode)
```

### C#

```csharp
CWBearingLoad AddBearingLoad(
   System.object CoordinateSystem,
   System.object FirstFace,
   ref System.int ErrorCode
)
```

### C++/CLI

```cpp
CWBearingLoad^ AddBearingLoad(
   System.Object^ CoordinateSystem,
   System.Object^ FirstFace,
   System.int% ErrorCode
)
```

### Parameters

- `CoordinateSystem`: Coordinate system (see **Remarks**)
- `FirstFace`: Array of cylindrical faces or circular shell edges (see **Remarks**)
- `ErrorCode`: Error as defined in [swsLoadsAndRestraintsManagerBearingLoadError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLoadsAndRestraintsManagerBearingLoadError_e.html)

### Return Value

[Bearing load](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBearingLoad.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddBearingLoad](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddBearingLoad.html).

## Examples

[Add Bearing Load (VBA)](Add_Bearing_Load_Example_VB.htm)
[Add Bearing Load (VB.NET)](Add_Bearing_Load_Example_VBNET.htm)
[Add Bearing Load (C#)](Add_Bearing_Load_Example_CSharp.htm)

## Remarks

The Z-axis of CoordinateSystem must coincide with the axes of the faces in the FirstFace array.

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
