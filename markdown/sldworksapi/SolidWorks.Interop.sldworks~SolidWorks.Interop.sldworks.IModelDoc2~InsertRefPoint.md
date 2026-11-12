---
title: "InsertRefPoint Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertRefPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertRefPoint.html"
---

# InsertRefPoint Method (IModelDoc2)

Inserts a reference point based on the current selections.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertRefPoint() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.InsertRefPoint()
```

### C#

```csharp
System.bool InsertRefPoint()
```

### C++/CLI

```cpp
System.bool InsertRefPoint();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if successful, false if not

## VBA Syntax

See [ModelDoc2::InsertRefPoint](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertRefPoint.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IRefPoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
