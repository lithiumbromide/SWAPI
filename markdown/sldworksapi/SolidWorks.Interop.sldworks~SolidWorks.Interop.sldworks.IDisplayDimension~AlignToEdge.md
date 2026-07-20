---
title: "AlignToEdge Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "AlignToEdge"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AlignToEdge.html"
---

# AlignToEdge Method (IDisplayDimension)

Aligns this linear dimension with the specified edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function AlignToEdge( _
   ByVal AlignmentEdge As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim AlignmentEdge As System.Object
Dim value As System.Boolean

value = instance.AlignToEdge(AlignmentEdge)
```

### C#

```csharp
System.bool AlignToEdge(
   System.object AlignmentEdge
)
```

### C++/CLI

```cpp
System.bool AlignToEdge(
   System.Object^ AlignmentEdge
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `AlignmentEdge`: [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)

### Return Value

True if successful, false if not

## VBA Syntax

See

[DisplayDimension::AlignToEdge](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~AlignToEdge.html)

.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)

[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)

[IDisplayDimension::SetHorizontal Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetHorizontal.html)

[IDisplayDimension::SetVertical Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetVertical.html)

## Availability

SOLIDWORKS 2024 SP03, Revision Number 32.3
