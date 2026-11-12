---
title: "ExtractPositiveBucklingFactorsOnly Property (ICWBucklingStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBucklingStudyOptions"
member: "ExtractPositiveBucklingFactorsOnly"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~ExtractPositiveBucklingFactorsOnly.html"
---

# ExtractPositiveBucklingFactorsOnly Property (ICWBucklingStudyOptions)

Gets or sets whether to extract only positive buckling factors from this buckling study.

## Syntax

### Visual Basic (Declaration)

```vb
Property ExtractPositiveBucklingFactorsOnly As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBucklingStudyOptions
Dim value As System.Boolean

instance.ExtractPositiveBucklingFactorsOnly = value

value = instance.ExtractPositiveBucklingFactorsOnly
```

### C#

```csharp
System.bool ExtractPositiveBucklingFactorsOnly {get; set;}
```

### C++/CLI

```cpp
property System.bool ExtractPositiveBucklingFactorsOnly {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to extract only positive buckling factors, false to extract both negative and positive buckling factors

## VBA Syntax

See [CWBucklingStudyOptions::ExtractPositiveBucklingFactorsOnly](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBucklingStudyOptions~ExtractPositiveBucklingFactorsOnly.html).

## See Also

[ICWBucklingStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html)
[ICWBucklingStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2026 SP0
