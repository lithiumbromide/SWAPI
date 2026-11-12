---
title: "ToleranceMax Property (ICalloutVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutVariable"
member: "ToleranceMax"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ToleranceMax.html"
---

# ToleranceMax Property (ICalloutVariable)

Gets or sets the maximum tolerance for a hole callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property ToleranceMax As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutVariable
Dim value As System.Double

instance.ToleranceMax = value

value = instance.ToleranceMax
```

### C#

```csharp
System.double ToleranceMax {get; set;}
```

### C++/CLI

```cpp
property System.double ToleranceMax {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Maximum tolerance

## VBA Syntax

See [CalloutVariable::ToleranceMax](ms-its:sldworksapivb6.chm::/sldworks~CalloutVariable~ToleranceMax.html).

## See Also

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html)
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.html)
[ICalloutVariable::ToleranceMin Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ToleranceMin.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
