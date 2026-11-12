---
title: "GetDecalsCount Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetDecalsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetDecalsCount.html"
---

# GetDecalsCount Method (IComponent2)

Gets the number of decals applied to this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDecalsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Integer

value = instance.GetDecalsCount()
```

### C#

```csharp
System.int GetDecalsCount()
```

### C++/CLI

```cpp
System.int GetDecalsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of decals

## VBA Syntax

See [Component2::GetDecalsCount](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetDecalsCount.html).

## Remarks

Call this method before calling [IComponent2::IGetDecals](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IGetDecals.html) to get the size of the array for that method.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetDecals Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetDecals.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
