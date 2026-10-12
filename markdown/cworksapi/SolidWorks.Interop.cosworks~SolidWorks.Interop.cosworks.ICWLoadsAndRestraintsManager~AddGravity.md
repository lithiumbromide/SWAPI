---
title: "AddGravity Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddGravity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddGravity.html"
---

# AddGravity Method (ICWLoadsAndRestraintsManager)

Adds a gravity load.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddGravity( _
   ByVal DispEntity As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWGravity
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim DispEntity As System.Object
Dim ErrorCode As System.Integer
Dim value As CWGravity

value = instance.AddGravity(DispEntity, ErrorCode)
```

### C#

```csharp
CWGravity AddGravity(
   System.object DispEntity,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWGravity^ AddGravity(
   System.Object^ DispEntity,
   [Out] System.int ErrorCode
)
```

### Parameters

- `DispEntity`: Reference geometry entity for direction
- `ErrorCode`: Error as defined in [swsGravityError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsGravityError_e.html)

### Return Value

[Gravity](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWGravity.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddGravity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddGravity.html).

## Examples

[Add Gravity Load (VBA)](Add_Gravity_Load_Example_VB.htm)
[Add Gravity Load (VB.NET)](Add_Gravity_Load_Example_VBNET.htm)
[Add Gravity Load (C#)](Add_Gravity_Load_Example_CSharp.htm)

## Remarks

Mass density must be defined to include the effect of gravity.

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
