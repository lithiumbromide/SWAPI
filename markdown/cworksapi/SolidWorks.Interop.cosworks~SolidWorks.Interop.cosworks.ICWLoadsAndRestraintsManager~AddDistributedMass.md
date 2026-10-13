---
title: "AddDistributedMass Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddDistributedMass"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddDistributedMass.html"
---

# AddDistributedMass Method (ICWLoadsAndRestraintsManager)

Creates a distributed mass.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddDistributedMass( _
   ByVal DispArray As System.Object, _
   ByVal NUnits As System.Integer, _
   ByVal DMass As System.Double, _
   ByRef ErrorCode As System.Integer _
) As CWDistributedMass
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim DispArray As System.Object
Dim NUnits As System.Integer
Dim DMass As System.Double
Dim ErrorCode As System.Integer
Dim value As CWDistributedMass

value = instance.AddDistributedMass(DispArray, NUnits, DMass, ErrorCode)
```

### C#

```csharp
CWDistributedMass AddDistributedMass(
   System.object DispArray,
   System.int NUnits,
   System.double DMass,
   ref System.int ErrorCode
)
```

### C++/CLI

```cpp
CWDistributedMass^ AddDistributedMass(
   System.Object^ DispArray,
   System.int NUnits,
   System.double DMass,
   System.int% ErrorCode
)
```

### Parameters

- `DispArray`: Array of faces or shell edges on which to distribute the mass
- `NUnits`: Units as defined in [swsUnitSystem_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnitSystem_e.html)
- `DMass`: Mass to distribute
- `ErrorCode`: Error code as defined in [swsDistributedMassError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDistributedMassError_e.html)

### Return Value

[ICWDistributedMass](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDistributedMass.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddDistributedMass](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddDistributedMass.html).

## Examples

[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
