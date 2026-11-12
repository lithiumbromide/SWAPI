---
title: "ComputeFreeBodyForce Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "ComputeFreeBodyForce"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~ComputeFreeBodyForce.html"
---

# ComputeFreeBodyForce Property (ICWStaticStudyOptions)

Obsolete. Superseded by [ICWStaticStudyOptions::ComputeFreeBodyForce2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~ComputeFreeBodyForce2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property ComputeFreeBodyForce As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Integer

instance.ComputeFreeBodyForce = value

value = instance.ComputeFreeBodyForce
```

### C#

```csharp
System.int ComputeFreeBodyForce {get; set;}
```

### C++/CLI

```cpp
property System.int ComputeFreeBodyForce {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to compute free body forces, 0 to not

## VBA Syntax

See [CWStaticStudyOptions::ComputeFreeBodyForce](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~ComputeFreeBodyForce.html).

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
