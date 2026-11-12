---
title: "IsSheetMetal Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IsSheetMetal"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsSheetMetal.html"
---

# IsSheetMetal Method (IBody2)

Gets whether this body was created by a sheet metal feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsSheetMetal() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Boolean

value = instance.IsSheetMetal()
```

### C#

```csharp
System.bool IsSheetMetal()
```

### C++/CLI

```cpp
System.bool IsSheetMetal();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this body was created by a sheet metal feature, false if not

## VBA Syntax

See [Body2::IsSheetMetal](ms-its:sldworksapivb6.chm::/sldworks~Body2~IsSheetMetal.html).

## Remarks

This method returns false for sheet metal bodies that are obtained from lightweight components using [IComponent2::GetBodies3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBodies3.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2009 FCS , Revision Number 17.0
