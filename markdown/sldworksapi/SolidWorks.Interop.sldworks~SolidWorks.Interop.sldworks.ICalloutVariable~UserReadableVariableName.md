---
title: "UserReadableVariableName Property (ICalloutVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutVariable"
member: "UserReadableVariableName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~UserReadableVariableName.html"
---

# UserReadableVariableName Property (ICalloutVariable)

Gets the name of the hole callout variable as it appears in the Dimension PropertyManager page in the **Callout value** drop-down list box.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property UserReadableVariableName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutVariable
Dim value As System.String

value = instance.UserReadableVariableName
```

### C#

```csharp
System.string UserReadableVariableName {get;}
```

### C++/CLI

```cpp
property System.String^ UserReadableVariableName {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the hole callout variable as it appears in the Dimension PropertyManager page in **Callout value** drop-down list box

## VBA Syntax

See [CalloutVariable::UserReadableVariableName](ms-its:sldworksapivb6.chm::/sldworks~CalloutVariable~UserReadableVariableName.html).

## Examples

[Get and Set Hole Callout Variables (C#)](Get_and_Set_Hole_Callout_Variables_Example_CSharp.htm)
[Get and Set Hole Callout Variables (VB.NET)](Get_and_Set_Hole_Callout_Variables_Example_VBNET.htm)
[Get and Set Hole Callout Variables (VBA)](Get_and_Set_Hole_Callout_Variables_Example_VB.htm)

## Remarks

Call [ICalloutVariable::VariableName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~VariableName.html) to get the name of the hole callout variable as it appears in the Dimension PropertyManager page in the **Dimension Text** box.

## See Also

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html)
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
