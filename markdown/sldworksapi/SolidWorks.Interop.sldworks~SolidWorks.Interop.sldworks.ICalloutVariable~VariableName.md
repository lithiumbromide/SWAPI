---
title: "VariableName Property (ICalloutVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutVariable"
member: "VariableName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~VariableName.html"
---

# VariableName Property (ICalloutVariable)

Gets the name of the hole callout variable as it appears in the Dimension PropertyManager page in the **Dimension Text** box.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property VariableName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutVariable
Dim value As System.String

value = instance.VariableName
```

### C#

```csharp
System.string VariableName {get;}
```

### C++/CLI

```cpp
property System.String^ VariableName {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the hole callout variable as it appears in the Dimension PropertyManager page in the **Dimension Text** box

## VBA Syntax

See [CalloutVariable::VariableName](ms-its:sldworksapivb6.chm::/sldworks~CalloutVariable~VariableName.html).

## Examples

[Get and Set Hole Callout Variables (C#)](Get_and_Set_Hole_Callout_Variables_Example_CSharp.htm)
[Get and Set Hole Callout Variables (VB.NET)](Get_and_Set_Hole_Callout_Variables_Example_VBNET.htm)
[Get and Set Hole Callout Variables (VBA)](Get_and_Set_Hole_Callout_Variables_Example_VB.htm)

## Remarks

Call [ICalloutVariable::UserReadableVariableName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~UserReadableVariableName.html) to get the name of the hole callout variable as it appears in the Dimension PropertyManager page in the **Callout value** drop-down list box.

## See Also

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html)
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
