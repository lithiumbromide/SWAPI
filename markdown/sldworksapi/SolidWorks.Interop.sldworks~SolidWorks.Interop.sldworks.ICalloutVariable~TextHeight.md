---
title: "TextHeight Property (ICalloutVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutVariable"
member: "TextHeight"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~TextHeight.html"
---

# TextHeight Property (ICalloutVariable)

Gets or sets the height of the tolerance text in a hole callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property TextHeight As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutVariable
Dim value As System.Double

instance.TextHeight = value

value = instance.TextHeight
```

### C#

```csharp
System.double TextHeight {get; set;}
```

### C++/CLI

```cpp
property System.double TextHeight {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Height of the tolerance text

## VBA Syntax

See [CalloutVariable::TextHeight](ms-its:sldworksapivb6.chm::/sldworks~CalloutVariable~TextHeight.html).

## See Also

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html)
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.html)
[ICalloutVariable::FitTextHeight Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitTextHeight.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
