---
title: "DeSelect Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "DeSelect"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~DeSelect.html"
---

# DeSelect Method (IAnnotation)

Deselects this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeSelect() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Boolean

value = instance.DeSelect()
```

### C#

```csharp
System.bool DeSelect()
```

### C++/CLI

```cpp
System.bool DeSelect();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the feature object was successfully deselected, false otherwise

## VBA Syntax

See [Annotation::DeSelect](ms-its:sldworksapivb6.chm::/sldworks~Annotation~DeSelect.html).

## Remarks

Use [IModelDoc2::DeSelectByID](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~DeSelectByID.html) instead of using this method. This method does not work
well when a PropertyManager page is open or a command is running. IModelDoc2::DeSelectByID
handles selection correctly whether or not a command is running.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
