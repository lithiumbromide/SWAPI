---
title: "GetPLMID Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetPLMID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetPLMID.html"
---

# GetPLMID Method (IComponent2)

Gets the ID of this [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm) document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPLMID() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.String

value = instance.GetPLMID()
```

### C#

```csharp
System.string GetPLMID()
```

### C++/CLI

```cpp
System.String^ GetPLMID();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

ID of this document

## VBA Syntax

See [Component2::GetPLMID](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetPLMID.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2024 SP01, Revision Number 32.1
