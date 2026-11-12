---
title: "SetDeformedBodyFailedSewOption Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "SetDeformedBodyFailedSewOption"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetDeformedBodyFailedSewOption.html"
---

# SetDeformedBodyFailedSewOption Method (ICWResults)

Sets the option to use when a deformed body fails to sew into a solid object.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDeformedBodyFailedSewOption( _
   ByVal NFailedSewOption As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NFailedSewOption As System.Integer

instance.SetDeformedBodyFailedSewOption(NFailedSewOption)
```

### C#

```csharp
void SetDeformedBodyFailedSewOption(
   System.int NFailedSewOption
)
```

### C++/CLI

```cpp
void SetDeformedBodyFailedSewOption(
   System.int NFailedSewOption
)
```

### Parameters

- `NFailedSewOption`: Option to use when a deformed body fails to sew into a solid object as defined in [swsCreateDeformedBodyFailedSewOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCreateDeformedBodyFailedSewOption_e.html)

## VBA Syntax

See [CWResults::SetDeformedBodyFailedSewOption](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~SetDeformedBodyFailedSewOption.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetDeformedBodyFailedSewOption Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDeformedBodyFailedSewOption.html)
[ICWResults::CreateDeformedBody2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateDeformedBody2.html)
[ICWResults::GetDeformedCoord Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDeformedCoord.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
