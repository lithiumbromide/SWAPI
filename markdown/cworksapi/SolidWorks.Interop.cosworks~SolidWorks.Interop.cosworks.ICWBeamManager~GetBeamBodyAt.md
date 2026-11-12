---
title: "GetBeamBodyAt Method (ICWBeamManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBeamManager"
member: "GetBeamBodyAt"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamManager~GetBeamBodyAt.html"
---

# GetBeamBodyAt Method (ICWBeamManager)

Gets the specified beam.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBeamBodyAt( _
   ByVal NIndex As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As CWBeamBody
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBeamManager
Dim NIndex As System.Integer
Dim ErrorCode As System.Integer
Dim value As CWBeamBody

value = instance.GetBeamBodyAt(NIndex, ErrorCode)
```

### C#

```csharp
CWBeamBody GetBeamBodyAt(
   System.int NIndex,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWBeamBody^ GetBeamBodyAt(
   System.int NIndex,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NIndex`: 0-based index of the beam to get (see **Remarks**)
- `ErrorCode`: 0 if successful, 1 if no beam at NIndex

### Return Value

[Beam](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBeamBody.html) or null if no beam at NIndex

## VBA Syntax

See [CWBeamManager::GetBeamBodyAt](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBeamManager~GetBeamBodyAt.html).

## Examples

[Get and Set Beams and Joints (C#)](Get_and_Set_Beams_and_Joints_Example_CSharp.htm)
[Get and Set Beams and Joints (VB.NET)](Get_and_Set_Beams_and_Joints_Example_VBNET.htm)
[Get and Set Beams and Joints (VBA)](Get_and_Set_Beams_and_Joints_Example_VB.htm)

## Remarks

Before calling this method, call [ICWBeamManager::BeamCount](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBeamManager~BeamCount.html) to get a valid value for NIndex.

## See Also

[ICWBeamManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamManager.html)
[ICWBeamManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamManager_members.html)
[ICWBeamManager::GetBeamBodyByName Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamManager~GetBeamBodyByName.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
