---
title: "GetAddToDB Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetAddToDB"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetAddToDB.html"
---

# GetAddToDB Method (IModelDoc2)

Gets whether entities are added directly to the SOLIDWORKS database.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAddToDB() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.GetAddToDB()
```

### C#

```csharp
System.bool GetAddToDB()
```

### C++/CLI

```cpp
System.bool GetAddToDB();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if currently adding items directly to the database, false otherwise

## VBA Syntax

See [ModelDoc2::GetAddToDB](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetAddToDB.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SetAddToDB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetAddToDB.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
