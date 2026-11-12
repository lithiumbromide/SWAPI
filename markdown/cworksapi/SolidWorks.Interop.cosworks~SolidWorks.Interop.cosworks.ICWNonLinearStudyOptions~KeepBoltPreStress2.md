---
title: "KeepBoltPreStress2 Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "KeepBoltPreStress2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~KeepBoltPreStress2.html"
---

# KeepBoltPreStress2 Property (ICWNonLinearStudyOptions)

Gets or sets whether to keep bolt pre-stress.

## Syntax

### Visual Basic (Declaration)

```vb
Property KeepBoltPreStress2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Boolean

instance.KeepBoltPreStress2 = value

value = instance.KeepBoltPreStress2
```

### C#

```csharp
System.bool KeepBoltPreStress2 {get; set;}
```

### C++/CLI

```cpp
property System.bool KeepBoltPreStress2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to keep bolt pre-stress, 0 or false to not (see **Remarks**)

## VBA Syntax

See [CWNonLinearStudyOptions::KeepBoltPreStress2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~KeepBoltPreStress2.html).

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
