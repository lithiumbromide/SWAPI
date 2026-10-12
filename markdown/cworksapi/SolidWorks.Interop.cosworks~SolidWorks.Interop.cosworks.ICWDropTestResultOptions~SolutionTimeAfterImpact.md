---
title: "SolutionTimeAfterImpact Property (ICWDropTestResultOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestResultOptions"
member: "SolutionTimeAfterImpact"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestResultOptions~SolutionTimeAfterImpact.html"
---

# SolutionTimeAfterImpact Property (ICWDropTestResultOptions)

Gets or sets the time interval after the moment of impact for observing and calculating results.

## Syntax

### Visual Basic (Declaration)

```vb
Property SolutionTimeAfterImpact As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestResultOptions
Dim value As System.Double

instance.SolutionTimeAfterImpact = value

value = instance.SolutionTimeAfterImpact
```

### C#

```csharp
System.double SolutionTimeAfterImpact {get; set;}
```

### C++/CLI

```cpp
property System.double SolutionTimeAfterImpact {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Time interval in microseconds

## VBA Syntax

See [CWDropTestResultOptions::SolutionTimeAfterImpact](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestResultOptions~SolutionTimeAfterImpact.html).

## Examples

See the examples in [ICWDropTestResultOptions](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestResultOptions.html).

## See Also

[ICWDropTestResultOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestResultOptions.html)
[ICWDropTestResultOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestResultOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
