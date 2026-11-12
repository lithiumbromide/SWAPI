---
title: "AddRestraint Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddRestraint"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddRestraint.html"
---

# AddRestraint Method (ICWLoadsAndRestraintsManager)

Creates a restraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddRestraint( _
   ByVal NRestraintType As System.Integer, _
   ByVal DispArray As System.Object, _
   ByVal RefGeom As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWRestraint
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim NRestraintType As System.Integer
Dim DispArray As System.Object
Dim RefGeom As System.Object
Dim ErrorCode As System.Integer
Dim value As CWRestraint

value = instance.AddRestraint(NRestraintType, DispArray, RefGeom, ErrorCode)
```

### C#

```csharp
CWRestraint AddRestraint(
   System.int NRestraintType,
   System.object DispArray,
   System.object RefGeom,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWRestraint^ AddRestraint(
   System.int NRestraintType,
   System.Object^ DispArray,
   System.Object^ RefGeom,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NRestraintType`: Type of restraint as defined in [swsRestraintType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsRestraintType_e.html)
- `DispArray`: Array of entities to which to apply the restraint
- `RefGeom`: Reference geometry entity for direction; valid only if NRestraintType is set to swsRestraintType_e.swsRestraintTypeReferenceGeometry
- `ErrorCode`: Error code as defined in [swsRestraintError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsRestraintError_e.html)

### Return Value

[Restraint](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWRestraint.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddRestraint](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddRestraint.html).

## Examples

[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
