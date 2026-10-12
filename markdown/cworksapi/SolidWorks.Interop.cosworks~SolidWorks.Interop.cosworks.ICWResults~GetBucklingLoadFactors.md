---
title: "GetBucklingLoadFactors Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetBucklingLoadFactors"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetBucklingLoadFactors.html"
---

# GetBucklingLoadFactors Method (ICWResults)

Gets the buckling load factors.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBucklingLoadFactors( _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetBucklingLoadFactors(ErrorCode)
```

### C#

```csharp
System.object GetBucklingLoadFactors(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetBucklingLoadFactors(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of buckling load factors

## VBA Syntax

See [CWResults::GetBucklingLoadFactors](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetBucklingLoadFactors.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
