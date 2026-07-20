---
title: "GetElementType Method (ICoordinateSystemElement)"
project: "SOLIDWORKS API Help"
interface: "ICoordinateSystemElement"
member: "GetElementType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemElement~GetElementType.html"
---

# GetElementType Method (ICoordinateSystemElement)

Gets the type of this coordinate system element.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetElementType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICoordinateSystemElement
Dim value As System.Integer

value = instance.GetElementType()
```

### C#

```csharp
System.int GetElementType()
```

### C++/CLI

```cpp
System.int GetElementType();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Coordinate system element type as defined by

[swCoordSysElementType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCoordSysElementType_e.html)

## VBA Syntax

See

[CoordinateSystemElement::GetElementType](ms-its:sldworksapivb6.chm::/sldworks~CoordinateSystemElement~GetElementType.html)

.

## Examples

See the

[ICoordinateSystemElement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemElement.html)

examples.

## See Also

[ICoordinateSystemElement Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemElement.html)

[ICoordinateSystemElement Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemElement_members.html)

## Availability

SOLIDWORKS 2025 SP01, Revision Number 33.1
