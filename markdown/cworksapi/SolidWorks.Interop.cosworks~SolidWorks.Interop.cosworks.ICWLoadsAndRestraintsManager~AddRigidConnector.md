---
title: "AddRigidConnector Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddRigidConnector"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddRigidConnector.html"
---

# AddRigidConnector Method (ICWLoadsAndRestraintsManager)

Adds a rigid connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddRigidConnector( _
   ByVal PersistIDFaceArray As System.Object, _
   ByVal PersistIDTargetArray As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWRigidConnector
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim PersistIDFaceArray As System.Object
Dim PersistIDTargetArray As System.Object
Dim ErrorCode As System.Integer
Dim value As CWRigidConnector

value = instance.AddRigidConnector(PersistIDFaceArray, PersistIDTargetArray, ErrorCode)
```

### C#

```csharp
CWRigidConnector AddRigidConnector(
   System.object PersistIDFaceArray,
   System.object PersistIDTargetArray,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWRigidConnector^ AddRigidConnector(
   System.Object^ PersistIDFaceArray,
   System.Object^ PersistIDTargetArray,
   [Out] System.int ErrorCode
)
```

### Parameters

- `PersistIDFaceArray`: Array of objects of the faces from a solid body
- `PersistIDTargetArray`: Array of objects of the faces from the target solid body
- `ErrorCode`: Error as defined in [swsRigidConnectorError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsRigidConnectorError_e.html)

### Return Value

[Rigid connector](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWRigidConnector.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddRigidConnector](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddRigidConnector.html).

## Examples

[Add Rigid Connector (VBA)](Add_Rigid_Connector_Example_VB.htm)
[Add Rigid Connector (VB.NET)](Add_Rigid_Connector_Example_VBNET.htm)
[Add Rigid Connector (C#)](Add_Rigid_Connector_Example_CSharp.htm)

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
