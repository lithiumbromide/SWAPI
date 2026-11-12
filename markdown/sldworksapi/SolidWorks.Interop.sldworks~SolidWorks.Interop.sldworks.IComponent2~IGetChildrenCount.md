---
title: "IGetChildrenCount Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IGetChildrenCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetChildrenCount.html"
---

# IGetChildrenCount Method (IComponent2)

Gets the number of children components for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetChildrenCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Integer

value = instance.IGetChildrenCount()
```

### C#

```csharp
System.int IGetChildrenCount()
```

### C++/CLI

```cpp
System.int IGetChildrenCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of children

## Examples

[Show All Components (VBA)](Show_All_Components_Example_VB.htm)

## Remarks

This method returns a single-level count. The [IComponent2::GetChildren](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetChildren.html) and [IComponent2::IGetChildren](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IGetChildren.html) do not recurse sub-assemblies.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
