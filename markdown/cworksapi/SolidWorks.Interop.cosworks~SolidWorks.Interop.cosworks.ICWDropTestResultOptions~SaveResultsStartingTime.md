---
title: "SaveResultsStartingTime Property (ICWDropTestResultOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestResultOptions"
member: "SaveResultsStartingTime"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestResultOptions~SaveResultsStartingTime.html"
---

# SaveResultsStartingTime Property (ICWDropTestResultOptions)

Gets or sets the time to start saving results after the moment of impact.

## Syntax

### Visual Basic (Declaration)

```vb
Property SaveResultsStartingTime As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestResultOptions
Dim value As System.Double

instance.SaveResultsStartingTime = value

value = instance.SaveResultsStartingTime
```

### C#

```csharp
System.double SaveResultsStartingTime {get; set;}
```

### C++/CLI

```cpp
property System.double SaveResultsStartingTime {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Start time in microseconds

## VBA Syntax

See [CWDropTestResultOptions::SaveResultsStartingTime](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestResultOptions~SaveResultsStartingTime.html).

## Examples

See the examples in [ICWDropTestResultOptions](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestResultOptions.html).

## See Also

[ICWDropTestResultOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestResultOptions.html)
[ICWDropTestResultOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestResultOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
