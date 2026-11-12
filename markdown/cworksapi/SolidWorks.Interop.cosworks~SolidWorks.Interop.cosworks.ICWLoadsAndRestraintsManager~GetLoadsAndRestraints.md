---
title: "GetLoadsAndRestraints Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "GetLoadsAndRestraints"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~GetLoadsAndRestraints.html"
---

# GetLoadsAndRestraints Method (ICWLoadsAndRestraintsManager)

Gets the load or restraint at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLoadsAndRestraints( _
   ByVal NIndex As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As CWLoadsAndRestraints
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim NIndex As System.Integer
Dim ErrorCode As System.Integer
Dim value As CWLoadsAndRestraints

value = instance.GetLoadsAndRestraints(NIndex, ErrorCode)
```

### C#

```csharp
CWLoadsAndRestraints GetLoadsAndRestraints(
   System.int NIndex,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWLoadsAndRestraints^ GetLoadsAndRestraints(
   System.int NIndex,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NIndex`: 0-based index of load or restraint to get
- `ErrorCode`: Error as defined in [swsLoadsAndRestraintsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLoadsAndRestraintsError_e.html)

### Return Value

[Load or restraint](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWLoadsAndRestraints.html) at specified index

## VBA Syntax

See [CWLoadsAndRestraintsManager::GetLoadsAndRestraints](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~GetLoadsAndRestraints.html).

## Examples

[Create and Edit Bolt and Pin Connectors (VBA)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VB.htm)
[Create and Edit Bolt and Pin Connectors (VB.NET)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VBNET.htm)
[Create and Edit Bolt and Pin Connectors (C#)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_CSharp.htm)

## Remarks

Before calling this method, call [ICWLoadsAndRestraintsManager::Count](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWLoadsAndRestraintsManager~GetLoadsAndRestraints.html) to get a valid value for NIndex. NIndex does not correspond to the vertical position of the load or restraint in the Simulation Study tree.

Cast the return object to the load or restraint class of interest (e.g., CWPinConnector in the example).

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)
[ICWLoadsAndRestraintsManager::CopyLoadsAndRestraintsToStudy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~CopyLoadsAndRestraintsToStudy.html)
[ICWLoadsAndRestraintsManager::DeleteLoadsAndRestraints Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~DeleteLoadsAndRestraints.html)
[ICWLoadsAndRestraintsManager::GetEdgeWeldConnector Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~GetEdgeWeldConnector.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
