---
title: "RemarkComment Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "RemarkComment"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~RemarkComment.html"
---

# RemarkComment Property (ICWStaticStudyOptions)

Gets or sets a report remark.

## Syntax

### Visual Basic (Declaration)

```vb
Property RemarkComment As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.String

instance.RemarkComment = value

value = instance.RemarkComment
```

### C#

```csharp
System.string RemarkComment {get; set;}
```

### C++/CLI

```cpp
property System.String^ RemarkComment {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Report remark

## VBA Syntax

See [CWStaticStudyOptions::RemarkComment](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~RemarkComment.html).

## Examples

See the [ICWStaticStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html) examples.

## Remarks

This property is valid only if [ICWStaticStudyOptions::IncludeRemarkInReport](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~IncludeRemarkInReport.html) is set to 1.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
