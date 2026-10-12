---
title: "GetTableAnnotations Method (IFamilyTableFeature)"
project: "SOLIDWORKS API Help"
interface: "IFamilyTableFeature"
member: "GetTableAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~GetTableAnnotations.html"
---

# GetTableAnnotations Method (IFamilyTableFeature)

Gets the annotations for this family table feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableAnnotations() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFamilyTableFeature
Dim value As System.Object

value = instance.GetTableAnnotations()
```

### C#

```csharp
System.object GetTableAnnotations()
```

### C++/CLI

```cpp
System.Object^ GetTableAnnotations();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IFamilyTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableAnnotation.html)s

## VBA Syntax

See [FamilyTableFeature::GetTableAnnotations](ms-its:sldworksapivb6.chm::/sldworks~FamilyTableFeature~GetTableAnnotations.html).

## Remarks

Use [IFamilyTableFeature::GetTableAnnotationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~GetTableAnnotationCount.html) to determine the size of the array returned by this method.

## See Also

[IFamilyTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature.html)
[IFamilyTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
