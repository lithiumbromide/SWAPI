---
title: "TextScale Property (ICalloutVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutVariable"
member: "TextScale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~TextScale.html"
---

# TextScale Property (ICalloutVariable)

Gets or sets the value with which to scale the tolerance font for a hole callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property TextScale As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutVariable
Dim value As System.Double

instance.TextScale = value

value = instance.TextScale
```

### C#

```csharp
System.double TextScale {get; set;}
```

### C++/CLI

```cpp
property System.double TextScale {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 <= value with which to scale the tolerance font <= 10.0

## VBA Syntax

See [CalloutVariable::TextScale](ms-its:sldworksapivb6.chm::/sldworks~CalloutVariable~TextScale.html).

## Remarks

Set [ICalloutVariable::UseTextScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~UseTextScale.html) to true to enable setting this property.

## See Also

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html)
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.html)
[ICalloutVariable::FitTextScale Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitTextScale.html)
[ICalloutVariable::FitUseTextScale Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitUseTextScale.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
