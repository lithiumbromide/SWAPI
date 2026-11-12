---
title: "UseUpdateLoadDirection2 Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "UseUpdateLoadDirection2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~UseUpdateLoadDirection2.html"
---

# UseUpdateLoadDirection2 Property (ICWNonLinearStudyOptions)

Gets or sets whether the direction of the applied load (uniform press, normal force, torque) is updated at every solution step with deflection.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseUpdateLoadDirection2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Boolean

instance.UseUpdateLoadDirection2 = value

value = instance.UseUpdateLoadDirection2
```

### C#

```csharp
System.bool UseUpdateLoadDirection2 {get; set;}
```

### C++/CLI

```cpp
property System.bool UseUpdateLoadDirection2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

- -1 or true = Use update load direction with deflection flag
- 0 or false = Do not use update load direction with deflection flag

(see **Remarks**)

## VBA Syntax

See [CWNonLinearStudyOptions::UseUpdateLoadDirection2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~UseUpdateLoadDirection2.html).

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
