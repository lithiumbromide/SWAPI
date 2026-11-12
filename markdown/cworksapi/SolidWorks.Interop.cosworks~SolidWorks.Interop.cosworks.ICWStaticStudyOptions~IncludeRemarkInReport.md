---
title: "IncludeRemarkInReport Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "IncludeRemarkInReport"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~IncludeRemarkInReport.html"
---

# IncludeRemarkInReport Property (ICWStaticStudyOptions)

Obsolete. Superseded by [ICWStaticStudyOptions::IncludeRemarkInReport2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~IncludeRemarkInReport2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeRemarkInReport As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Integer

instance.IncludeRemarkInReport = value

value = instance.IncludeRemarkInReport
```

### C#

```csharp
System.int IncludeRemarkInReport {get; set;}
```

### C++/CLI

```cpp
property System.int IncludeRemarkInReport {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to include a report remark, 0 to not

## VBA Syntax

See [CWStaticStudyOptions::IncludeRemarkInReport](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~IncludeRemarkInReport.html).

## Examples

See the [ICWStaticStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html) examples.

## Remarks

After setting this property to 1, set the remark using [ICWStaticStudyOptions::RemarkComment](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~RemarkComment.html).

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
