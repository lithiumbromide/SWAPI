---
title: "IsDangling Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "IsDangling"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IsDangling.html"
---

# IsDangling Method (IAnnotation)

Gets whether this annotation is dangling.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsDangling() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Boolean

value = instance.IsDangling()
```

### C#

```csharp
System.bool IsDangling()
```

### C++/CLI

```cpp
System.bool IsDangling();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the annotation is dangling, false if not

## VBA Syntax

See [Annotation::IsDangling](ms-its:sldworksapivb6.chm::/sldworks~Annotation~IsDangling.html).

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
