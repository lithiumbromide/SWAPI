---
title: "AddPressure Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddPressure"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddPressure.html"
---

# AddPressure Method (ICWLoadsAndRestraintsManager)

Creates pressure.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddPressure( _
   ByVal NPressureType As System.Integer, _
   ByVal DispArray As System.Object, _
   ByVal RegGeom As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWPressure
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim NPressureType As System.Integer
Dim DispArray As System.Object
Dim RegGeom As System.Object
Dim ErrorCode As System.Integer
Dim value As CWPressure

value = instance.AddPressure(NPressureType, DispArray, RegGeom, ErrorCode)
```

### C#

```csharp
CWPressure AddPressure(
   System.int NPressureType,
   System.object DispArray,
   System.object RegGeom,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWPressure^ AddPressure(
   System.int NPressureType,
   System.Object^ DispArray,
   System.Object^ RegGeom,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NPressureType`: Pressure type as defined in [swsPressureType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsPressureType_e.html)
- `DispArray`: Array of entities (faces or shell edges) to which to apply pressure
- `RegGeom`: Reference geometry for direction
- `ErrorCode`: Error as defined in [swsPressureError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsPressureError_e.html)

### Return Value

[Pressure](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWPressure.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddPressure](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddPressure.html).

## Examples

[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)

## Remarks

Pass null or nothing if reference geometry is not used. If you pass a Dispatch pointer, it is ignored.

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
