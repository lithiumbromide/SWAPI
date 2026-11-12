---
title: "GetJointGroup Method (ICWBeamManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBeamManager"
member: "GetJointGroup"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamManager~GetJointGroup.html"
---

# GetJointGroup Method (ICWBeamManager)

Gets the joints in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetJointGroup( _
   ByRef ErrorCode As System.Integer _
) As CWJoints
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBeamManager
Dim ErrorCode As System.Integer
Dim value As CWJoints

value = instance.GetJointGroup(ErrorCode)
```

### C#

```csharp
CWJoints GetJointGroup(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWJoints^ GetJointGroup(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: 0 if successful, 1 if not

### Return Value

[Joints](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWJoints.html)

## VBA Syntax

See [CWBeamManager::GetJointGroup](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBeamManager~GetJointGroup.html).

## Examples

[Get and Set Beams and Joints (C#)](Get_and_Set_Beams_and_Joints_Example_CSharp.htm)
[Get and Set Beams and Joints (VB.NET)](Get_and_Set_Beams_and_Joints_Example_VBNET.htm)
[Get and Set Beams and Joints (VBA)](Get_and_Set_Beams_and_Joints_Example_VB.htm)

## See Also

[ICWBeamManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamManager.html)
[ICWBeamManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamManager_members.html)
[ICWBeamBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)
[ICWBeamManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamManager.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
