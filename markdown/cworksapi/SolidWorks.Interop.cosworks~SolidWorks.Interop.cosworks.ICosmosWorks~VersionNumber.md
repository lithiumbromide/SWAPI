---
title: "VersionNumber Property (ICosmosWorks)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICosmosWorks"
member: "VersionNumber"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICosmosWorks~VersionNumber.html"
---

# VersionNumber Property (ICosmosWorks)

Gets the SOLIDWORKS Simulation version number.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property VersionNumber As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICosmosWorks
Dim value As System.String

value = instance.VersionNumber
```

### C#

```csharp
System.string VersionNumber {get;}
```

### C++/CLI

```cpp
property System.String^ VersionNumber {
   System.String^ get();
}
```

### Property Value

Version number

## VBA Syntax

See [CosmosWorks::VersionNumber](ms-its:cworksapivb6.chm::/CosmosWorksLib~CosmosWorks~VersionNumber.html).

## See Also

[ICosmosWorks Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICosmosWorks.html)
[ICosmosWorks Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICosmosWorks_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
