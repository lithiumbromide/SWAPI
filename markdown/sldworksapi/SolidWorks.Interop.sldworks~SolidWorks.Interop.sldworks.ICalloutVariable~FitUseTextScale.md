---
title: "FitUseTextScale Property (ICalloutVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutVariable"
member: "FitUseTextScale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitUseTextScale.html"
---

# FitUseTextScale Property (ICalloutVariable)

Gets or sets whether to use the fit tolerance font scale value in a hole callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property FitUseTextScale As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutVariable
Dim value As System.Boolean

instance.FitUseTextScale = value

value = instance.FitUseTextScale
```

### C#

```csharp
System.bool FitUseTextScale {get; set;}
```

### C++/CLI

```cpp
property System.bool FitUseTextScale {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use the fit tolerance font scale value, false to not

## VBA Syntax

See [CalloutVariable::FitUseTextScale](ms-its:sldworksapivb6.chm::/sldworks~CalloutVariable~FitUseTextScale.html).

## Remarks

Use [ICalloutVariable::FitTextScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~FitTextScale.html) to get or set the fit tolerance font scale value in a hole callout.

## See Also

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html)
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.html)
[ICalloutVariable::TextScale Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~TextScale.html)
[ICalloutVariable::UseTextScale Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~UseTextScale.html)
[ICalloutVariable::HoleFit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~HoleFit.html)
[ICalloutVariable::ShaftFit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ShaftFit.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
