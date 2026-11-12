---
title: "UseInertialRelief2 Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "UseInertialRelief2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~UseInertialRelief2.html"
---

# UseInertialRelief2 Property (ICWStaticStudyOptions)

Gets or sets whether to solve using inertial relief.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseInertialRelief2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Boolean

instance.UseInertialRelief2 = value

value = instance.UseInertialRelief2
```

### C#

```csharp
System.bool UseInertialRelief2 {get; set;}
```

### C++/CLI

```cpp
property System.bool UseInertialRelief2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

- -1 or true = Use inertial relief
- 0 or false = Do not use inertial relief

(see **Remarks**)

## VBA Syntax

See [CWStaticStudyOptions::UseInertialRelief2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~UseInertialRelief2.html).

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
