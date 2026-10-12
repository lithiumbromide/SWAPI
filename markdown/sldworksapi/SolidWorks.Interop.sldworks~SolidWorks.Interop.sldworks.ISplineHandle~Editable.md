---
title: "Editable Property (ISplineHandle)"
project: "SOLIDWORKS API Help"
interface: "ISplineHandle"
member: "Editable"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~Editable.html"
---

# Editable Property (ISplineHandle)

Gets or sets whether this spline handle can be edited.

## Syntax

### Visual Basic (Declaration)

```vb
Property Editable As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineHandle
Dim value As System.Boolean

instance.Editable = value

value = instance.Editable
```

### C#

```csharp
System.bool Editable {get; set;}
```

### C++/CLI

```cpp
property System.bool Editable {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Trueif the spline can be edited, false if not

## VBA Syntax

See [SplineHandle::Editable](ms-its:sldworksapivb6.chm::/sldworks~SplineHandle~Editable.html).

## See Also

[ISplineHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.html)
[ISplineHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
