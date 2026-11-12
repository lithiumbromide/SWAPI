---
title: "VariableType Property (ICalloutVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutVariable"
member: "VariableType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~VariableType.html"
---

# VariableType Property (ICalloutVariable)

Gets the type of specific hole callout variable.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property VariableType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutVariable
Dim value As System.Integer

value = instance.VariableType
```

### C#

```csharp
System.int VariableType {get;}
```

### C++/CLI

```cpp
property System.int VariableType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of specific hole callout variable as defined in [swCalloutVariable_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCalloutVariable_e.html)

## VBA Syntax

See [CalloutVariable::VariableType](ms-its:sldworksapivb6.chm::/sldworks~CalloutVariable~VariableType.html).

## Remarks

Call [ICalloutVariable::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~Type.html) to get the type of general hole callout variable.

## See Also

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html)
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
