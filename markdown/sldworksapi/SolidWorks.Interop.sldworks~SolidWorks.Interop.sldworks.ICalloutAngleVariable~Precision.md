---
title: "Precision Property (ICalloutAngleVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutAngleVariable"
member: "Precision"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutAngleVariable~Precision.html"
---

# Precision Property (ICalloutAngleVariable)

Gets or sets the number of digits to display after the decimal point of the angle value of this hole callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property Precision As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutAngleVariable
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

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Number of digits displayed after the decimal point of the angle value

## VBA Syntax

See

[CalloutAngleVariable::Precision](ms-its:sldworksapivb6.chm::/sldworks~CalloutAngleVariable~Precision.html)

.

## See Also

[ICalloutAngleVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutAngleVariable.html)

[ICalloutAngleVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutAngleVariable_members.html)

[ICalloutAngleVariable::Angle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutAngleVariable~Angle.html)

## Availability

SOLIDWORKS 2025 FCS, Revision Number 33
