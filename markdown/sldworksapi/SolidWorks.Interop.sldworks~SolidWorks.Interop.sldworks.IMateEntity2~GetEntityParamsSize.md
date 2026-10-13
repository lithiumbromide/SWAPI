---
title: "GetEntityParamsSize Method (IMateEntity2)"
project: "SOLIDWORKS API Help"
interface: "IMateEntity2"
member: "GetEntityParamsSize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~GetEntityParamsSize.html"
---

# GetEntityParamsSize Method (IMateEntity2)

Gets the number of parameters for this mate entity.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntityParamsSize() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMateEntity2
Dim value As System.Integer

value = instance.GetEntityParamsSize()
```

### C#

```csharp
System.int GetEntityParamsSize()
```

### C++/CLI

```cpp
System.int GetEntityParamsSize();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of parameters for this mate entity

## VBA Syntax

See [MateEntity2::GetEntityParamsSize](ms-its:sldworksapivb6.chm::/sldworks~MateEntity2~GetEntityParamsSize.html).

## Remarks

Call this method before calling [IMateEntity2::IGetEntityParams](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateEntity2~IGetEntityParams.html) to determine the size of the array for that method.

## See Also

[IMateEntity2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2.html)
[IMateEntity2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2_members.html)
[IMateEntity2::EntityParams Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~EntityParams.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
