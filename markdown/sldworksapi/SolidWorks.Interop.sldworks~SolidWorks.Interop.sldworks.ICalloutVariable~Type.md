---
title: "Type Property (ICalloutVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutVariable"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~Type.html"
---

# Type Property (ICalloutVariable)

Gets the type of general hole callout variable.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutVariable
Dim value As System.Integer

value = instance.Type
```

### C#

```csharp
System.int Type {get;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of general hole callout variable as defined in [swCalloutVariableType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCalloutVariableType_e.html)

## VBA Syntax

See [CalloutVariable::Type](ms-its:sldworksapivb6.chm::/sldworks~CalloutVariable~Type.html).

## Examples

[Get and Set Hole Callout Variables (C#)](Get_and_Set_Hole_Callout_Variables_Example_CSharp.htm)
[Get and Set Hole Callout Variables (VB.NET)](Get_and_Set_Hole_Callout_Variables_Example_VBNET.htm)
[Get and Set Hole Callout Variables (VBA)](Get_and_Set_Hole_Callout_Variables_Example_VB.htm)

## Remarks

Use [ICalloutVariable::VariableType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~VariableType.html) to get the type of specific callout variable.

## See Also

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html)
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.html)
[ICalloutAngleVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutAngleVariable.html)
[ICalloutLengthVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutLengthVariable.html)
[ICalloutStringVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutStringVariable.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
