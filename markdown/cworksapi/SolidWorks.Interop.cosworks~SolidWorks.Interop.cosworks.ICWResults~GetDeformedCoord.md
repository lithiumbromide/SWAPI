---
title: "GetDeformedCoord Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetDeformedCoord"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDeformedCoord.html"
---

# GetDeformedCoord Method (ICWResults)

Gets nodal deform coordinates for the specified plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDeformedCoord( _
   ByVal SPlotName As System.String, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim SPlotName As System.String
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetDeformedCoord(SPlotName, ErrorCode)
```

### C#

```csharp
System.object GetDeformedCoord(
   System.string SPlotName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetDeformedCoord(
   System.String^ SPlotName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SPlotName`: Name of plot
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of x, y, z coordinates for all deform nodes

## VBA Syntax

See [CWResults::GetDeformedCoord](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetDeformedCoord.html).

## Examples

[Create Body From Deformed Shape (VBA)](Create_Body_From_Deformed_Shape_Example_VB.htm)
[Create Body From Deformed Shape (VB.NET)](Create_Body_From_Deformed_Shape_Example_VBNET.htm)
[Create Body From Deformed Shape (C#)](Create_Body_From_Deformed_Shape_Example_CSharp.htm)

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::CreateDeformedBody2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateDeformedBody2.html)
[ICWResults::GetDeformedBodyFailedSewOption Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDeformedBodyFailedSewOption.html)
[ICWResults::SetDeformedBodyFailedSewOption Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetDeformedBodyFailedSewOption.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
