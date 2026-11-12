---
title: "ConfigurationName Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "ConfigurationName"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~ConfigurationName.html"
---

# ConfigurationName Property (ICWStudy)

Gets the name of the study's configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ConfigurationName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As System.String

value = instance.ConfigurationName
```

### C#

```csharp
System.string ConfigurationName {get;}
```

### C++/CLI

```cpp
property System.String^ ConfigurationName {
   System.String^ get();
}
```

### Property Value

Configuration name

## VBA Syntax

See [CWStudy::ConfigurationName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~ConfigurationName.html).

## Examples

[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::ActivateConfiguration Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~ActivateConfiguration.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
