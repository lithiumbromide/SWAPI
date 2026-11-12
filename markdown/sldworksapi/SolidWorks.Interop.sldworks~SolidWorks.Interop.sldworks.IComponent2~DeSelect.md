---
title: "DeSelect Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "DeSelect"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~DeSelect.html"
---

# DeSelect Method (IComponent2)

Deselects this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeSelect() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Boolean

value = instance.DeSelect()
```

### C#

```csharp
System.bool DeSelect()
```

### C++/CLI

```cpp
System.bool DeSelect();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the component was successfully deselected, false if not

## VBA Syntax

See [Component2::DeSelect](ms-its:sldworksapivb6.chm::/sldworks~Component2~DeSelect.html).

## Remarks

Use [IModelDoc2::DeSelectByID](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~DeSelectByID.html) instead of this method. This method does not work well when a PropertyManager page is open or a command is running. IModelDoc2::DeSelectByID handles selection correctly whether or not a command is running.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::Select3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Select3.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
