---
title: "Length Property (ICalloutLengthVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutLengthVariable"
member: "Length"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutLengthVariable~Length.html"
---

# Length Property (ICalloutLengthVariable)

Gets or sets the length for this length variable in a hole callout.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Length As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutLengthVariable
Dim value As System.Double

value = instance.Length
```

### C#

```csharp
System.double Length {get;}
```

### C++/CLI

```cpp
property System.double Length {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Length

## VBA Syntax

See [CalloutLengthVariable::Length](ms-its:sldworksapivb6.chm::/sldworks~CalloutLengthVariable~Length.html).

## Examples

[Get and Set Hole Callout Variables (C#)](Get_and_Set_Hole_Callout_Variables_Example_CSharp.htm)
[Get and Set Hole Callout Variables (VB.NET)](Get_and_Set_Hole_Callout_Variables_Example_VBNET.htm)
[Get and Set Hole Callout Variables (VBA)](Get_and_Set_Hole_Callout_Variables_Example_VB.htm)

## See Also

[ICalloutLengthVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutLengthVariable.html)
[ICalloutLengthVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutLengthVariable_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
