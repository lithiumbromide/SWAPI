---
title: "Select Method (ISplineHandle)"
project: "SOLIDWORKS API Help"
interface: "ISplineHandle"
member: "Select"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle~Select.html"
---

# Select Method (ISplineHandle)

Selects a spline handle.

## Syntax

### Visual Basic (Declaration)

```vb
Function Select( _
   ByVal AppendFlag As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISplineHandle
Dim AppendFlag As System.Boolean
Dim value As System.Boolean

value = instance.Select(AppendFlag)
```

### C#

```csharp
System.bool Select(
   System.bool AppendFlag
)
```

### C++/CLI

```cpp
System.bool Select(
   System.bool AppendFlag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AppendFlag`: True appends the spline handle to the selection list, false replaces the selection list with the spline handle

### Return Value

True if the spline handle is selected, false if not

## VBA Syntax

See [SplineHandle::Select](ms-its:sldworksapivb6.chm::/sldworks~SplineHandle~Select.html).

## See Also

[ISplineHandle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle.html)
[ISplineHandle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
