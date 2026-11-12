---
title: "GetEdgeWeldResults Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetEdgeWeldResults"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetEdgeWeldResults.html"
---

# GetEdgeWeldResults Method (ICWResults)

Gets the edge weld results for the specified edge weld connector.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdgeWeldResults( _
   ByVal EdgeWeldConnector As System.String, _
   ByVal NUnit As System.Integer, _
   ByRef BPassFail As System.Boolean, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim EdgeWeldConnector As System.String
Dim NUnit As System.Integer
Dim BPassFail As System.Boolean
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetEdgeWeldResults(EdgeWeldConnector, NUnit, BPassFail, ErrorCode)
```

### C#

```csharp
System.object GetEdgeWeldResults(
   System.string EdgeWeldConnector,
   System.int NUnit,
   out System.bool BPassFail,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetEdgeWeldResults(
   System.String^ EdgeWeldConnector,
   System.int NUnit,
   [Out] System.bool BPassFail,
   [Out] System.int ErrorCode
)
```

### Parameters

- `EdgeWeldConnector`: Name of the edge weld connector for which to get edge weld results
- `NUnit`: Unit as defined in [swsUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnit_e.html)
- `BPassFail`: True if the edge weld is safe to use, false if not
- `ErrorCode`: Error code as defined in [swsWeldResultErrorCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsWeldResultErrorCode_e.html)

### Return Value

Array of edge weld results (see **Remarks**)

## VBA Syntax

See [CWResults::GetEdgeWeldResults](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetEdgeWeldResults.html).

## Examples

[Calculate Edge Weld Results (C#)](Calculate_Edge_Weld_Results_Example_CSharp.htm)
[Calculate Edge Weld Results (VB.NET)](Calculate_Edge_Weld_Results_Example_VBNET.htm)
[Calculate Edge Weld Results (VBA)](Calculate_Edge_Weld_Results_Example_VB.htm)

## Remarks

The array of edge weld results contains these minimum, maximum, and mean values in this order:

- Weld size
- Weld throat size
- Joint normal force
- Shear-weld axis force
- Shear-surface normal force
- Bending moment

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)

## Availability

SOLIDWORKS Simulation API 2013 SP3.0
