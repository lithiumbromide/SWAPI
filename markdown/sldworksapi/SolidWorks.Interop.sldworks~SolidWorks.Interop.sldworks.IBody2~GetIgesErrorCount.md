---
title: "GetIgesErrorCount Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetIgesErrorCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetIgesErrorCount.html"
---

# GetIgesErrorCount Method (IBody2)

Gets the number of errors encountered while running an IGES routine.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIgesErrorCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Integer

value = instance.GetIgesErrorCount()
```

### C#

```csharp
System.int GetIgesErrorCount()
```

### C++/CLI

```cpp
System.int GetIgesErrorCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of errors encountered while running an IGES routine

## VBA Syntax

See [Body2::GetIgesErrorCount](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetIgesErrorCount.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetIgesErrorCode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetIgesErrorCode.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
