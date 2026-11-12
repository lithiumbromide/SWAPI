---
title: "Region Property (ISustainabilityAssemblyProcess)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityAssemblyProcess"
member: "Region"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyProcess~Region.html"
---

# Region Property (ISustainabilityAssemblyProcess)

Gets or sets the region where this assembly is assembled.

## Syntax

### Visual Basic (Declaration)

```vb
Property Region As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityAssemblyProcess
Dim value As System.Integer

instance.Region = value

value = instance.Region
```

### C#

```csharp
System.int Region {get; set;}
```

### C++/CLI

```cpp
property System.int Region {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Region of assembly as defined in [swSustainabilityRegionName_e](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.swSustainabilityRegionName_e.html)

## VBA Syntax

See [SustainabilityAssemblyProcess::Region](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityAssemblyProcess~Region.html).

## Examples

See the examples in [ISustainabilityAssemblyProcess](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityAssemblyProcess.html).

## See Also

[ISustainabilityAssemblyProcess Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyProcess.html)
[ISustainabilityAssemblyProcess Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyProcess_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
