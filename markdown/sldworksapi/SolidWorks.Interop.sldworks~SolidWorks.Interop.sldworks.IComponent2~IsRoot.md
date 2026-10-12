---
title: "IsRoot Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IsRoot"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsRoot.html"
---

# IsRoot Method (IComponent2)

Gets whether this component is the root component.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsRoot() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Boolean

value = instance.IsRoot()
```

### C#

```csharp
System.bool IsRoot()
```

### C++/CLI

```cpp
System.bool IsRoot();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this component is the root component, false if not

## VBA Syntax

See [Component2::IsRoot](ms-its:sldworksapivb6.chm::/sldworks~Component2~IsRoot.html).

## Examples

[Open Assembly in Large Design Review Mode (VBA)](Open_Assembly_in_Large_Design_Review_Mode_Example_VB.htm)
[Open Assembly in Large Design Review Mode (VB.NET)](Open_Assembly_in_Large_Design_Review_Mode_Example_VBNET.htm)
[Open Assembly in Large Design Review Mode (C#)](Open_Assembly_in_Large_Design_Review_Mode_Example_CSharp.htm)

## Remarks

The root component is located at the top of the FeatureManager design tree in an assembly.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetModelDoc2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetModelDoc2.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
