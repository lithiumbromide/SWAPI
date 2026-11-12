---
title: "UseLargeStrain2 Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "UseLargeStrain2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~UseLargeStrain2.html"
---

# UseLargeStrain2 Property (ICWNonLinearStudyOptions)

Gets or sets whether to use large strain formulation.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseLargeStrain2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Boolean

instance.UseLargeStrain2 = value

value = instance.UseLargeStrain2
```

### C#

```csharp
System.bool UseLargeStrain2 {get; set;}
```

### C++/CLI

```cpp
property System.bool UseLargeStrain2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

- -1 or true = Use large strain formulation
- 0 or false = Do not use large strain formulation

(see **Remarks**)

## VBA Syntax

See [CWNonLinearStudyOptions::UseLargeStrain2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~UseLargeStrain2.html).

## Remarks

This property:

- is valid for plasticity material models only.
- returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
