---
title: "DurationType Property (ISustainabilityAssemblyProcess)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityAssemblyProcess"
member: "DurationType"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyProcess~DurationType.html"
---

# DurationType Property (ISustainabilityAssemblyProcess)

Gets or sets the units of time that the assembly is built to last.

## Syntax

### Visual Basic (Declaration)

```vb
Property DurationType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityAssemblyProcess
Dim value As System.Integer

instance.DurationType = value

value = instance.DurationType
```

### C#

```csharp
System.int DurationType {get; set;}
```

### C++/CLI

```cpp
property System.int DurationType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Units of [ISustainabilityAssemblyProcess::BuiltToLast](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityAssemblyProcess~BuiltToLast.html) time as defined in [swSustainabilityDurationType_e](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.swSustainabilityDurationType_e.html)

## VBA Syntax

See [SustainabilityAssemblyProcess::DurationType](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityAssemblyProcess~DurationType.html).

## Examples

See the examples in [ISustainabilityAssemblyProcess](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityAssemblyProcess.html).

## See Also

[ISustainabilityAssemblyProcess Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyProcess.html)
[ISustainabilityAssemblyProcess Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyProcess_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
