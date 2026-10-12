---
title: "UseInPlaneEffect Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "UseInPlaneEffect"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~UseInPlaneEffect.html"
---

# UseInPlaneEffect Property (ICWStaticStudyOptions)

Obsolete. Superseded by [ICWStaticStudyOptions::UseInPlaneEffect2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~UseInPlaneEffect2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseInPlaneEffect As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Integer

instance.UseInPlaneEffect = value

value = instance.UseInPlaneEffect
```

### C#

```csharp
System.int UseInPlaneEffect {get; set;}
```

### C++/CLI

```cpp
property System.int UseInPlaneEffect {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

- 1 = Use inplane effect
- 0 = Do not use inplane effect

## VBA Syntax

See [CWStaticStudyOptions::UseInPlaneEffect](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~UseInPlaneEffect.html).

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWStaticStudyOptions::SolverType Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~SolverType.html)
[ICWStaticStudyOptions::UseInertialRelief Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~UseInertialRelief.html)
[ICWStaticStudyOptions::UseSoftSpring Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~UseSoftSpring.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
