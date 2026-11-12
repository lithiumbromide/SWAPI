---
title: "SaveAsReport Method (ISustainabilityEnvironmentalImpact)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityEnvironmentalImpact"
member: "SaveAsReport"
kind: "method"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact~SaveAsReport.html"
---

# SaveAsReport Method (ISustainabilityEnvironmentalImpact)

Saves the environmental impact results to a file of the specified type with the specified name on the specified path.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SaveAsReport( _
   ByVal FileType As System.Integer, _
   ByVal FileName As System.String, _
   ByVal SaveTo As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityEnvironmentalImpact
Dim FileType As System.Integer
Dim FileName As System.String
Dim SaveTo As System.String

instance.SaveAsReport(FileType, FileName, SaveTo)
```

### C#

```csharp
void SaveAsReport(
   System.int FileType,
   System.string FileName,
   System.string SaveTo
)
```

### C++/CLI

```cpp
void SaveAsReport(
   System.int FileType,
   System.String^ FileName,
   System.String^ SaveTo
)
```

### Parameters

- `FileType`: Type of FileName as defined in [swSustainabilitySaveAsFileType_e](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.swSustainabilitySaveAsFileType_e.html)
- `FileName`: Base name of the file to save
- `SaveTo`: Path to FileName

## VBA Syntax

See [SustainabilityEnvironmentalImpact::SaveAsReport](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityEnvironmentalimpact~SaveAsReport.html).

## Examples

See the examples in [ISustainabilityEnvironmentalImpact](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact.html).

## Remarks

Before calling this method, call:

1. [ISustainabilityEnvironmentalImpact::DurationOfUse](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~DurationOfUse.html)
2. [ISustainabilityEnvironmentalImpact::DurationType](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~DurationType.html)
3. [ISustainabilityEnvironmentalImpact::UpdateResults](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityEnvironmentalImpact~UpdateResults.html)

## See Also

[ISustainabilityEnvironmentalImpact Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact.html)
[ISustainabilityEnvironmentalImpact Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityEnvironmentalImpact_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
