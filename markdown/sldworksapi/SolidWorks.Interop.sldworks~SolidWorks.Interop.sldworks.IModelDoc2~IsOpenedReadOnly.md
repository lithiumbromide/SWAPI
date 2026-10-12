---
title: "IsOpenedReadOnly Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IsOpenedReadOnly"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsOpenedReadOnly.html"
---

# IsOpenedReadOnly Method (IModelDoc2)

Gets whether a SOLIDWORKS document is open in read-only mode.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsOpenedReadOnly() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.IsOpenedReadOnly()
```

### C#

```csharp
System.bool IsOpenedReadOnly()
```

### C++/CLI

```cpp
System.bool IsOpenedReadOnly();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this document is read-only, false if not

## VBA Syntax

See [ModelDoc2::IsOpenedReadOnly](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IsOpenedReadOnly.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::IsOpenedViewOnly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsOpenedViewOnly.html)
[IModelDoc2::SetReadOnlyState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetReadOnlyState.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
