---
title: "Angle Property (ICalloutAngleVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutAngleVariable"
member: "Angle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutAngleVariable~Angle.html"
---

# Angle Property (ICalloutAngleVariable)

Gets the value of an angle variable in a hole callout.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Angle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutAngleVariable
Dim value As System.Double

value = instance.Angle
```

### C#

```csharp
System.double Angle {get;}
```

### C++/CLI

```cpp
property System.double Angle {
   System.double get();
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Angle in radians

## VBA Syntax

See

[CalloutAngleVariable::Angle](ms-its:sldworksapivb6.chm::/sldworks~CalloutAngleVariable~Angle.html)

.

## Examples

[Get and Set Hole Callout Variables (C#)](Get_and_Set_Hole_Callout_Variables_Example_CSharp.htm)

[Get and Set Hole Callout Variables (VB.NET)](Get_and_Set_Hole_Callout_Variables_Example_VBNET.htm)

[Get and Set Hole Callout Variables (VBA)](Get_and_Set_Hole_Callout_Variables_Example_VB.htm)

## See Also

[ICalloutAngleVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutAngleVariable.html)

[ICalloutAngleVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutAngleVariable_members.html)

[ICalloutAngleVariable::Precision Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutAngleVariable~Precision.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
