---
title: "UseSoftSpring Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "UseSoftSpring"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~UseSoftSpring.html"
---

# UseSoftSpring Property (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetUseSoftSpring2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetUseSoftSpring2.html) and [ICWDynamicStudyOptions::SetUseSoftSpring2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetUseSoftSpring2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property UseSoftSpring As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim value As System.Integer

instance.UseSoftSpring = value

value = instance.UseSoftSpring
```

### C#

```csharp
System.int UseSoftSpring {get; set;}
```

### C++/CLI

```cpp
property System.int UseSoftSpring {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

- 1 = Use soft springs
- 0 = Do not use soft springs

## VBA Syntax

See [CWDynamicStudyOptions::UseSoftSpring](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~UseSoftSpring.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
