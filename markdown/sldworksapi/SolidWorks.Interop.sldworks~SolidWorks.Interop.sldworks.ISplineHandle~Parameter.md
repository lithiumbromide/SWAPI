---
title: "Parameter Property (ISplineHandle)"
project: "SOLIDWORKS API Help"
interface: "ISplineHandle"
member: "Parameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~Parameter.html"
---

# Parameter Property (ISplineHandle)

Gets value in the parameter space of the curve underlying the spline handle.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Parameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineHandle
Dim value As System.Double

value = instance.Parameter
```

### C#

```csharp
System.double Parameter {get;}
```

### C++/CLI

```cpp
property System.double Parameter {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value in the parameter space of the curve underlying the spline handle

## VBA Syntax

See [SplineHandle::Parameter](ms-its:sldworksapivb6.chm::/sldworks~SplineHandle~Parameter.html).

## Remarks

There is no user-interface equivalent for this property as it is typically only useful for API client code.

## See Also

[ISplineHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.html)
[ISplineHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
