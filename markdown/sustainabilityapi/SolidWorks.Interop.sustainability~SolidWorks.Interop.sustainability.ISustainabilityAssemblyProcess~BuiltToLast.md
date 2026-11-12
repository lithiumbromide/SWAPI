---
title: "BuiltToLast Property (ISustainabilityAssemblyProcess)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityAssemblyProcess"
member: "BuiltToLast"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyProcess~BuiltToLast.html"
---

# BuiltToLast Property (ISustainabilityAssemblyProcess)

Gets or sets the length of time that the assembly is built to last.

## Syntax

### Visual Basic (Declaration)

```vb
Property BuiltToLast As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityAssemblyProcess
Dim value As System.Double

instance.BuiltToLast = value

value = instance.BuiltToLast
```

### C#

```csharp
System.double BuiltToLast {get; set;}
```

### C++/CLI

```cpp
property System.double BuiltToLast {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Length of time in [ISustainabilityAssemblyProcess::DurationType](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityAssemblyProcess~DurationType.html) units that the assembly is built to last

## VBA Syntax

See [SustainabilityAssemblyProcess::BuiltToLast](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityAssemblyProcess~BuiltToLast.html).

## Examples

See the examples in [ISustainabilityAssemblyProcess](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityAssemblyProcess.html).

## See Also

[ISustainabilityAssemblyProcess Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyProcess.html)
[ISustainabilityAssemblyProcess Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyProcess_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
