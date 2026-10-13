---
title: "Precision Property (ICalloutLengthVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutLengthVariable"
member: "Precision"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutLengthVariable~Precision.html"
---

# Precision Property (ICalloutLengthVariable)

Gets or sets number of digits after the decimal point to display the primary precision value for a length variable in a hole callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property Precision As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutLengthVariable
Dim value As System.Integer

instance.Precision = value

value = instance.Precision
```

### C#

```csharp
System.int Precision {get; set;}
```

### C++/CLI

```cpp
property System.int Precision {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of digits after the decimal point to display the primary precision value

## VBA Syntax

See [CalloutLengthVariable::Precision](ms-its:sldworksapivb6.chm::/sldworks~CalloutLengthVariable~Precision.html).

## Examples

[Get and Set Hole Callout Variables (C#)](Get_and_Set_Hole_Callout_Variables_Example_CSharp.htm)
[Get and Set Hole Callout Variables (VB.NET)](Get_and_Set_Hole_Callout_Variables_Example_VBNET.htm)
[Get and Set Hole Callout Variables (VBA)](Get_and_Set_Hole_Callout_Variables_Example_VB.htm)

## Remarks

Call [IDisplayDimension::SetPrecision3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetPrecision3.html) to set the dual precision value for a display dimension for a hole callout.

## See Also

[ICalloutLengthVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutLengthVariable.html)
[ICalloutLengthVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutLengthVariable_members.html)
[ICalloutLengthVariable::TolerancePrecision Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutLengthVariable~TolerancePrecision.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
