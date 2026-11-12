---
title: "GetType Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetType.html"
---

# GetType Method (IComponent2)

Gets this lightweight assembly component's document type.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Integer

value = instance.GetType()
```

### C#

```csharp
System.int GetType()
```

### C++/CLI

```cpp
System.int GetType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of document as defined by [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

## VBA Syntax

See [Component2::GetType](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetType.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2024 SP01, Revision Number 32.1
