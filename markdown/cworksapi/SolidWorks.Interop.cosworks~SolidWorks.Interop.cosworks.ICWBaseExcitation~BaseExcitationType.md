---
title: "BaseExcitationType Property (ICWBaseExcitation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBaseExcitation"
member: "BaseExcitationType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~BaseExcitationType.html"
---

# BaseExcitationType Property (ICWBaseExcitation)

Gets or sets the type of this base excitation.

## Syntax

### Visual Basic (Declaration)

```vb
Property BaseExcitationType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBaseExcitation
Dim value As System.Integer

instance.BaseExcitationType = value

value = instance.BaseExcitationType
```

### C#

```csharp
System.int BaseExcitationType {get; set;}
```

### C++/CLI

```cpp
property System.int BaseExcitationType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of base excitation as defined by [swsBaseExcitationType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsBaseExcitationType_e.html)

## VBA Syntax

See [CWBaseExcitation::BaseExcitationType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBaseExcitation~BaseExcitationType.html).

## Examples

[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)

## See Also

[ICWBaseExcitation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html)
[ICWBaseExcitation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
