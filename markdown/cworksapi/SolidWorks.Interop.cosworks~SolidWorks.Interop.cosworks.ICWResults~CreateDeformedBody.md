---
title: "CreateDeformedBody Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "CreateDeformedBody"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateDeformedBody.html"
---

# CreateDeformedBody Method (ICWResults)

Obsolete. Superseded by [ICWResults::CreateDeformedBody2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateDeformedBody2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub CreateDeformedBody( _
   ByVal NCreateAs As System.Integer, _
   ByVal SName As System.String, _
   ByRef ErrorCode As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NCreateAs As System.Integer
Dim SName As System.String
Dim ErrorCode As System.Integer

instance.CreateDeformedBody(NCreateAs, SName, ErrorCode)
```

### C#

```csharp
void CreateDeformedBody(
   System.int NCreateAs,
   System.string SName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
void CreateDeformedBody(
   System.int NCreateAs,
   System.String^ SName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NCreateAs`: Save option as defined in [swsCreateDeformedBodyOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCreateDeformedBodyOption_e.html)
- `SName`: Name of the part or configuration to save
- `ErrorCode`: Error code as defined in [swsCreateDeformedBodyError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCreateDeformedBodyError_e.html)

## VBA Syntax

See [CWResults::CreateDeformedBody](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~CreateDeformedBody.html).

## Remarks

The new document is saved in the location of the original part or assembly.

Deformed shapes of assembly documents are saved as multibody parts.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetDeformedBodyFailedSewOption Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDeformedBodyFailedSewOption.html)
[ICWResults::SetDeformedBodyFailedSewOption Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetDeformedBodyFailedSewOption.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
