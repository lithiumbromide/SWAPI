---
title: "ToleranceMin Property (ICalloutVariable)"
project: "SOLIDWORKS API Help"
interface: "ICalloutVariable"
member: "ToleranceMin"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ToleranceMin.html"
---

# ToleranceMin Property (ICalloutVariable)

Gets or sets the minimum tolerance for a hole callout.

## Syntax

### Visual Basic (Declaration)

```vb
Property ToleranceMin As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICalloutVariable
Dim value As System.Double

instance.ToleranceMin = value

value = instance.ToleranceMin
```

### C#

```csharp
System.double ToleranceMin {get; set;}
```

### C++/CLI

```cpp
property System.double ToleranceMin {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Minimum tolerance

## VBA Syntax

See [CalloutVariable::ToleranceMin](ms-its:sldworksapivb6.chm::/sldworks~CalloutVariable~ToleranceMin.html).

## See Also

[ICalloutVariable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable.html)
[ICalloutVariable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.html)
[ICalloutVariable::ToleranceMax Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ToleranceMax.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
