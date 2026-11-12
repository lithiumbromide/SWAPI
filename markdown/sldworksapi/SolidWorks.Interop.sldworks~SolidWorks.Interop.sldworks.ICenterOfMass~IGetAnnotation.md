---
title: "IGetAnnotation Method (ICenterOfMass)"
project: "SOLIDWORKS API Help"
interface: "ICenterOfMass"
member: "IGetAnnotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterOfMass~IGetAnnotation.html"
---

# IGetAnnotation Method (ICenterOfMass)

Gets the annotation for this center of mass.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAnnotation() As Annotation
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterOfMass
Dim value As Annotation

value = instance.IGetAnnotation()
```

### C#

```csharp
Annotation IGetAnnotation()
```

### C++/CLI

```cpp
Annotation^ IGetAnnotation();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to the [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) object
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[ICenterOfMass Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterOfMass.html)
[ICenterOfMass Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterOfMass_members.html)
[ICenterOfMass::GetAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterOfMass~GetAnnotation.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
