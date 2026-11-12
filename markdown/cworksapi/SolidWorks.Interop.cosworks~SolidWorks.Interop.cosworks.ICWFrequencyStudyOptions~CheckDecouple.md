---
title: "CheckDecouple Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "CheckDecouple"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~CheckDecouple.html"
---

# CheckDecouple Property (ICWFrequencyStudyOptions)

Gets and sets whether to decouple the mixed free body modes of this frequency study.

## Syntax

### Visual Basic (Declaration)

```vb
Property CheckDecouple As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
Dim value As System.Boolean

instance.CheckDecouple = value

value = instance.CheckDecouple
```

### C#

```csharp
System.bool CheckDecouple {get; set;}
```

### C++/CLI

```cpp
property System.bool CheckDecouple {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to decouple the mixed free body modes, false to not

## VBA Syntax

See [CWFrequencyStudyOptions::CheckDecouple](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~CheckDecouple.html).

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2024 SP0
