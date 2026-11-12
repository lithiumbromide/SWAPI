---
title: "UseSoftSpring Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "UseSoftSpring"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~UseSoftSpring.html"
---

# UseSoftSpring Property (ICWStaticStudyOptions)

Obsolete. Superseded by [ICWStaticStudyOptions::UseSoftSpring2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~UseSoftSpring2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseSoftSpring As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
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

- 1 = Use soft spring to stabilize model
- 0 = Do not use soft spring

## VBA Syntax

See [CWStaticStudyOptions::UseSoftSpring](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~UseSoftSpring.html).

## Examples

See the [ICWBearingLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html) examples.

## Remarks

You can use this property to check the stability of the model. You should set this property to 0 and use proper restraints to stabilize the model for final runs.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWStaticStudyOptions::SolverType Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~SolverType.html)
[ICWStaticStudyOptions::UseInertialRelief Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~UseInertialRelief.html)
[ICWStaticStudyOptions::UseInPlaneEffect Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~UseInPlaneEffect.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
