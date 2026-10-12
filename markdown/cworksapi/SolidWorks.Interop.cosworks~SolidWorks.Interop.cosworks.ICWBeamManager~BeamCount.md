---
title: "BeamCount Property (ICWBeamManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBeamManager"
member: "BeamCount"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamManager~BeamCount.html"
---

# BeamCount Property (ICWBeamManager)

Gets the number of beams in the model.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BeamCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBeamManager
Dim value As System.Integer

value = instance.BeamCount
```

### C#

```csharp
System.int BeamCount {get;}
```

### C++/CLI

```cpp
property System.int BeamCount {
   System.int get();
}
```

### Property Value

Number of beams

## VBA Syntax

See [CWBeamManager::BeamCount](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBeamManager~BeamCount.html).

## Examples

[Get and Set Beams and Joints (C#)](Get_and_Set_Beams_and_Joints_Example_CSharp.htm)
[Get and Set Beams and Joints (VB.NET)](Get_and_Set_Beams_and_Joints_Example_VBNET.htm)
[Get and Set Beams and Joints (VBA)](Get_and_Set_Beams_and_Joints_Example_VB.htm)

## See Also

[ICWBeamManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamManager.html)
[ICWBeamManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamManager_members.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
