---
title: "UseInertialRelief Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "UseInertialRelief"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~UseInertialRelief.html"
---

# UseInertialRelief Property (ICWStaticStudyOptions)

Obsolete. Superseded by [ICWStaticStudyOptions::UseInertialRelief2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~UseInertialRelief2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseInertialRelief As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Integer

instance.UseInertialRelief = value

value = instance.UseInertialRelief
```

### C#

```csharp
System.int UseInertialRelief {get; set;}
```

### C++/CLI

```cpp
property System.int UseInertialRelief {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

- 1 = Use inertial relief
- 0 = Do not use inertial relief

## VBA Syntax

See [CWStaticStudyOptions::UseInertialRelief](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~UseInertialRelief.html).

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWStaticStudyOptions::SolverType Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~SolverType.html)
[ICWStaticStudyOptions::UseInPlaneEffect Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~UseInPlaneEffect.html)
[ICWStaticStudyOptions::UseSoftSpring Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~UseSoftSpring.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
