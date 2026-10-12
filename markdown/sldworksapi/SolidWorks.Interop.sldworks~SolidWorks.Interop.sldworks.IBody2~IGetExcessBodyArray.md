---
title: "IGetExcessBodyArray Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IGetExcessBodyArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetExcessBodyArray.html"
---

# IGetExcessBodyArray Method (IBody2)

Gets the excess bodies after sewing.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetExcessBodyArray() As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As Body2

value = instance.IGetExcessBodyArray()
```

### C#

```csharp
Body2 IGetExcessBodyArray()
```

### C++/CLI

```cpp
Body2^ IGetExcessBodyArray();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of excess [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IGetExcessBodyCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetExcessBodyCount.html)
[IBody2::GetExcessBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetExcessBodyArray.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
