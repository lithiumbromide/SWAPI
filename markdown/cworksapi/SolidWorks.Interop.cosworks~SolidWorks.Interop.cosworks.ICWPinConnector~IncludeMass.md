---
title: "IncludeMass Property (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "IncludeMass"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~IncludeMass.html"
---

# IncludeMass Property (ICWPinConnector)

Gets or sets whether to include the mass of the pin in the analysis of this pin connector.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeMass As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector
Dim value As System.Boolean

instance.IncludeMass = value

value = instance.IncludeMass
```

### C#

```csharp
System.bool IncludeMass {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeMass {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to include mass, false to not

## VBA Syntax

See [CWPinConnector::IncludeMass](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~IncludeMass.html).

## Examples

See the [ICWPinConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html) examples.

## Remarks

If you set this property to true, use [ICWPinConnector::MassValue](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~MassValue.html) to set the mass value.

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2009 API
