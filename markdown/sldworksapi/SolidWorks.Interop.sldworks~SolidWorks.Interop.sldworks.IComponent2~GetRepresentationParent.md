---
title: "GetRepresentationParent Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetRepresentationParent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetRepresentationParent.html"
---

# GetRepresentationParent Method (IComponent2)

Gets the representation parent of this [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm) document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRepresentationParent() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.String

value = instance.GetRepresentationParent()
```

### C#

```csharp
System.string GetRepresentationParent()
```

### C++/CLI

```cpp
System.String^ GetRepresentationParent();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Representation parent of this SOLIDWORKS Design connected to the 3DEXPERIENCE platform document

## VBA Syntax

See [Component2::GetRepresentationParent](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetRepresentationParent.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2024 SP01, Revision Number 32.1
