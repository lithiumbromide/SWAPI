---
title: "IncludeRemarkInReport2 Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "IncludeRemarkInReport2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~IncludeRemarkInReport2.html"
---

# IncludeRemarkInReport2 Property (ICWStaticStudyOptions)

Gets or sets whether to include a remark in the report.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeRemarkInReport2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Boolean

instance.IncludeRemarkInReport2 = value

value = instance.IncludeRemarkInReport2
```

### C#

```csharp
System.bool IncludeRemarkInReport2 {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeRemarkInReport2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to include a report remark, 0 or false to not (see **Remarks**)

## VBA Syntax

See [CWStaticStudyOptions::IncludeRemarkInReport2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~IncludeRemarkInReport2.html).

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
