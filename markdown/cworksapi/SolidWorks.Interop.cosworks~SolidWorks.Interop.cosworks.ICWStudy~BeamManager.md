---
title: "BeamManager Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "BeamManager"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~BeamManager.html"
---

# BeamManager Property (ICWStudy)

Gets the beam manager.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BeamManager As CWBeamManager
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWBeamManager

value = instance.BeamManager
```

### C#

```csharp
CWBeamManager BeamManager {get;}
```

### C++/CLI

```cpp
property CWBeamManager^ BeamManager {
   CWBeamManager^ get();
}
```

### Property Value

[Beam manager](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBeamManager.html)

## VBA Syntax

See [CWStudy::BeamManager](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~BeamManager.html).

## Examples

[Get and Set Beams and Joints (C#)](Get_and_Set_Beams_and_Joints_Example_CSharp.htm)
[Get and Set Beams and Joints (VB.NET)](Get_and_Set_Beams_and_Joints_Example_VBNET.htm)
[Get and Set Beams and Joints (VBA)](Get_and_Set_Beams_and_Joints_Example_VB.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
