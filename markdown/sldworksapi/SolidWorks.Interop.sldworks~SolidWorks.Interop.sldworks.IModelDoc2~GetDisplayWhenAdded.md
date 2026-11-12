---
title: "GetDisplayWhenAdded Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetDisplayWhenAdded"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetDisplayWhenAdded.html"
---

# GetDisplayWhenAdded Method (IModelDoc2)

Gets whether new sketch entities are displayed when created.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayWhenAdded() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.GetDisplayWhenAdded()
```

### C#

```csharp
System.bool GetDisplayWhenAdded()
```

### C++/CLI

```cpp
System.bool GetDisplayWhenAdded();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if new sketch entities are displayed when added, false if not

## VBA Syntax

See [ModelDoc2::GetDisplayWhenAdded](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetDisplayWhenAdded.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SetDisplayWhenAdded Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetDisplayWhenAdded.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
